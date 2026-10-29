# F271九月基础稿：34个来源命题的条件与依赖

由规范图谱导出。仅此一稿的来源命题已整理，四稿整族与历史闭包仍未完成。来源主端点B、其余33项C，全部完整依赖链未知；没有本地Lean／Comparator或真人审核。存在有序KMS态不等于有限零场Gibbs均值为正，更不等于Bloch系数或球面律已验证。

## CLM-271-F-THM-MAIN — 低温有序KMS态存在

来源等级：B；完整链：未知。

陈述：For each integer d>=3 and each positive half-integer S there is finite beta0(d,S)>0; for every finite beta>=beta0 a translation-invariant beta-KMS state has omega(Sz_0)>=S/4.

条件与限制：Nearest-neighbor coupling-one isotropic Heisenberg model on Zd; existential threshold, fixed d,S. A selected state, not the finite zero-field Gibbs mean, rotational average, Bloch coefficient or effective critical temperature.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/00-introduction.tex；thm:main; statement lines [64, 73]。

## CLM-271-F-LEM-SLOT-REALIZATION — 对称槽实现

来源等级：C；完整链：未知。

陈述：ell=2S spin-one-half slots restricted to the site-symmetric subspace realize spin S; full Hamiltonian and magnetization commute with the symmetrizer, with Hhat=-sum U_edge/2+qLambda I/4.

条件与限制：All ell squared slot pairs per site bond and unordered edges once. Individual edge transpositions need not preserve the symmetric subspace; do not interchange compression and arbitrary products.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/01-loops.tex；lem:slot-realization; statement lines [42, 70]。

## CLM-271-F-PROP-SPIN-LOOPS — 精确自旋交换表示

来源等级：C；完整链：未知。

陈述：Finite-cube partition function equals exp(beta qLambda/4) times the base expectation of 2^cycle_count; magnetization spectral observables follow fair independent cycle colors conditional on the weighted picture.

条件与限制：Finite cube, positive finite beta, physical spin spectrum. Color independence is conditional on the picture; the picture itself is cycle weighted. qLambda is the slot-edge count, not the number of physical bonds.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/01-loops.tex；prop:spin-loops; statement lines [132, 155]。

## CLM-271-F-LEM-DENSE-PINS — 稠密边界钉极限

来源等级：C；完整链：未知。

陈述：Increasing finite dense boundary cuts eventually give the same pin weights and missing-cycle union per sampled finite picture; the normalized laws converge in total variation and bounded convergent observables converge.

条件与限制：Fixed finite cube and beta, deterministic finite extra pins, grid contains zero. The eventual index is picture dependent and the domination bound is not uniform in volume.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/01-loops.tex；lem:dense-pins; statement lines [252, 273]。

## CLM-271-F-LEM-FACTORIAL — 无条件钉律阶乘支配

来源等级：C；完整链：未知。

陈述：Under the normalized pin law, ordered distinct actual marks have factorial measure at most 2^n times the base Poisson product intensity, also with fixed time order or interval.

条件与限制：Finite deterministic pins with optional dense boundary D0. This is an unconditional estimate under the pin law; it is not fresh-clock domination after fixing an exposure.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/01-loops.tex；lem:factorial; statement lines [319, 331]。

## CLM-271-F-PROP-PIN-TEST — 同时钉测试

来源等级：C；完整链：未知。

陈述：For nonempty single-time T disjoint from E, the missing-cycle event under E has probability <=(2r)^|T|, with r defined by the positive-time next-pin return fraction under P=E union T.

条件与限制：Finite volume, any beta>0, finite E optionally united with D0. The law for r has more pins; replacing it with the smaller-pin law would change the input.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/02-pin-test.tex；prop:pin-test; statement lines [22, 30]。

## CLM-271-F-LEM-PIN-STABILITY-CLOSURE — 稳定多项式闭包

来源等级：C；完整链：未知。

陈述：Bounded-degree coefficientwise limits, real specialization and differentiation preserve stability up to zero; variable identification and the stated identify/extract operation preserve stability up to zero.

条件与限制：Fixed finite variable set and common degree bound for limits. Nonzero must be checked separately where a probability polynomial is normalized.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/02-pin-test.tex；lem:pin-stability-closure; statement lines [69, 77]。

## CLM-271-F-LEM-PIN-PARTIAL-SYMMETRIZATION — 部分对称化

来源等级：C；完整链：未知。

陈述：A convex mixture (1-u)F+u tau F remains stable and multiaffine for a stable multiaffine F, a variable transposition tau and u in [0,1].

条件与限制：Specific multiaffine class and transposition mixture; not arbitrary convex combinations of stable polynomials or arbitrary conditioning.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/02-pin-test.tex；lem:pin-partial-symmetrization; statement lines [123, 127]。

## CLM-271-F-LEM-PIN-EXCHANGE-SYMBOL — 交换符号稳定性

来源等级：C；完整链：未知。

陈述：The expected permutation symbol is stable for independent Bernoulli transposition products and deterministic permutations, and their finite-set distributional limits; independent Poisson and uniform-subset permutation layers admit such limits.

条件与限制：Layers are ordered, not assumed commuting. This concerns the unconditioned base permutation law; all-hit conditioning is a later step.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/02-pin-test.tex；lem:pin-exchange-symbol; statement lines [172, 182]。

## CLM-271-F-LEM-PIN-SPLICING — 删除非钉与输出抽取

来源等级：C；完整链：未知。

陈述：Identifying a nonpin input/output variable and extracting its linear coefficient produces the nonzero stable pin symbol weighted by 2^missing_cycles; differentiation and zero specialization yield the generating polynomial of sigma(T).

条件与限制：Layered finite source symbol, fixed pins P and T subset P, positive normalizer ZP. A deleted fixed point contributes factor two. Do not omit the cycle weight.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/02-pin-test.tex；lem:pin-splicing; statement lines [254, 275]。

## CLM-271-F-LEM-PIN-PRESENCE — 同时出现概率

来源等级：C；完整链：未知。

陈述：For a finite random subset with stable generating polynomial, Pr(J subset A)<=product_j Pr(j in A), also after positive-probability presence conditioning on disjoint remaining coordinates.

条件与限制：The conditioning is presence of B subset A, not arbitrary exposed trajectories. Pairwise covariance alone is not the stated all-subset input.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/02-pin-test.tex；lem:pin-presence; statement lines [316, 325]。

## CLM-271-F-PROP-EXPOSURE — 暴露路径分解

来源等级：C；完整链：未知。

陈述：Under PP, the unexposed law at almost every exposure a is fresh Qa conditioned on all cycles hitting P; gP=Qa(all-hit)>0 almost surely under the actual exposure marginal. That marginal is proportional to 1_FA 2^cA gP muA.

条件与限制：Histories include endpoint maps and actual exposed paths. Retain gP in the outer marginal; do not average proposed unweighted histories or remove the all-hit condition.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/03-exposure.tex；prop:exposure; statement lines [74, 105]。

## CLM-271-F-LEM-EXTERIOR — 条件化前外幂矩

来源等级：C；完整链：未知。

陈述：For a finite permutation law built as independent transposition products and limits, E wedge^k Pi = wedge^k E Pi for every k. It applies to unconditioned fresh layered hole maps.

条件与限制：All exterior moments, not only the full determinant or trace. The lemma does not assert preservation after all-hit conditioning; independent factors are essential to this construction.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/03-exposure.tex；lem:exterior; statement lines [209, 229]。

## CLM-271-F-PROP-FIRST-MOMENT — 条件下一钉首矩

来源等级：C；完整链：未知。

陈述：For V=J disjoint union Q, J nonempty and the exterior-moment identities, all-hit probability is det(I-KQQ). If positive, KQQ is transient and the conditional next-pin mean is the Schur-complement first-positive hitting kernel. Arbitrary complex W determinant identity also holds.

条件与限制：Use column-forward matrices. An empty Q is permitted. The probability must be positive for conditioning/inversion; all mean entries are recovered, not only the trace. No full path-law equality follows.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/03-exposure.tex；prop:first-moment; statement lines [289, 318]。

## CLM-271-F-LEM-EXPOSURE-DENSE-RETURN — 暴露后的新鲜转移首矩

来源等级：C；完整链：未知。

陈述：For almost every actual exposure, next-pin return to T equals the corresponding fresh-turn hitting probability tau_T_positive<tau_E; outer averaging uses PP.

条件与限制：Finite pins plus dense boundary handled by the source limit. Fresh transition choices are remade on successive turns; this is an identity of conditional first moments, not of original repeated paths.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/03-exposure.tex；lem:exposure-dense-return; statement lines [428, 441]。

## CLM-271-F-LEM-RETURN-ENERGY — 最小命中函数与返回能量

来源等级：C；完整链：未知。

陈述：There is a smallest nonnegative f with f=1 on T, U* f=f off T, 0<=f<=1 and zero boundary. Counting energy equals sum_T(1-U*f), and m(1-r) bounds its actual-outer-law expectation.

条件与限制：Boundary-killed substochastic U and f use the SAME exposure. Closed classes inaccessible to T may have f=0; almost-sure absorption and reversibility are unnecessary.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/03-exposure.tex；lem:return-energy; statement lines [555, 578]。

## CLM-271-F-LEM-NONGRID — 非网格确定时刻阻塞

来源等级：C；完整链：未知。

陈述：Under the larger-pin induction input I_p(P), any prescribed 2d distinct sites are all blocked with probability <=C p^(2d); a nonempty sparse site set has probability <=(C sqrt(p))^|A| at each deterministic time.

条件与限制：Source grid mesh <=p^(4d), p<=1, fixed d,ell. Sparse growth counts slot multiplicity when choosing tests. Not independent-time or all-time blocking bounds.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/04-sparse-geometry.tex；lem:nongrid; statement lines [90, 102]。

## CLM-271-F-LEM-COMPONENT-TAIL — 阻塞分量尾

来源等级：C；完整链：未知。

陈述：For sufficiently small p<=p0 under I_p(P), a blocked component at a prescribed site reaches radius h with probability <=C exp(-c h^gamma), uniformly at every deterministic time.

条件与限制：Components use the source fixed adjacency radius. p0 and sparse-growth choices are fixed before decreasing p; separated sparse witnesses, not arbitrary counted assignments, justify the probability estimate.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/04-sparse-geometry.tex；lem:component-tail; statement lines [157, 170]。

## CLM-271-F-PROP-REGULARITY — 规则性失败概率

来源等级：C；完整链：未知。

陈述：For fixed local radius Mstar and the source regular-anchor definition, failure at a deterministic time and anchor is <=C R^d p^(2d)+C exp(-c R^xi), xi=nu gamma>0.

条件与限制：Assumes I_p(P), p<=p0, R>=1; constants may depend on fixed local geometry but not volume/grid/pins/anchor. Do not turn fixed-time failure into simultaneous all-time regularity.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/04-sparse-geometry.tex；prop:regularity; statement lines [290, 300]。

## CLM-271-F-LEM-LOCAL-CONNECTIVITY — 局部避障连通

来源等级：C；完整链：未知。

陈述：For fixed d>=2 and K, a radius rho(d,K)>=K+1 exists: endpoints within K avoiding F can be connected in B_rho if that ball contains fewer than 2d blocked sites, with length <=(2rho+1)^d.

条件与限制：A deterministic lattice statement with strict <2d hypothesis and fixed radii. It does not give global connectivity of arbitrary obstacle graphs.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/04-sparse-geometry.tex；lem:local-connectivity; statement lines [341, 351]。

## CLM-271-F-PROP-LOCAL-NASH — 可用槽局部Nash界

来源等级：C；完整链：未知。

陈述：For d>=3, bounded slot multiplicity and a regular anchor at sufficiently large scale R, a nonnegative slot function supported over B_R satisfies ||v||2^(2+4/d)<=C D(v)||v||1^(4/d).

条件与限制：Counting norms, zero extension beyond support and the stated Dirichlet convention. Available unblocked sites may have any multiplicity 1..ell. Geometry and support restrictions cannot be dropped.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/04-sparse-geometry.tex；prop:local-nash; statement lines [401, 413]。

## CLM-271-F-LEM-HULLS — 填充包络拓扑

来源等级：C；完整链：未知。

陈述：For finite blocked sets with the source radius-four thickening of fixed-range components, hulls are finite connected with connected complement and are disjoint or nested; crossing endpoints have distances four/five and exterior boundary routes avoid blocked sites.

条件与限制：d>=2 and the defined thickening/connectivity. The downstream representative map is applied once; representatives can lie in other hulls, so idempotence must not be presumed.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/05-flows.tex；lem:hulls; statement lines [63, 79]。

## CLM-271-F-PROP-FLOW-DECAY — 带衰减的单位流

来源等级：C；完整链：未知。

陈述：For d>=3, nu=1/(100d), a regular anchor and large enough R, each available source slot within B_R admits a flow of divergence delta_source with envelope C(1+distance)^(-k), k=d-1-d nu, and finite squared energy.

条件与限制：The source extends the finite-volume available graph to the infinite lattice with exterior slots available. A finite graph without a sink cannot have this divergence. Local geometry constants and specified source slots matter.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/05-flows.tex；prop:flow-decay; statement lines [171, 184]。

## CLM-271-F-LEM-FLOW-OVERLAP — 流包络重叠

来源等级：C；完整链：未知。

陈述：Two source-centered flow envelopes with d/2<k<d have sum_e |J(e)Jprime(e)| <=C(1+source_distance)^(-(2k-d)).

条件与限制：Specified lattice/slot growth and bounded envelope constants; this is a deterministic convolution bound, not stochastic independence of flows.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/05-flows.tex；lem:flow-overlap; statement lines [315, 327]。

## CLM-271-F-PROP-FLOW-ENERGY — 稀疏任意注入能量

来源等级：C；完整链：未知。

陈述：For source anchors with sparse growth L(1+h)^alpha, regular retained subset and arbitrary subunit masses over B_R, a flow realizes their summed divergence with energy <=C m R^alpha; finitely supported real tests obey the resulting Dirichlet pairing bound.

条件与限制：d>=3, alpha=1/100, nu=1/(100d), sufficiently large R. The graph is the extended infinite graph. Masses may depend on the same geometry; no independence assumption or measurable time-continuous flow choice is required.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/05-flows.tex；prop:flow-energy; statement lines [346, 371]。

## CLM-271-F-LEM-TWO-ENDS — 双端泄漏能量

来源等级：C；完整链：未知。

陈述：For fixed exposed environment, beta>=4s and real zero-boundary v, <v,(I-U)v> bounds half the sum of forward and reversed length-2s norm losses; each partial norm is nonincreasing.

条件与限制：Correct killed propagator factor order and adjoint reversal are required. Instantaneous completion losses remain nonnegative; do not replace inequalities by identities after dropping jumps.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/06-leakage.tex；lem:two-ends; statement lines [130, 141]。

## CLM-271-F-LEM-LOCALIZATION — 钉律平均局域化

来源等级：C；完整链：未知。

陈述：For s>=1, R=ceil(Cstar s), beta>=5s, any allowed cube/pins/single-time test and either direction, expected lost l1 mass under PP is <=C m exp(-c s) up to time 2s.

条件与限制：Actual exposure marginal, fixed distinguished starts and disjoint T; actual and independent fresh factorial measures are separated. No estimate conditional on an arbitrarily fixed exposure is inferred.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/06-leakage.tex；lem:localization; statement lines [234, 245]。

## CLM-271-F-LEM-REGULAR-TIME-DECAY — 足够规则时间后的扩散

来源等级：C；完整链：未知。

陈述：Under sparse tests and I_p(P), localized pieces have expected squared l2 norm <=C(s^-d/2+delta) for s<=u<=2s; their sum has bound C m[exp(-c s)+R^alpha(s^-d/2+delta)].

条件与限制：Either direction; source preliminary small-p threshold and regularity delta. Integrated regular-time decay, not independence of time slices or guaranteed good geometry at every time.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/06-leakage.tex；lem:regular-time-decay; statement lines [332, 346]。

## CLM-271-F-PROP-LEAKAGE — 期望泄漏闭合

来源等级：C；完整链：未知。

陈述：With s=p^-11/10, R=ceil(Cstar s), grid mesh <=p^(4d), larger-pin I_p(P) and beta>=5s, forward and reversed expected norm losses are >=m[1-epsilon(p)], with epsilon=C[exp(-cs)+R^alpha(s^-d/2+delta+s^-1)].

条件与限制：Small p, sparse T and D0 plus finite grid pins. The larger-pin hypothesis only is used; delta retains both polynomial and stretched-exponential terms. Existence of constants is not an effective temperature certificate.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/06-leakage.tex；prop:leakage; statement lines [403, 423]。

## CLM-271-F-THM-PIN-BOOTSTRAP — 统一稀疏钉闭合

来源等级：C；完整链：未知。

陈述：For each d>=3 and ell>=1, L>=max(2d,ell,4) and pstar in (0,1/4) exist. For p<=pstar, beta>=5p^-11/10 and source grid/sparse conditions, PE(T missing)<=p^|T|; in particular singleton boundary miss<=pstar at zero time.

条件与限制：Downward induction over a finite grid with disjoint nonempty single-time tests; beta remains finite. No arbitrary dense test law, practical pstar or temperature estimate is supplied.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/06-leakage.tex；thm:pin-bootstrap; statement lines [553, 573]。

## CLM-271-F-LEM-SURFACE-COST — 边界着色代价与谱尾

来源等级：C；完整链：未知。

陈述：At fixed sufficiently low-temperature source setup, forcing cycles meeting D0 to be up costs at most a surface exponential; the zero-field magnetization spectral tail above SV_N/2 is >=one-half exp(-C boundary). Missing cycles retain fair colors under the conditioning.

条件与限制：C depends on beta,d,S, not N. A positive tail is not positive zero-field mean, and the mark/color event is not itself a changed Hamiltonian.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/07-kms.tex；lem:surface-cost; statement lines [37, 52]。

## CLM-271-F-PROP-MAGNETIZED-LIMIT — 消失场选态

来源等级：C；完整链：未知。

陈述：With h_N=N^-1/2, finite Hamiltonian H_N-h_N M_N, product-trace exterior extension and translation averaging, there is a pointwise convergent subsequence to a translation-invariant state; every such selected subsequential limit has spin-z expectation >=S/4.

条件与限制：The low-temperature input from earlier sections is retained. This proposition selects the state; its KMS property is a further argument using dynamics/strip limits. Do not claim uniqueness or a convergence rate. Actual Lean uses a different existential box/field sequence.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/07-kms.tex；prop:magnetized-limit; statement lines [118, 139]。

## CLM-271-F-LEM-DEEP-DYNAMICS — 深箱动力学逼近

来源等级：C；完整链：未知。

陈述：For a fixed local observable, local support/origin set and compact real-time interval, finite-cube zero-field dynamics converge uniformly as the support depth grows. For the selected h_N and deep translates, tilted dynamics approach translates of the zero-field limit.

条件与限制：Uniformity is over deep boxes/translates and compact times. Uses established norm-locality input; it does not alone construct an ordered equilibrium state or control imaginary times by the same real-time norm bound.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/07-kms.tex；lem:deep-dynamics; statement lines [236, 255]。

## CLM-271-F-LEM-STRIP-LIMIT — 有界闭条带极限

来源等级：C；完整链：未知。

陈述：Individually bounded functions analytic inside a fixed closed beta-strip and continuous on it, with common real-edge bounds C, are uniformly bounded by C. Locally uniform convergence on BOTH edges gives closed-strip locally uniform convergence to the corresponding bounded analytic function.

条件与限制：Fixed beta>0. Individual boundedness, common boundary bounds and both edge limits are all required. This is the analytic step preserving both KMS boundary identities for the same limiting state.

定位：math/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/07-kms.tex；lem:strip-limit; statement lines [319, 338]。

