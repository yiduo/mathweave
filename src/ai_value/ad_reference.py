"""Two scalar numerical reference paths; neither calls an AD derivative.

Decimal precision sensitivity is not an independent judge. The literal-value
finite differences provide a second calculation route, sharing Decimal and the
interpretation of the function; none of these checks is interval arithmetic.
"""
from decimal import Decimal, ROUND_HALF_EVEN, localcontext
from fractions import Fraction


def analytic(n, r_text, z_text, precision):
    with localcontext() as ctx:
        ctx.prec = precision
        ctx.rounding = ROUND_HALF_EVEN
        rf, zf = Fraction(r_text), Fraction(z_text)
        r = Decimal(rf.numerator) / Decimal(rf.denominator)
        z = Decimal(zf.numerator) / Decimal(zf.denominator)
        if z <= 0:
            return {"value": str(z), "dr": "0", "dz": "1"}
        q = Decimal(2) / Decimal(n - 2)
        c = -Decimal(n - 2) / Decimal(2)
        y = r * r * (q * z.ln()).exp()
        base_log = (1 + y).ln()
        common = ((c - 1) * base_log).exp()
        return {"value": str(z * (c * base_log).exp()),
                "dr": str(-Decimal(n - 2) * r * ((1 + q) * z.ln()).exp() * common),
                "dz": str(common)}


def literal_value(n, r, z):
    """Caller supplies its own Decimal context; even real-r extension."""
    if z <= 0:
        return z
    u = (z.ln() / Decimal(n - 2)).exp()
    t = r * u
    w = (-Decimal(n - 2) / Decimal(2) * (1 + t * t).ln()).exp()
    return z * w


def finite_differences(n, r_text, z_text, step, precision):
    # Deliberately parse again, rather than reusing analytic intermediates.
    with localcontext() as ctx:
        ctx.prec = precision
        ctx.rounding = ROUND_HALF_EVEN
        r_num = Fraction(r_text)
        z_num = Fraction(z_text)
        r = Decimal(r_num.numerator) / Decimal(r_num.denominator)
        z = Decimal(z_num.numerator) / Decimal(z_num.denominator)
        h = Decimal(step)
        dr = (literal_value(n, r + h, z) - literal_value(n, r - h, z)) / (2 * h)
        dz = (literal_value(n, r, z + h) - literal_value(n, r, z - h)) / (2 * h)
        return {"dr": str(dr), "dz": str(dz)}


def residual(observed, reference):
    with localcontext() as ctx:
        ctx.prec = 180
        a, b = Decimal(str(observed)), Decimal(str(reference))
        if not a.is_finite() or not b.is_finite():
            return {"absolute": None, "relative": None, "finite": False}
        error = abs(a - b)
        return {"absolute": str(error), "relative": str(error / abs(b)) if b else None,
                "finite": True}


def agrees(observed, reference, tolerance):
    with localcontext() as ctx:
        ctx.prec = 180
        a, b = Decimal(str(observed)), Decimal(str(reference))
        return (a.is_finite() and b.is_finite()
                and abs(a - b) <= Decimal(tolerance) * (1 + abs(b)))


def judge_valid(reference_low, reference_high, differences, tolerances):
    checks = {"precision_" + k: agrees(reference_low[k], reference_high[k], tolerances["precision"])
              for k in ("value", "dr", "dz")}
    for i, difference in enumerate(differences):
        for k in ("dr", "dz"):
            checks["difference_%s_%s" % (i, k)] = agrees(
                difference[k], reference_high[k], tolerances["difference"])
    for k in ("dr", "dz"):
        checks["step_sensitivity_" + k] = agrees(
            differences[0][k], differences[1][k], tolerances["step_sensitivity"])
    return checks
