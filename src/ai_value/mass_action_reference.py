"""Independent expanded-polynomial oracle for finite mass-action checks.

No permanence theorem is proved or numerically certified here. All arithmetic
is rational; the nonlinear finite-time reference is an elementary loss bound.
"""
from __future__ import annotations

from fractions import Fraction


def expanded_model(model):
    d = len(model['species'])
    if d < 1 or len(set(model['species'])) != d:
        raise ValueError('Invalid species')
    coefficients = {}
    complexes = set()
    arcs = []
    for reaction in model['reactions']:
        a, b = tuple(reaction['source']), tuple(reaction['target'])
        if (len(a) != d or len(b) != d or any(type(n) is not int or n < 0 for n in a+b)
                or a == b or model.get('variable_rates', False)):
            raise ValueError('Unsupported source model')
        rate = Fraction(reaction['rate'])
        if rate <= 0:
            raise ValueError('Nonpositive rate')
        complexes.update([a, b]); arcs.append((a, b))
        vector = coefficients.setdefault(a, [Fraction(0) for _ in range(d)])
        for i in range(d):
            vector[i] += rate * (b[i] - a[i])
    names = sorted(complexes)
    index = {a: i for i, a in enumerate(names)}
    reach = [[i == j for j in range(len(names))] for i in range(len(names))]
    for a, b in arcs:
        reach[index[a]][index[b]] = True
    for k in range(len(names)):
        for i in range(len(names)):
            for j in range(len(names)):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    weak = all(reach[index[b]][index[a]] for a, b in arcs)
    return coefficients, weak


def evaluate(coefficients, state):
    """Evaluate a grouped polynomial, independently of reaction accumulation."""
    result = [Fraction(0) for _ in state]
    for exponent, vector in sorted(coefficients.items()):
        monomial = Fraction(1)
        for value, power in zip(state, exponent):
            monomial *= value ** power
        for i, coefficient in enumerate(vector):
            result[i] += coefficient * monomial
    return result


def expected_report(independent_weak, verified, old_trace):
    """Fixed report oracle: finite observations never supply eventual bounds."""
    return {
        'conditional_continuous_permanence': 'conditional' if independent_weak else 'unsupported',
        'finite_continuous_positive': 'supported' if verified else 'unsupported',
        'finite_euler_nonnegative': 'supported' if all(x >= 0 for row in old_trace for x in row) else 'refuted',
        'finite_euler_positive': 'supported' if all(x > 0 for row in old_trace for x in row) else 'refuted',
        'eventual_numerical_permanence': 'unsupported',
        'uniform_initial_burnin': 'unsupported',
        'arbitrary_step_from_continuous_theorem': 'unsupported',
    }


def verify_reference(model, initial, certificate):
    """Check the entire supplied model and a conservative/logistic certificate.

    Conservative verification combines net coefficients before deriving loss
    constants. The producer instead bounds each reaction channel separately.
    """
    coefficients, weak = expanded_model(model)
    if len(initial) != len(model['species']) or any(x <= 0 for x in initial):
        raise ValueError('Invalid initial state')
    if not weak:
        raise ValueError('Outside source weak reversibility')
    if certificate['kind'] == 'conservative_loss':
        weights = [Fraction(x) for x in model['conservation_weights']]
        if len(weights) != len(initial) or any(x <= 0 for x in weights):
            raise ValueError('Invalid positive conservation vector')
        mass = sum(a*b for a, b in zip(weights, initial))
        bounds = [mass/x for x in weights]
        if Fraction(certificate['mass']) != mass:
            raise ValueError('Wrong mass')
        if [Fraction(x) for x in certificate['upper']] != bounds:
            raise ValueError('Wrong upper bounds')
        if len(certificate['loss']) != len(initial):
            raise ValueError('Wrong loss dimension')
        required = [Fraction(0) for _ in initial]
        for exponent, vector in coefficients.items():
            if sum(a*b for a, b in zip(weights, vector)) != 0:
                raise ValueError('Polynomial does not conserve supplied mass')
            for i, coefficient in enumerate(vector):
                if coefficient >= 0:
                    continue
                if exponent[i] == 0:
                    raise ValueError('Negative boundary coefficient')
                bound = -coefficient
                for j, (upper, power) in enumerate(zip(bounds, exponent)):
                    bound *= upper ** (power-(i == j))
                required[i] += bound
        offered = [Fraction(x) for x in certificate['loss']]
        if any(a < b for a, b in zip(offered, required)):
            raise ValueError('Understated finite-time loss bound')
        return {'verified': True, 'kind': 'conservative_loss',
                'independent_loss': [str(x) for x in required],
                'finite_time_only': True, 'eventual_uniform_bound_certified': False}
    if certificate['kind'] == 'logistic_interval':
        if len(initial) != 1 or set(coefficients) != {(1,), (2,)}:
            raise ValueError('Not the stated scalar logistic polynomial')
        a, b = coefficients[(1,)][0], -coefficients[(2,)][0]
        if a <= 0 or b <= 0:
            raise ValueError('Invalid logistic signs')
        equilibrium = a/b
        lo, hi = min(initial[0], equilibrium), max(initial[0], equilibrium)
        if Fraction(certificate['lower']) != lo or Fraction(certificate['upper'][0]) != hi:
            raise ValueError('Wrong logistic interval')
        return {'verified': True, 'kind': 'logistic_interval',
                'equilibrium': str(equilibrium), 'finite_time_only': True,
                'eventual_uniform_bound_certified': False}
    raise ValueError('Unsupported reference kind')
