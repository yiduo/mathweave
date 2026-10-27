"""Synthetic finite-step certificate separation; target called only explicitly."""
from __future__ import annotations

from fractions import Fraction
from itertools import product
import time

from .attempts import record_progress, set_execution_phase
from .mass_action_reference import expanded_model, evaluate, verify_reference, expected_report


def parse_model(model):
    d = len(model['species'])
    if not d or len(set(model['species'])) != d or model.get('variable_rates', False):
        raise ValueError('Invalid species or nonconstant rates')
    result = []
    for e in model['reactions']:
        a, b = e['source'], e['target']
        if (len(a) != d or len(b) != d or a == b
                or any(type(n) is not int or n < 0 for n in a+b)):
            raise ValueError('Invalid complexes')
        rate = Fraction(e['rate'])
        if rate <= 0:
            raise ValueError('Nonpositive rate')
        result.append((tuple(a), tuple(b), rate))
    return result


def source_eligible(model, initial):
    reactions = parse_model(model)
    if len(initial) != len(model['species']) or any(x <= 0 for x in initial):
        raise ValueError('Initial point is not strictly positive')
    graph = {}
    for a, b, _ in reactions:
        graph.setdefault(a, set()).add(b); graph.setdefault(b, set())
    for a, b, _ in reactions:
        visited, todo = set(), [b]
        while todo:
            current = todo.pop()
            if current not in visited:
                visited.add(current); todo.extend(graph[current]-visited)
        if a not in visited:
            return False
    return True


def vector_field(model, state):
    result = [Fraction(0) for _ in state]
    for a, b, rate in parse_model(model):
        flux = rate
        for x, power in zip(state, a):
            flux *= x ** power
        for i in range(len(state)):
            result[i] += flux*(b[i]-a[i])
    return result


def build_reference(model, initial):
    if not source_eligible(model, initial):
        raise ValueError('Not weakly reversible')
    if 'conservation_weights' not in model:
        # This bounded test interface covers precisely this independently
        # checkable nonconservative old analytic control, not arbitrary systems.
        reactions = parse_model(model)
        if (len(initial) != 1 or len(reactions) != 2
                or {(a, b) for a, b, _ in reactions} != {((1,), (2,)), ((2,), (1,))}):
            raise ValueError('No independent reference supplied; source may remain eligible')
        rates = {(a, b): k for a, b, k in reactions}
        equilibrium = rates[((1,), (2,))]/rates[((2,), (1,))]
        return {'kind': 'logistic_interval', 'lower': str(min(initial[0], equilibrium)),
                'upper': [str(max(initial[0], equilibrium))]}
    weights = [Fraction(x) for x in model['conservation_weights']]
    if len(weights) != len(initial) or any(x <= 0 for x in weights):
        raise ValueError('Not a positive conservation vector')
    mass = sum(w*x for w, x in zip(weights, initial))
    upper = [mass/w for w in weights]
    loss = [Fraction(0) for _ in initial]
    for a, b, rate in parse_model(model):
        if sum(w*(y-x) for w, x, y in zip(weights, a, b)) != 0:
            raise ValueError('Reaction does not conserve supplied mass')
        for i in range(len(initial)):
            if a[i] <= b[i]:
                continue
            term = rate*(a[i]-b[i])
            for j in range(len(initial)):
                term *= upper[j]**(a[j]-(i == j))
            loss[i] += term
    return {'kind': 'conservative_loss', 'mass': str(mass),
            'upper': [str(x) for x in upper], 'loss': [str(x) for x in loss]}


def finite_lower(initial, certificate, horizon, exponent_cap):
    if certificate['kind'] == 'logistic_interval':
        return [certificate['lower']]
    result = []
    for x, k in zip(initial, certificate['loss']):
        z = Fraction(k)*horizon
        exponent = -(-z.numerator//z.denominator)
        if exponent > exponent_cap:
            raise ValueError('Frozen rational reference exponent cap exceeded')
        # exp(-z) >= 3^(-ceil(z)), since e < 3; no floating exp evaluation.
        result.append(str(x/Fraction(3**exponent)))
    return result


def assess_report(claims, eligible, reference_verified, updates):
    result = {}
    for kind in claims:
        if kind == 'conditional_continuous_permanence':
            result[kind] = 'conditional' if eligible else 'unsupported'
        elif kind == 'finite_continuous_positive':
            result[kind] = 'supported' if reference_verified else 'unsupported'
        elif kind in {'finite_euler_nonnegative', 'finite_euler_positive'}:
            accepted = all(x >= 0 if kind.endswith('nonnegative') else x > 0
                           for row in updates for x in row)
            result[kind] = 'supported' if accepted else 'refuted'
        elif kind in {'eventual_numerical_permanence', 'uniform_initial_burnin',
                      'arbitrary_step_from_continuous_theorem'}:
            result[kind] = 'unsupported'
        else:
            raise ValueError('Unknown requested report claim')
    return result


def evaluate_case(model, initial, step, steps, exponent_cap, claims, progress_id=None):
    if step <= 0 or type(steps) is not int or steps < 1:
        raise ValueError('Invalid time discretization')
    costs = {}; tick = time.perf_counter()
    eligible = source_eligible(model, initial)
    costs['source_qualification_seconds'] = time.perf_counter()-tick
    tick = time.perf_counter()
    coefficients, independent_weak = expanded_model(model)
    costs['old_polynomial_setup_seconds'] = time.perf_counter()-tick
    if not eligible or not independent_weak:
        raise ValueError('Primary fixture outside the frozen source class')
    tick = time.perf_counter(); certificate = build_reference(model, initial)
    costs['reference_production_seconds'] = time.perf_counter()-tick
    tick = time.perf_counter()
    reference = verify_reference(model, initial, certificate)
    costs['independent_reference_verification_seconds'] = time.perf_counter()-tick
    if progress_id is not None:
        record_progress({'phase': 'finite_reference', 'case_id': progress_id,
                         'certificate': certificate, 'verification': reference})
    costs['reaction_euler_seconds'] = 0.0; costs['old_expanded_euler_seconds'] = 0.0
    state = initial[:]; trace = []; exact_matches = True; conserved = True
    new_updates = []; old_updates = []
    # The strong old method computes the very same actual finite coordinate
    # updates. Source/theorem labels cannot replace this calculation.
    for j in range(steps):
        tick = time.perf_counter()
        new = [x+step*f for x, f in zip(state, vector_field(model, state))]
        costs['reaction_euler_seconds'] += time.perf_counter()-tick
        tick = time.perf_counter()
        old = [x+step*f for x, f in zip(state, evaluate(coefficients, state))]
        costs['old_expanded_euler_seconds'] += time.perf_counter()-tick
        new_updates.append(new); old_updates.append(old)
        equal = new == old; exact_matches = exact_matches and equal
        if certificate['kind'] == 'conservative_loss':
            weights = [Fraction(x) for x in model['conservation_weights']]
            conserved = conserved and sum(a*b for a, b in zip(weights, new)) == Fraction(certificate['mass'])
        trace.append({'step': j+1, 'state_before': [str(x) for x in state],
                      'reaction_update': [str(x) for x in new],
                      'old_expanded_update': [str(x) for x in old],
                      'exact_match': equal, 'negative': any(x < 0 for x in new),
                      'strictly_positive': all(x > 0 for x in new)})
        if progress_id is not None:
            record_progress({'phase': 'euler_step', 'case_id': progress_id,
                             'transition': trace[-1]})
        state = new
        if any(x <= 0 for x in new):
            break  # Never interpret mass action on an inadmissible negative state.
    horizon = step*len(trace)
    tick = time.perf_counter()
    lower = finite_lower(initial, certificate, horizon, exponent_cap)
    costs['finite_lower_seconds'] = time.perf_counter()-tick
    negative = any(x['negative'] for x in trace)
    tick = time.perf_counter(); report = assess_report(claims, eligible, reference['verified'], new_updates)
    costs['report_seconds'] = time.perf_counter()-tick
    tick = time.perf_counter(); oracle_report = expected_report(independent_weak, reference['verified'], old_updates)
    costs['old_report_seconds'] = time.perf_counter()-tick
    if set(claims) != set(oracle_report):
        raise ValueError('Missing or unexpected frozen report claims')
    return {'source_eligible': eligible, 'reference': certificate,
            'independent_reference': reference, 'horizon': str(horizon),
            'finite_continuous_lower': lower, 'trace': trace,
            'reaction_expanded_equality': exact_matches,
            'weighted_conservation': conserved, 'euler_has_negative': negative,
            'old_coordinate_guard_catches_negative': any(x < 0 for row in old_updates for x in row),
            'separated_guard_catches_negative': report['finite_euler_nonnegative'] == 'refuted',
            'report': report, 'independent_old_report': oracle_report,
            'report_agreement': report == oracle_report,
            'finite_euler_all_nonnegative': all(Fraction(v) >= 0 for t in trace for v in t['reaction_update']),
            'eventual_numerical_permanence_certified': report['eventual_numerical_permanence'] == 'supported',
            'new_integrator_or_2026_increment_certified': False, '_runtime_costs': costs}


def experiment(spec):
    started = time.monotonic(); set_execution_phase('calculation', started)
    raw = []; model_counts = {}; failures = []; events = []; cost = {'calculation_started': started}
    for model, scale, step in product(spec['input']['models'], spec['input']['rate_scales'], spec['input']['steps']):
        for k, values in enumerate(model['initial_states']):
            actual = {key: value for key, value in model.items() if key != 'initial_states'}
            actual['reactions'] = [{**e, 'rate': str(Fraction(e['rate'])*Fraction(scale))} for e in model['reactions']]
            initial = [Fraction(x) for x in values]
            row = {'id': model['id']+'-scale'+scale+'-h'+step+'-x'+str(k),
                   'model_id': model['id'], 'stratum': model['stratum'],
                   'rate_scale': scale, 'step_size': step, 'initial': values,
                   'old_scope': model['old_scope'], 'status': 'pending'}
            try:
                result = evaluate_case(actual, initial, Fraction(step), spec['input']['steps_per_case'],
                                       spec['input']['rational_lower_exponent_cap'], spec['input']['report_claims'], row['id'])
                for key, value in result.pop('_runtime_costs').items():
                    cost[key] = cost.get(key, 0.0)+value
                row.update(result, status='complete')
                if result['euler_has_negative']:
                    events.append(row['id'])
            except Exception as exc:
                row.update(status='inconclusive', error={'class': type(exc).__name__, 'message': str(exc)})
                failures.append(row['id'])
            raw.append(row); record_progress(row)
            model_counts[model['id']] = model_counts.get(model['id'], 0)+1
    valid = not failures and all(x['reaction_expanded_equality'] and x['weighted_conservation']
                                and x['independent_reference']['verified'] for x in raw)
    classification_errors = [x['id'] for x in raw if x['status'] == 'complete'
                             and (not x['report_agreement']
                                  or x['old_coordinate_guard_catches_negative'] != x['separated_guard_catches_negative'])]
    nonlinear_events = [x['id'] for x in raw if x['status'] == 'complete'
                        and x['stratum'] == 'nonlinear_multilinkage' and x['euler_has_negative']]
    successes = valid and not classification_errors and len(raw) == spec['success']['fixtures'] and bool(events) and bool(nonlinear_events)
    summary = {'instances': len(raw), 'models': model_counts, 'inconclusive_cases': failures,
               'judge_valid_all': valid, 'negative_euler_cases': events,
               'nonlinear_multilinkage_negative_cases': nonlinear_events,
               'classification_error_cases': classification_errors,
               'all_exact_judges_and_conservation': True if valid else None,
               'all_old_and_separated_guard_decisions_agree': not classification_errors if valid else None,
               'eventual_numerical_permanence_claims': sum(x.get('eventual_numerical_permanence_certified',False) for x in raw),
               'primary_result': 'inconclusive' if not valid else 'supported' if successes else 'adverse',
               'meets_prediction': bool(successes), 'new_2026_application_gain_demonstrated': False,
               'interpretation': 'Finite synthetic certificate separation only. Honest old coordinate checks suffice; no permanent-region, source-proof, trajectory-accuracy, integrator-speed or deployment claim.'}
    cost['calculation_seconds'] = time.monotonic()-started
    # Existing archive engine stores this separately when explicitly requested;
    # scientific raw/summary contain no measured clocks.
    summary['_runtime_metrics'] = cost
    set_execution_phase('archive', time.monotonic())
    return raw, summary
