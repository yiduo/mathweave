# APP-337-01 — pre-target static review packet v1

Status: proposed conditional far-transfer candidate, not yet registered as a canonical connection. No target function, gradient or benchmark output has been observed. This packet follows actual source-code inspection, so its algebraic and backend predictions are explicitly nonblind. It does not claim a novel activation, calculus result, software defect, training improvement or 2026 algorithmic advantage.

## Source and proposed target

Pinned OpenAI/math revision: `1581d4cbdd69a0faf34b2089614fe2a814316a6a`. F337 second manuscript `Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026/build/sections/06-chords.tex`, lemma `lem:chord-tests` and its proof, especially lines100–123. The proof uses actual two-variable C1 composites through zeros instead of assuming a fractional intermediate is C1 or Sobolev. See `data/provenance/readings/F-337.json` and `PART-337-C1-ZERO-COMPOSITE` for scope. This scalar calculus fragment can be studied independently; the full Sobolev membership and weighted chord inequalities still require the hypothetical extremizer and normalized critical PDE minimizer. None of those geometric inequalities is claimed for machine-learning data.

Proposed target: implementation-admission audit for scalar radial features with exact zero gates in a real reverse-mode AD backend. The inputs are explicitly synthetic. Exact zeros are deliberate boundary cases, not representative prevalence measurements. No real network, customer bug, application deployment or data distribution is asserted.

For integer n>2, beta=1/(n-2), a=kappa=1, and r>=0:

`F(r,z)=z*(1+r*r*z**(2*beta))**(-1/(2*beta))` for z>=0; extend F(r,z)=z for z<0.

This is source F_1, not a new function. It is jointly C1 at z=0; derivative with respect to z is1 and with respect to r is0 there. For z>0, set y=r*r*z**(2*beta):

`dz=(1+y)**(-1/(2*beta)-1)`

`dr=-(r/beta)*z**(1+2*beta)*(1+y)**(-1/(2*beta)-1)`.

For z<0, dz=1 and dr=0. These formulae are pre-target algebraic predictions, not numerical observations or proof audit.

## Actual backend and inspected primitives

Autograd1.9.1, official PyPI wheel `autograd-1.9.1-py3-none-any.whl`, 54,387bytes, SHA256 `b788bae3fa010cbffb4cfb7b8ba2a3f0daa6072a8506da6164c779fe9cf3e05a`; MIT. Official metadata requires Python>=3.10 and NumPy<3; SciPy is optional and will not be installed. Existing runtime Python3.12.14 and NumPy2.3.5. Wheel has been downloaded and statically inspected, not imported or installed. New metadata+wheel acquisition is62,681bytes, below1MiB cap.

Actual wheel `autograd/numpy/numpy_vjps.py` lines139–143 defines the base-power VJP using upstream gradient times exponent times base to the shifted exponent; the base gradient is not uniformly masked at base0 for fractional positive exponents. Lines225–230 define where routing. Lines12–68 register comparisons as nondifferentiated tracing primitives. `numpy_boxes.py` lines69–73 routes Python multiplication/power to these primitives; lines117–127 routes comparisons. `core.py` lines10–32 traces and applies the reverse graph. These are selected actual source scopes, not backend execution. Do not infer an implementation defect: differentiation of a nonsmooth intermediate is outside the primitive's smooth contract, even if the total mathematical composite has a derivative.

## Proposed frozen inputs, implementations and judges

Cartesian grid n=[3,4,5,6,8,12], r=[0,1/4,1,4], z=[-1,-1/8,0,2^-80,2^-40,1/8,1,2], giving192fixtures. Inputs use rational strings; order fixed lexicographically by these lists. No random draws, tuning, holdout or real-data prevalence claim. n=3,4 are nonsingular intermediate-power controls; n>=5 have a fractional exponent2beta<1. All r=0 cases, negative extension, zero and tiny positive values remain in the output.

Compare:

1. Naive factored actual-AD implementation: Python `if z<0: return z`, otherwise evaluate the full displayed fractional formula, including at z=0. Use actual Autograd differentiation separately in r and z.
2. Strong old baseline: Python `if z<=0: return z` before any fractional-power operation, otherwise the same expression, differentiated by the same backend. This is ordinary correct pre-operation branching, not a newly invented method. Its mathematical first derivative is valid at the C1 join. No finite epsilon replacement of zero, post-result NaN suppression or hand-written fake AD.
3. Independent old analytic reference evaluated with Decimal80 and Decimal120 precision via logarithm/exponential, recording precision sensitivity. For z=0/negative use exact rational derivatives. Also evaluate centered finite differences of F using a separately written high-precision value path at Decimal180, absolute h=10^-100 for z derivatives and r derivatives; retain the degenerate r=0 cases. This is a numerical cross-check, not a rigorous interval proof. Review whether this proposed h/precision rule is sufficient and whether tolerances are consistent before freezing implementation.

Proposed numerical tolerances: relative-plus-absolute `1e-10*(1+abs(reference))` for float values/first derivatives; Decimal80/120 derivative agreement `1e-60*(1+abs(reference))`; high-precision finite-difference agreement `1e-12*(1+abs(reference))`. Any unresolved judge disagreement makes the relevant conclusion inconclusive, not silently discarded or repaired using target outputs. Values and both gradient components must be preserved for every fixture. NaN/infinity are represented explicitly as classifications in standards-compliant JSON; warnings and exceptions are recorded with fixture, method and component.

Proposed primary prediction: at least one n>=5,z=0 naive dF/dz is nonfinite or outside tolerance, while the old pre-operation-branch implementation is finite and within tolerance for all192fixtures in both derivative components. All forward values agree with the independent reference. Naive negative-extension and n=3,4 controls should be finite and within tolerance. Record unexpected naive failures separately; do not assert all fractional cases fail or count failures as independent hypotheses.

Proposed limits:60seconds for target calculation,64MiB peak Python allocation,128MiB process RSS; separately measure import/setup, calculation and compression times and full process RSS. No training stack, new dataset or large dependency. All input/specification/source/runtime/wheel hashes, raw outcomes, warning/error records and summary must be archived compressed with verified roundtrip hashes. Freeze executable specification and implementation commit before any target numerical output. Failed executions remain archived.

## Interpretation and null

Even if the primary prediction is supported, the result is a bounded implementation-consistency calibration. The correct old branch is expected to solve it. No incremental numerical or application value of the2026 theorem is established by this comparison. The library power VJP is not alleged to violate its own smooth-domain contract. If all naive cases are fine, retain that adverse observation against the prediction; if judges disagree or limits fail, retain inconclusive/resource failure. Do not add a new application check until complete card fields, actual external test and reproducibility evidence exist. Full theory chains remain unknown, source scalar fragment C; no human/provider acceptance.

## Review request

Independently inspect this same packet and the cited actual local source files. Do not run/import Autograd, evaluate target numerical fixtures or contact another reviewer. Record strongest objections or support, exact algebra/zero-extension checks, fixture fairness, strong-old-baseline adequacy, derivative-judge independence, tolerances, resource/storage and interpretation limits. Identify required pre-target changes rather than pretending consensus approval. Exact selected backend model is unknown; this is an isolated same-OpenAI-provider auxiliary opinion, not human review or independent second-provider evidence.
