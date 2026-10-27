"""Software controls only; never read or run the frozen EXP149 fixture pack."""
import copy
from fractions import Fraction as F
import gzip
import json
from pathlib import Path
import tempfile
import unittest

from ai_value.mass_action_guard import (source_eligible, build_reference, vector_field,
                                        finite_lower, assess_report)
from ai_value.mass_action_reference import expanded_model, evaluate, verify_reference, expected_report


class MassActionSoftwareTests(unittest.TestCase):
    def model(self):
        # UNIT-only weighted exchange, absent from the three target models.
        return {'species': ['X', 'Y'], 'conservation_weights': ['1', '3'],
                'reactions': [{'source': [3, 0], 'target': [0, 1], 'rate': '7/2'},
                              {'source': [0, 1], 'target': [3, 0], 'rate': '2/7'}]}

    def test_forged_conservation_loss_and_boundary_certificates_rejected(self):
        m = self.model(); x = [F(2, 5), F(3, 8)]
        cert = build_reference(m, x)
        self.assertTrue(verify_reference(m, x, cert)['verified'])
        bad = copy.deepcopy(cert); bad['loss'][0] = '-1'
        with self.assertRaises(ValueError): verify_reference(m, x, bad)
        bad = copy.deepcopy(cert); bad['mass'] = '123'
        with self.assertRaises(ValueError): verify_reference(m, x, bad)
        badmodel = copy.deepcopy(m); badmodel['reactions'][0]['target'] = [0, 2]
        with self.assertRaises(ValueError): verify_reference(badmodel, x, cert)

    def test_species_and_reaction_permutations_preserve_independent_polynomial(self):
        m = self.model(); x = [F(2, 5), F(3, 8)]
        grouped, weak = expanded_model(m); self.assertTrue(weak)
        self.assertEqual(vector_field(m, x), evaluate(grouped, x))
        other = copy.deepcopy(m); other['species'].reverse(); other['conservation_weights'].reverse()
        other['reactions'].reverse()
        for e in other['reactions']:e['source'].reverse(); e['target'].reverse()
        grouped2, weak2 = expanded_model(other); self.assertTrue(weak2)
        self.assertEqual(evaluate(grouped2, x[::-1]), evaluate(grouped, x)[::-1])
        self.assertTrue(verify_reference(other, x[::-1], build_reference(other, x[::-1]))['verified'])

    def test_source_and_reference_eligibility_are_distinct(self):
        m = self.model(); x = [F(2, 5), F(3, 8)]
        del m['conservation_weights']; self.assertTrue(source_eligible(m, x))
        with self.assertRaisesRegex(ValueError, 'No independent reference'):
            build_reference(m, x)
        m['reactions'].pop(); self.assertFalse(source_eligible(m, x))
        for modification in ['zero_rate','fractional_exponent','nonpositive_initial','variable_rate']:
            n = self.model(); xx=x[:]
            if modification=='zero_rate':n['reactions'][0]['rate']='0'
            if modification=='fractional_exponent':n['reactions'][0]['source'][0]=1.5
            if modification=='nonpositive_initial':xx[0]=F(0)
            if modification=='variable_rate':n['variable_rates']=True
            with self.assertRaises(ValueError):source_eligible(n,xx)

    def test_finite_nonnegative_and_eventual_claims_cannot_be_conflated(self):
        claims = list(expected_report(True,True,[[F(0),F(1)]]))
        a = assess_report(claims,True,True,[[F(0),F(1)]])
        self.assertEqual(a,expected_report(True,True,[[F(0),F(1)]]))
        self.assertEqual(a['finite_euler_nonnegative'],'supported')
        self.assertEqual(a['finite_euler_positive'],'refuted')
        self.assertEqual(a['conditional_continuous_permanence'],'conditional')
        for k in ['eventual_numerical_permanence','uniform_initial_burnin','arbitrary_step_from_continuous_theorem']:
            self.assertEqual(a[k],'unsupported')
        with self.assertRaises(ValueError):assess_report(['unregistered_claim'],True,True,[[F(1)]])
        b=assess_report(claims,True,True,[[F(-1),F(2)]])
        self.assertEqual(b['finite_euler_nonnegative'],'refuted')

    def test_finite_rational_reference_is_not_time_uniform_and_respects_cap(self):
        cert={'kind':'conservative_loss','loss':['3/2','0']};x=[F(1,7),F(2,9)]
        self.assertEqual(finite_lower(x,cert,F(1,2),4),['1/21','2/9'])
        self.assertEqual(finite_lower(x,cert,F(0),4),['1/7','2/9'])
        with self.assertRaisesRegex(ValueError,'cap'):finite_lower(x,cert,F(4),4)

    def test_logistic_reference_checks_actual_polynomial_and_interval(self):
        model={'species':['X'],'reactions':[
            {'source':[1],'target':[2],'rate':'3/5'},
            {'source':[2],'target':[1],'rate':'7/3'}]}
        initial=[F(7,4)];cert=build_reference(model,initial)
        self.assertEqual(cert['lower'],'9/35')
        self.assertTrue(verify_reference(model,initial,cert)['verified'])
        forged=copy.deepcopy(cert);forged['lower']='1'
        with self.assertRaises(ValueError):verify_reference(model,initial,forged)
        model['reactions'][0]['target']=[3]
        with self.assertRaises(ValueError):verify_reference(model,initial,cert)

    def test_runtime_costs_live_in_manifest_not_deterministic_payload(self):
        from ai_value.experiments import RUNNERS,run
        name='UNIT-RUNTIME-METRICS'
        with tempfile.TemporaryDirectory(prefix='mathweave-unit-cost-') as folder:
            root=Path(folder);(root/'experiments/specs').mkdir(parents=True);(root/'configs').mkdir();(root/'src/ai_value').mkdir(parents=True)
            (root/'configs/research.json').write_text('{}')
            (root/'experiments/specs'/f'{name}.json').write_text(json.dumps({'id':name,'resource_limit_seconds':10,'resource_limit_mb':64,'retain_runtime_metrics':True}))
            RUNNERS[name]=lambda spec:([{'software_only':True}],{'meets_prediction':True,'_runtime_metrics':{'control_clock':0.125}})
            try:
                result=run(root,name);archive=root/'experiments/runs'/result['run_id']
                self.assertEqual(result['stage_runtime_metrics'],{'control_clock':0.125})
                payload=json.loads(gzip.decompress((archive/'summary.json.gz').read_bytes()))
                self.assertNotIn('_runtime_metrics',payload)
            finally:del RUNNERS[name]
