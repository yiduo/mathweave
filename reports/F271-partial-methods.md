# F271：八个来源方法接口，完整族整理仍在进行

本报告由规范方法记录导出。原文主张不是数学审核通过；八个接口均为来源C、完整链未知，无新增候选或科学运行。118个带标签定位仅是词法索引，不计118个完成拆解。四当前稿已实际读完，整族命题、历史书目和跨域关系仍待整理。

## PART-271-CONDITIONAL-KERNEL — 条件下一钉均值

输入：A finite admissible unconditioned permutation law on I disjoint union D; K is its column-forward mean.

输出：Unnormalized next-pin determinant identity; if Pr(all cycles hit I)>0 and I nonempty, E[Sigma|all-hit]=KII+KID(I-KDD)^-1 KDI.

条件：Admissibility is a limit of independent Bernoulli transpositions and deterministic permutations.；Positive all-hit probability is required for conditional expectation and inverse; the unnormalized polynomial identity also covers zero probability.

迁移限制：Only a conditional first moment is identified. Full paths are not independent fresh Markov paths; the conditioned permutation need not retain exterior-moment closure.

旧方法比较：DLM2020 all-minor preservation/independent products is an old baseline; the all-hit bridge needs its separate identity.

来源：math/preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/sections/02-exchange.tex；lem:next-pin statement lines [267, 295]; full containing file previously actually read。

## PART-271-DUAL-CAPACITY — 双方向残差到容量误差

输入：A finite nonnegative doubly substochastic U with killed coordinates, an unkilled point i, and trial h with h(i)=1 and h=0 on killing.

输出：For the probability q of a positive-step return to i before killing, |q-(1-c)|<=|<h,mu+>|+2X^2+2epsilon.

条件：Counting measure and column-forward U. Real c; ||h||infinity<=M.；There are X,epsilon>=0 with |<mu_d,z>|<=X sqrt(<z,(I-U)z>)+epsilon for BOTH d=+,- and EVERY real z vanishing on K with ||z||infinity<=1+M.

迁移限制：A scalar residual alone is insufficient. Inaccessible closed classes are allowed. This gives neither a new fast solver nor practical error constants without constructing the dual certificate.

旧方法比较：Gaudilliere-Landim nonreversible potential theory and direct finite harmonic linear algebra are old baselines, with different stationary/irreducibility interfaces.

来源：math/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/04-capacity.tex；lem:capacity statement lines [73, 94]; full containing file previously actually read。

## PART-271-TORUS-FLOW — 环面截流与残差配对

输入：Sparse source centers, subunit nonnegative masses supported in regular lifted balls B_A, and a torus L sufficiently large relative to A.

输出：A source pairing is bounded by sqrt(C m A^alpha) sqrt(Dirichlet energy)+C m L^(1/2-k)||Y||2, k=199/100.

条件：Regularity is the deterministic lifted-hole condition.；Keep the cutoff divergence error; the later absorption uses ghost killing energy >=q||Y||2^2.

迁移限制：An infinite unit-source flow cannot simply become a sink-free finite-torus flow. Dropping the divergence error changes the statement. Constants and thresholds are model dependent.

旧方法比较：Classical flow-energy and Cauchy-Schwarz bounds remain baselines; no routing runtime improvement has been measured.

来源：math/preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/sections/03-sparse-pins.tex；lem:torus-flow-pairing statement lines [414, 428]; full containing file previously actually read。

## PART-271-CLOSED-CLASSES — 迹界控制小封闭类

输入：The source exposure skeleton graph Gamma, row-stochastic and column-stochastic K closed on its components, w=1-q in (0,1), D=I-wK.

输出：Each closed component contributes at least 1/q to Tr D^-1; the soft-pin trace estimate yields E[number of components]<=q N.

条件：The source endpoint/contact graph and soft-pin weighted law are required.；The bound E Tr D^-1<=N is an additional source identity, not automatic for every stochastic K.

迁移限制：Does not assume irreducibility, reversibility or large classes. It does not assert a component bound for an arbitrary graph lacking the trace estimate.

旧方法比较：Finite stochastic-block eigenvalue and resolvent identities are the old linear-algebra baseline.

来源：math/preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/sections/04-spatial-comparison.tex；lem:skeleton-graph statement lines [234, 248]; full containing file previously actually read。

## PART-271-STRIP-CURVATURE — 条带零点条件下的曲率传播

输入：Holomorphic F in |Im z|<a0, real/even on R, F(0)=0, 0<=F(x)<=K|x| and Re F(x+iy)<=F(x).

输出：A positive convolution representation of Fsecond gives 0<=Fsecond(x)<=exp(2pi|x|/a) Fsecond(0), and the integrated exponential bound on F.

条件：Choose a strictly inside (0,a0).；All strip, growth and positivity assumptions apply; the source argument localizes in frequency before using its Schwartz multiplier.

迁移限制：Ordinary spectral Laplace variance is not Duhamel covariance. No universal concentration statement follows for data with unverified zero-free strip.

旧方法比较：Classical complex analysis and exponential Markov bounds remain the comparison route; the strip width must be supplied.

来源：math/preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/sections/05-zero-field.tex；lem:strip-curvature statement lines [18, 42]; full containing file previously actually read。

## PART-271-CYCLIC-ZERO-FREE — 严格单槽收缩到循环迹非零

输入：Finite cyclic product with at least one admissible mean-permutation layer and intervening tensor single-slot matrices.

输出：The complete cyclic trace is nonzero when each intervening slot map sends the closed unit disk strictly into the open disk with nonvanishing coordinate factor.

条件：The projective coordinate must remain defined on the closed disk.；Every slot between successive permutation layers satisfies the strict mapping condition.

迁移限制：Samplewise nonzero traces do not imply their average is nonzero. Arbitrary complex insertions or non-strict boundary maps are not admitted.

旧方法比较：Asano/Ruelle contraction antecedents remain an unqualified historical interface here; not an invented new zero-free theorem.

来源：math/preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/sections/02-exchange.tex；lem:trace-zero-free statement lines [390, 403]; full containing file previously actually read。

## PART-271-PRESSURE-INCREMENTS — 用压力增量保留极限顺序

输入：Finite-volume positive-field pressure, the actual posterior mixture of extra pins and uniform pin estimates.

输出：Integrate finite-volume derivative bounds before volume and field limits; then fixed-K low-temperature estimates can be passed to the K limit in their stated order.

条件：Posterior pin mixing is not an independent product law.；Keep N->infinity, right field->0, beta->infinity at fixed K, then K->infinity.

迁移限制：Zero-field free-energy asymptotics alone cannot be differentiated in an unexamined field. A fixed-K little-o is not an effective uniform-in-K finite-temperature error.

旧方法比较：CGS2015 zero-field free energy is a qualified older interface, not already a field-derivative magnetization conclusion.

来源：math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/07-pressure.tex；lem:pin-mixture statement lines [84, 100]; full containing file previously actually read; entire containing pressure section and final integrated-derivative proof, not mixture statement alone。

## PART-271-HARMONIC-SELECTION — 由样本矩选择调和对数

输入：Almost surely nonzero holomorphic random F_n in the right half-plane, T_n->infinity, locally Lipschitz s and a dense set of positive real points.

输出：Matching exponential product first/second moments and the locally uniform second-moment upper bound select a harmonic v with v(x)=s(x) and v(z)<=s(Re z).

条件：All finite dense-point products need the stated moment limits.；Nonvanishing is samplewise and logarithmic normalization is T_n.

迁移限制：An existence selection does not supply a practical sampler, a success probability bound for finite budgets, or zero-freeness of the average.

旧方法比较：Paley-Zygmund, submean estimates and Harnack compactness form the classical comparison ingredients; no computational advantage is inferred.

来源：math/preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/sections/07-pressure.tex；lem:harmonic-selection statement lines [373, 395]; full containing file previously actually read。

