"""Frozen finite GAD receiver audit, not an additivity or hardware test.

The real 2x2 matrix/Kraus path and Decimal population/determinant path are
separate implementations. Only the declared real phase-pair signals are used.
"""
from __future__ import annotations

from decimal import Decimal, localcontext
from fractions import Fraction
import math
import traceback

from .attempts import record_progress


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def transpose(a):
    return [[a[j][i] for j in range(2)] for i in range(2)]


def matrix_sum(matrices):
    return [[sum(m[i][j] for m in matrices) for j in range(2)] for i in range(2)]


class MatrixAudit:
    def __init__(self, tolerance=1e-12):
        self.tolerance = tolerance
        self.clamps = []
        self.states = []

    def endpoint(self, x, low, high, label):
        if not math.isfinite(x):
            raise ArithmeticError(label + ": nonfinite value")
        if low <= x <= high:
            return x
        bound = low if x < low else high
        if abs(x - bound) > self.tolerance:
            raise ArithmeticError(label + ": domain violation " + repr(x))
        self.clamps.append({"object": label, "raw": x, "clipped": bound,
                            "reason": "frozen endpoint allowance"})
        return bound

    def state(self, a, label):
        trace = a[0][0] + a[1][1]
        hermitian = abs(a[0][1] - a[1][0])
        if abs(trace - 1) > self.tolerance or hermitian > self.tolerance:
            raise ArithmeticError(label + ": trace/Hermiticity violation")
        discriminant = (a[0][0] - a[1][1]) ** 2 + 4 * a[0][1] * a[1][0]
        # State eigenvalues lie in [0,1], so their squared difference does too.
        disc = self.endpoint(discriminant, 0.0, 1.0, label + ".discriminant")
        eigen_raw = [(trace - math.sqrt(disc)) / 2, (trace + math.sqrt(disc)) / 2]
        eigen = [self.endpoint(v, 0.0, 1.0, label + ".lambda" + str(i))
                 for i, v in enumerate(eigen_raw)]
        nats = -sum(v * math.log(v) for v in eigen if v > 0)
        result = {"object": label, "matrix": a, "trace": trace,
                  "hermiticity_residual": hermitian, "discriminant_raw": discriminant,
                  "eigenvalues_raw": eigen_raw, "eigenvalues_used": eigen,
                  "entropy_nats": nats, "entropy_bits": nats / math.log(2)}
        self.states.append(result)
        return result


def matrix_oracle(gamma, nu, p):
    audit = MatrixAudit()
    kraus = [[[math.sqrt(1-nu), 0.0], [0.0, math.sqrt(1-nu)*math.sqrt(1-gamma)]],
             [[0.0, math.sqrt(gamma*(1-nu))], [0.0, 0.0]],
             [[math.sqrt(nu)*math.sqrt(1-gamma), 0.0], [0.0, math.sqrt(nu)]],
             [[0.0, 0.0], [math.sqrt(gamma*nu), 0.0]]]
    complete = matrix_sum([mm(transpose(k), k) for k in kraus])
    residual = max(abs(complete[i][j] - int(i == j)) for i in range(2) for j in range(2))
    if residual > audit.tolerance:
        raise ArithmeticError("Kraus completeness violation")
    outputs = []
    for index, sign in enumerate([1, -1]):
        vector = [math.sqrt(1-p), sign * math.sqrt(p)]
        rho = [[vector[i]*vector[j] for j in range(2)] for i in range(2)]
        audit.state(rho, "input" + str(index))
        out = matrix_sum([mm(mm(k, rho), transpose(k)) for k in kraus])
        outputs.append(out)
    entropies = [audit.state(a, "output" + str(i))["entropy_bits"] for i, a in enumerate(outputs)]
    average = [[sum(a[i][j] for a in outputs) / 2 for j in range(2)] for i in range(2)]
    quantum = audit.state(average, "average")["entropy_bits"] - sum(entropies) / 2
    projectors = [[[0.5, 0.5*s], [0.5*s, 0.5]] for s in [1, -1]]
    probabilities_raw = [[sum(mm(e, a)[i][i] for i in range(2)) for e in projectors] for a in outputs]
    probabilities = [[audit.endpoint(v, 0.0, 1.0, "Pr(%s,%s)" % (x,y))
                      for y,v in enumerate(row)] for x,row in enumerate(probabilities_raw)]
    row_residual = max(abs(sum(row)-1) for row in probabilities_raw)
    joint = [[v/2 for v in row] for row in probabilities]
    total_residual = abs(sum(map(sum, joint))-1)
    if max(row_residual, total_residual) > audit.tolerance:
        raise ArithmeticError("Measurement normalization violation")
    px = [sum(row) for row in joint]
    py = [sum(row[y] for row in joint) for y in range(2)]
    classical = sum(joint[x][y] * math.log(joint[x][y]/(px[x]*py[y]), 2)
                    for x in range(2) for y in range(2) if joint[x][y] > 0)
    return {"holevo_bits": quantum, "fixed_x_mi_bits": classical, "gap_bits": quantum-classical,
            "kraus": kraus, "kraus_completeness_matrix": complete, "kraus_completeness_residual": residual,
            "states": audit.states, "probabilities_raw": probabilities_raw, "probabilities_used": probabilities,
            "joint": joint, "measurement_normalization_residual": max(row_residual, total_residual),
            "clamps": audit.clamps}


def decimal_input(value):
    if isinstance(value, Decimal):
        return value
    f = Fraction(value)
    return Decimal(f.numerator) / Decimal(f.denominator)


def scalar_oracle(gamma, nu, p, precision):
    # No matrix-state construction, matrix eigensolver or matrix clipping here.
    with localcontext() as ctx:
        ctx.prec = precision
        g,n,p = [decimal_input(v) for v in (gamma,nu,p)]
        zero,one = Decimal(0),Decimal(1)
        clamps = []
        def bound(x, lower, upper, label):
            if not x.is_finite():
                raise ArithmeticError(label + ": nonfinite Decimal")
            if lower <= x <= upper:
                return x
            nearest = lower if x < lower else upper
            if abs(x-nearest) > Decimal("1e-60"):
                raise ArithmeticError(label + ": Decimal domain violation " + str(x))
            clamps.append({"object": label, "raw": str(x), "clipped": str(nearest)})
            return nearest
        def h2(x):
            x = bound(x, zero, one, "entropy_probability")
            y = bound(one-x, zero, one, "entropy_complement")
            return -sum(t*t.ln() for t in [x,y] if t) / Decimal(2).ln()
        t = bound((one-g)*p+g*n, zero, one, "population")
        v = bound(g*n*(one-n)+g*(one-g)*(p-n)**2, zero, Decimal("0.25"), "determinant")
        rad = bound(one-4*v, zero, one, "spectrum_discriminant")
        eigen = (one+rad.sqrt())/2
        quantum = h2(t)-h2(eigen)
        coherence_squared = bound((one-g)*p*(one-p), zero, Decimal("0.25"), "coherence_squared")
        crossover = bound(Decimal("0.5")-coherence_squared.sqrt(), zero, one, "crossover")
        classical = one-h2(crossover)
        return {"holevo_bits": quantum, "fixed_x_mi_bits": classical, "gap_bits": quantum-classical,
                "population": t, "determinant": v, "large_eigenvalue": eigen,
                "crossover": crossover, "clamps": clamps}


def scalar_strings(values):
    return {k: str(v) if isinstance(v, Decimal) else v for k,v in values.items()}


def h2_float(x):
    return -sum(t*math.log(t,2) for t in [x,1-x] if t > 0)


def golden(objective, number, sqrt):
    a,b = number(0),number(1)
    ratio = (sqrt(number(5))-number(1))/number(2)
    c,d = b-ratio*(b-a),a+ratio*(b-a)
    fc,fd = objective(c),objective(d)
    for _ in range(96):
        if fc >= fd:
            b,d,fd = d,c,fc
            c = b-ratio*(b-a)
            fc = objective(c)
        else:
            a,c,fc = c,d,fd
            d = a+ratio*(b-a)
            fd = objective(d)
    candidates = [number(0),number(1),a,b,c,d,(a+b)/number(2)]
    scored = [(objective(x),x) for x in candidates]
    value,p = max(scored, key=lambda row: (row[0],-row[1]))
    return {"p": p, "value_bits": value, "iterations": 96,
            "candidates": [{"p": str(x), "value_bits": str(y)} for y,x in scored]}


def optimization(gamma,nu):
    g,n = float(Fraction(gamma)),float(Fraction(nu))
    audit = MatrixAudit()
    def objective(p):
        v = audit.endpoint(g*n*(1-n)+g*(1-g)*(p-n)**2,0.0,0.25,"optimizer.v")
        rad = audit.endpoint(1-4*v,0.0,1.0,"optimizer.radicand")
        t = audit.endpoint((1-g)*p+g*n,0.0,1.0,"optimizer.population")
        return h2_float(t)-h2_float((1+math.sqrt(rad))/2)
    searches = {"float": golden(objective,float,math.sqrt)}
    for precision in [70,100]:
        with localcontext() as ctx:
            ctx.prec = precision
            searches[str(precision)] = golden(
                lambda p: scalar_oracle(gamma,nu,p,precision)["holevo_bits"], Decimal, Decimal.sqrt)
    outputs = {}
    for name, search in searches.items():
        m = matrix_oracle(g,n,float(search["p"]))
        outputs[name] = {"p": str(search["p"]), "value_bits": str(search["value_bits"]),
                         "iterations": search["iterations"], "candidates": search["candidates"],
                         "matrix_at_candidate": m,
                         "matrix_scalar_residual": abs(m["holevo_bits"]-float(search["value_bits"]))}
    vals = [float(v["value_bits"]) for v in outputs.values()]
    return {"searches": outputs, "objective_disagreement": max(vals)-min(vals), "float_clamps": audit.clamps}


def experiment(spec):
    rows = []
    errors = []
    for index, fixture in enumerate(spec["input"]["fixtures"]):
        row = {"kind": "fixture", "index": index, **fixture}
        try:
            g,n,p = [float(Fraction(fixture[k])) for k in ["gamma","nu","p"]]
            m = matrix_oracle(g,n,p)
            dec = [scalar_oracle(fixture["gamma"],fixture["nu"],fixture["p"],pr) for pr in [70,100]]
            matrix_scalar = max(abs(m[k]-float(d[k])) for d in dec
                                for k in ["holevo_bits","fixed_x_mi_bits","gap_bits"])
            with localcontext() as ctx:
                ctx.prec = 110
                precision_delta = max(abs(dec[0][k]-dec[1][k]) for k in
                                      ["holevo_bits","fixed_x_mi_bits","gap_bits"])
                threshold = Decimal(spec["threshold_classification"]["threshold_bits"])
                margin = Decimal(spec["threshold_classification"]["arithmetic_safety_margin_bits"])
                gaps = [Decimal(str(m["gap_bits"])),dec[0]["gap_bits"],dec[1]["gap_bits"]]
                uncertain = any(abs(v-threshold)<=margin for v in gaps)
                exceeds = all(v>threshold+margin for v in gaps)
            crossover = float(dec[1]["crossover"])
            expected = [[1-crossover,crossover],[crossover,1-crossover]]
            probability_delta = max(abs(m["probabilities_raw"][x][y]-expected[x][y])
                                    for x in range(2) for y in range(2))
            point_ok = (matrix_scalar<=float(spec["success"]["matrix_scalar_absolute_disagreement_max"])
                        and probability_delta<=float(spec["success"]["matrix_receiver_probability_disagreement_max"])
                        and precision_delta<=Decimal(spec["success"]["decimal70_100_absolute_disagreement_max"]))
            row.update(matrix=m, decimal70=scalar_strings(dec[0]),decimal100=scalar_strings(dec[1]),
                       matrix_scalar_residual=matrix_scalar,probability_residual=probability_delta,
                       decimal_precision_residual=str(precision_delta),point_checks_pass=point_ok,
                       threshold_uncertain=uncertain,
                       eligible_interior_exceedance=fixture["stratum"]=="interior" and exceeds and point_ok)
        except Exception:
            row["error"] = traceback.format_exc()
            errors.append({"kind":"fixture","index":index,"error":row["error"]})
        rows.append(row)
        record_progress(row)
    fixtures = [v for v in rows if v["kind"]=="fixture" and "error" not in v]
    lookup = {(v["gamma"],v["nu"],v["p"]):v for v in fixtures}
    control_residuals = []
    for row in fixtures:
        g,n,p = [Fraction(row[k]) for k in ["gamma","nu","p"]]
        q,mi = row["matrix"]["holevo_bits"],row["matrix"]["fixed_x_mi_bits"]
        residuals = {"holevo_dominance": max(0.0,mi-q)}
        if g==1 or p in [0,1]:
            residuals["zero_information"] = max(abs(q),abs(mi))
        if g==0:
            residuals["identity_same_encoder"] = abs(q-h2_float(float(p)))
        if n==Fraction(1,2) and p==Fraction(1,2):
            value = 1-h2_float((1-math.sqrt(1-float(g)))/2)
            residuals["unital_matched"] = max(abs(q-value),abs(mi-value))
        other = lookup.get((str(g),str(1-n),str(1-p)))
        if other is None:
            residuals["reflection"] = 1.0
        else:
            residuals["reflection"] = max(abs(q-other["matrix"]["holevo_bits"]),
                                           abs(mi-other["matrix"]["fixed_x_mi_bits"]))
        control_residuals.append({"index":row["index"],"residuals":residuals})
    for gamma in spec["input"]["grid"]:
        for nu in spec["input"]["grid"]:
            row = {"kind":"optimizer","gamma":gamma,"nu":nu}
            try:
                result = optimization(gamma,nu)
                best_grid = max(v["matrix"]["holevo_bits"] for v in fixtures
                                if v["gamma"]==gamma and v["nu"]==nu)
                result["below_frozen_grid_residual"] = max(0.0,best_grid-min(
                    float(v["value_bits"]) for v in result["searches"].values()))
                row.update(result)
            except Exception:
                row["error"] = traceback.format_exc()
                errors.append({"kind":"optimizer","gamma":gamma,"nu":nu,"error":row["error"]})
            rows.append(row)
            record_progress(row)
    opts = [v for v in rows if v["kind"]=="optimizer" and "error" not in v]
    max_control = max((v for row in control_residuals for v in row["residuals"].values()),default=1.0)
    max_opt = max([v["objective_disagreement"] for v in opts] +
                  [v["below_frozen_grid_residual"] for v in opts] +
                  [s["matrix_scalar_residual"] for v in opts for s in v["searches"].values()],default=1.0)
    opt_by_pair = {(v["gamma"],v["nu"]):v for v in opts}
    # Explicitly keep the original optimized naive label separate from SAME-p.
    labels = []
    for row in fixtures:
        opt = opt_by_pair.get((row["gamma"],row["nu"]))
        if opt is not None:
            labels.append({"index":row["index"],"same_encoder_naive_bits":row["matrix"]["holevo_bits"],
                           "honest_old_fixed_receiver_bits":row["matrix"]["fixed_x_mi_bits"],
                           "separate_approx_optimized_naive_bits":opt["searches"]["100"]["value_bits"],
                           "optimized_label_is_not_same_encoder_or_certified_capacity":True})
    exceed = [v["index"] for v in fixtures if v["eligible_interior_exceedance"]]
    summary = {"instances":len(fixtures),"interior_cases":sum(v["stratum"]=="interior" for v in fixtures),
               "optimizer_pairs":len(opts),"errors":errors,"control_residuals":control_residuals,
               "max_control_residual":max_control,"max_optimizer_residual":max_opt,
               "interior_gap_exceedance_indices":exceed,"threshold_uncertain_indices":[v["index"] for v in fixtures if v["threshold_uncertain"]],
               "maximum_same_encoder_gap_bits":max((v["matrix"]["gap_bits"] for v in fixtures),default=None),
               "max_matrix_scalar_residual":max((v["matrix_scalar_residual"] for v in fixtures),default=None),
               "max_probability_residual":max((v["probability_residual"] for v in fixtures),default=None),
               "naive_and_honest_old_labels":labels,
               "new_2026_computational_gain_established":False,
               "interpretation":"Finite synthetic fixed-X receiver calibration;honest old probabilities already suffice. Not hardware, optimal individual POVM, finite code or additivity proof."}
    summary["meets_prediction"] = (not errors and len(fixtures)==125 and len(opts)==25 and
        summary["interior_cases"]==27 and len(exceed)>=spec["success"]["interior_gap_exceedances_min"] and
        all(v["point_checks_pass"] for v in fixtures) and
        max_control<=float(spec["success"]["control_absolute_residual_max"]) and
        max_opt<=float(spec["success"]["optimization_objective_disagreement_max"]))
    record_progress({"kind":"summary","summary":summary})
    return rows,summary
