# F271 有限程Bloch稿的来源命题

由规范图谱生成。以下30条保留来源C、完整依赖链未知；不表示Lean覆盖、独立证明审核、完整族/历史或应用检验完成。

固定自旋/耦合和coset几何；完整色散决定系数。先积分场导数界，再N→∞、h↓0、固定K的β→∞，最后K→∞。

## CLM-271-FR-THM-MAIN · 有限程三维Bloch渐近律

At fixed S,J, lim beta^(3/2)(S-m_SJ(beta))=zeta(3/2)/(8*pi^(3/2)*sqrt(det D_SJ)).

适用条件与限制：

- Positive half-integer S fixed; J>=0,finite support,J0=0,J(z)=J(-z),support generates Z3. Spatial anisotropy and lack of nearest-neighbor bonds are allowed.
- D_SJ=(S/2)sum_z J(z)zz^T. Magnetization is the right field derivative AFTER the thermodynamic pressure limit.
- Integrate finite-volume derivative bounds first; take N->infinity,h->0+,beta->infinity at fixedK,thenK->infinity. No effective beta threshold or uniform-in-S,J error is supplied.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/01-introduction.tex`，thm:main statement lines[68, 77]; full source body previously read and selected scopes reread。

## CLM-271-FR-PROP-LOOP-REPRESENTATION · 带全耦合权重的交换圈表示

Z_Lambda(h)=exp(beta*w_Lambda/4) E_base sum_color exp(beta*h*M(color)); at h=0 the cycle-weight/color law gives the complete finite spectral law of total M.

适用条件与限制：

- Finite cube,beta>0,realh; ell=2S slots per site, every slot pair above each interaction bond has Poisson rate J_e/2.
- w_Lambda=sum over slot edges J_e; site seams are independent uniform slot permutations. The coloring magnetization is half the signed time-zero slot count.
- This finite spectral identity alone does not establish spontaneous magnetization, full quantum-state equivalence or low-temperature asymptotics.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/02-pins.tex`，prop:loop-representation statement lines[53, 70]; full source body previously read and selected scopes reread。

## CLM-271-FR-LEM-DENSE-BOUNDARY · 稠密边界切点极限

Increasing deterministic time sets with dense union eventually agree almost surely with continuous boundary pinning in cycle counts and avoiding-cycle sets; laws converge in TV and uniformly bounded a.s.-convergent observables converge in expectation.

适用条件与限制：

- Finite deterministicF; boundary slots at increasing finite time sets containing0, limitD=F unionD0.
- Finite sampled exchange picture and common deterministic bound for observables; not arbitrary unbounded-observable convergence or a finite approximation rate.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/02-pins.tex`，lem:dense-boundary statement lines[145, 159]; full source body previously read and selected scopes reread。

## CLM-271-FR-LEM-FACTORIAL · 实际标记的阶乘支配

Under any allowed or finite pin law, the ordered distinct-j-mark factorial integral is at most2^j times the base intensity product integral for every nonnegative measurable test.

适用条件与限制：

- j>=1; nonnegative measurable test, possibly infinite integral; prescribed time order/restrictions allowed.
- Weaker4^j may be used later. Mixed fresh/actual lists factor only via an independently sampled fresh Poisson family and unconditional factorial measures.
- Does not make repeated uses of physical marks across turns independent.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/02-pins.tex`，lem:factorial statement lines[182, 192]; full source body previously read and selected scopes reread。

## CLM-271-FR-PROP-PIN-IDENTITIES · 钉扎与改变后返回律

For i outsideE, d_E(i)=r(E,{i})/(1+r(E,{i})); for simultaneous target T, P_E(T subset B_E)<=(2r(E,T))^|T|.

适用条件与限制：

- E allowed or finite; nonempty distinct finiteT at ONE deterministic time, disjointE.
- r is the average strictly positive-time first T-return-beforeE event under the CHANGED pin law P=E unionT.
- Do not replace r by an unconditioned path return or drop the changed law.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/02-pins.tex`，prop:pin-identities statement lines[248, 255]; full source body previously read and selected scopes reread。

## CLM-271-FR-PROP-EXPOSURE · 保留外层权重的条件暴露

The remaining picture given the avoiding-cycle exposure has law Q_a conditioned onG_P; its exposure marginal retains 1_FA*2^cA*g_P(a)/Z_P.

适用条件与限制：

- Almost every exposure under the actual pinned law hasg_P(a)>0; conditional trajectory/endpoint branches are defined by deterministic initial label setsA.
- The same assertion holds for finite deterministicP. The g_P factor is part of the outer law, not a removable normalization.
- Conditional remaining pictures are not independent unconditioned fresh pictures.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/02-pins.tex`，prop:exposure statement lines[414, 440]; full source body previously read and selected scopes reread。

## CLM-271-FR-LEM-EXTERIOR-MOMENTS · 可准入排列的外幂矩

If a finite random permutation is a distributional limit of independent Bernoulli transpositions and deterministic permutations, E wedge^k Pi=wedge^k(E Pi) for every0<=k<=|V|.

适用条件与限制：

- The unconditioned layered permutation for fixed exposure and finite cuts underQ_a satisfies this admissibility.
- This is a law-specific all-exterior-moment statement, not a property of an arbitrary random permutation or its all-hit conditioned law.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/02-pins.tex`，lem:exterior-moments statement lines[504, 516]; full source body previously read and selected scopes reread。

## CLM-271-FR-PROP-NEXT-PIN-KERNEL · 全命中条件下的正步首返均值

For V=I disjointB,I nonempty and the exterior-moment law, Pr(every cycle meetsI)=det(I-K_BB); if positive, E Sigma conditionalG_I=K_II+K_IB(I-K_BB)^-1K_BI.

适用条件与限制：

- K=E Pi in column-forward convention; Sigma is the next POSITIVE visit permutation onI.
- Positive all-hit probability implies transience ofK_BB and admits the inverse; ifB empty determinant1/correction0.
- Only the conditional FIRST MOMENT equals the independent Markov hitting kernel; full routes/joint law and exterior closure after conditioning are not identified.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/02-pins.tex`，prop:next-pin-kernel statement lines[550, 569]; full source body previously read and selected scopes reread。

## CLM-271-FR-PROP-FRESH-WALK · 条件首返事件的一粒子恒等式

For almost every actual pinned exposure and every i inT, P_P(R_i conditional exposure)=q_i(a); hence |T|r(E,T)=E_P sum_i q_i(a).

适用条件与限制：

- P=E unionT; q_i is the fresh-walk positive return in the exposed environment with the actual stopping rule.
- The equality is conditional first-moment/event probability after integrating the exposure law with g_P; it does not couple the full original paths to independent fresh paths.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/02-pins.tex`，prop:fresh-walk statement lines[648, 657]; full source body previously read and selected scopes reread。

## CLM-271-FR-PROP-NASH · 局部可用槽图Nash界

For R>=R0 and a regular slice/anchor, nonnegative v supported above the multi-coset bar ball has ||v||2^(10/3)<=C D_t(v)||v||1^(4/3).

适用条件与限制：

- Regularity is the source deterministic per-coset blocked-site/hull condition, with all slots available outside the finite volume.
- D_t uses ALL weighted interaction bonds; c0 times the nearest-neighbor coset energy is only a lower comparison.
- C is uniform in R,z,t,unavailable slots, but depends on fixedS,J,coset/geometry choices; no uniform near-degenerate coupling claim.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/03-geometry.tex`，prop:nash statement lines[195, 203]; full source body previously read and selected scopes reread。

## CLM-271-FR-LEM-ROUTED-FLOW · 正则三维图的共同单位流路由

In the available-slot nearest-neighbor graph, each source slot overB_R has a unit flow to infinity with divF=delta_a and envelope C(1+distance)^(-199/100).

适用条件与限制：

- At mostell slots/site; all available slot pairs joined above NN site edges; all slots available outside a finite set; both regular-anchor conditions andR>=R0.
- Use maximal disjoint filled hulls and route each ORIGINAL endpoint only once; retain a uniformly bounded connector and routed lattice inverse-square flow.
- Infinite-graph unit flow input, not a sink-free finite-torus divergence identity or a measured fast routing algorithm.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/03-geometry.tex`，lem:routed-flow statement lines[292, 327]; full source body previously read and selected scopes reread。

## CLM-271-FR-PROP-SPARSE-ENERGY · 稀疏多源的能量配对

For a sparse list ofm centers counting repetitions, any regular subsetI and nonnegative subunit masses mu_i supported in each bar ball satisfy |<sum mu_i,Y>|^2<=C*m*R^alpha*D_t(Y).

适用条件与限制：

- R>=R0,alpha=1/100; every selected center regular at the slice; each mass<=1.
- Y real finitely supported on the infinite available-slot extension. Multiplicities and all cosets count toward the source sparse-growth bound.
- No probability independence among sources is assumed and no finite-torus cutoff error is silently removed.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/03-geometry.tex`，prop:sparse-energy statement lines[358, 369]; full source body previously read and selected scopes reread。

## CLM-271-FR-LEM-NEAR-FLOW · 局部半径内的逆平方流衰减

The SAME routed flows satisfy |F_a(e)|<=C(1+h)^(-2) for distanceh<=R from the source site.

适用条件与限制：

- Use the fixed routing construction of the routed-flow lemma and its regularity hypotheses.
- C andR0 independent ofR, with fixed geometry; outside radiusR only the weaker global exponent is asserted.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/03-geometry.tex`，lem:near-flow statement lines[412, 419]; full source body previously read and selected scopes reread。

## CLM-271-FR-PROP-SPREAD-ENERGY · 已扩散单源的能量改善

For a regular slice and nonnegative source of mass<=1 and ||mu||2<=C1*tau^(-3/4), |<mu,Y>|^2<=C*tau^(-1/2)*D_t(Y).

适用条件与限制：

- 1<=tau<=R andR>=R0; source supported above the anchor bar ball; Y real finitely supported.
- C may depend onC1 and fixed geometry, nottau,R,slice orvolume. A bareL2 bound withtau>R is outside the statement.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/03-geometry.tex`，prop:spread-energy statement lines[457, 472]; full source body previously read and selected scopes reread。

## CLM-271-FR-LEM-BLOCKING · 有限网格归纳下的阻塞界

Assuming I(P), any prescribed6 distinct blocked coordinate sites have probability<=C*p^6; any nonempty sparse setA has probability<=(C*sqrt(p))^|A| at a deterministic time.

适用条件与限制：

- p=beta^(-9/10),beta>=1; P=D0 unionF on a finite circular grid with gaps<=p^12; I(P) concerns sparse tests disjointP at grid times.
- Uniform over finite grid choice/size, cosets and deterministic times; this conditional induction input is later discharged, not assumed for a smaller pin set.
- Finite-range marked-star counts do not require the full interaction graph to be bipartite.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/04-bootstrap.tex`，lem:blocking statement lines[51, 63]; full source body previously read and selected scopes reread。

## CLM-271-FR-LEM-COMPONENT-TAIL · 阻塞连通分量的伸展指数尾

Under I(P), P_P(w blocked and radius_w C(w)>=h)<=C exp(-c*h^lambda),h>=1,uniform deterministic time/coset/site.

适用条件与限制：

- beta>=beta0 with fixed model constants. Components use blocked-site sup-distance<=8 adjacency.
- Only separated sparse binary-tree witnesses enter the probability union bound; unrestricted assignments are merely a numerical overcount.
- Not independent site percolation and not a uniform tail under arbitrary outside laws.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/04-bootstrap.tex`，lem:component-tail statement lines[108, 119]; full source body previously read and selected scopes reread。

## CLM-271-FR-PROP-IRREGULARITY · 单切片失正规概率

Under I(P), every deterministic t,z andR>=1 obey P_P(slice not regular)<=delta_R=C R^3 p^6+C exp(-c R^xi),xi=nu*lambda>0.

适用条件与限制：

- beta>=beta0;nu=1/300 and fixed regularity radii/coset geometry.
- The subsequent good-exposure bound uses Fubini/Markov and does not assume independent time slices.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/04-bootstrap.tex`，prop:irregularity statement lines[191, 200]; full source body previously read and selected scopes reread。

## CLM-271-FR-LEM-LOCALIZATION · 无需归纳前提的路径局域化

A deterministic schedule of at most2K+2 full/partial traversals, either direction and each<=one period, loses expectedL1 mass at mostC_K exp(-c beta) when localized at the initial anchor.

适用条件与限制：

- R_K=ceil(a(K+1)beta); choosea independently ofK. Initial deterministic slot is almost surely a hole under an allowed pinned exposure law.
- Matching layers at every concatenation, start/end/spatial killing projections included; noI(P) assumption.
- Also valid for the all-available full-slot walk. Reused physical marks across turns are controlled by unconditional path counting, not false independence.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/04-bootstrap.tex`，lem:localization statement lines[254, 270]; full source body previously read and selected scopes reread。

## CLM-271-FR-PROP-DIFFUSION · 好暴露下正反子区间扩散

On a good exposure, any localized arbitrary-direction traversal subinterval sends nonnegative mass<=1 to L2 norm<=C*b^(-3/4) for elapsedb>=beta/16; entry maximum<=C*b^(-3/2) forb>=beta/8.

适用条件与限制：

- The sameL2 statement holds for adjoints. Good means nonregular time in a period has measure<=beta/100.
- C independent ofK andR_K with fixed model/geometry. Kernels use one fixed exposure and matching instantaneous operations.
- Good-exposure assumption is deterministic here; obtaining its probability needs the separate sparse-pin bootstrap.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/04-bootstrap.tex`，prop:diffusion statement lines[320, 335]; full source body previously read and selected scopes reread。

## CLM-271-FR-LEM-HITTING-ENERGY · 正步命中与对称部分能量

For targetT, f=1 onT and boundary-killed future-turn hitting probability elsewhere, g=f-eta gives sum_T q_i<=|T|-<f,(I-Q)f>=<eta,Qeta>+2<Qeta,g>-<g,(I-Q)g>.

适用条件与限制：

- E allowed,T finite nonempty/disjointE at one deterministic cut,P=E unionT.
- Q=(U+Utranspose)/2; U boundary-killed one-period column kernel, with zero boundary coordinates. Extra pins affect q stopping and the bound, so keep the inequality.
- 0<=f<=1 without assuming almost-sure absorption; do not exchange Q powers with original U powers.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/04-bootstrap.tex`，lem:hitting-energy statement lines[373, 388]; full source body previously read and selected scopes reread。

## CLM-271-FR-LEM-SUFFIX-ENERGY · 正反后缀能量耗散

For y zero on boundary and E_y=<y,(I-Q)y>, a matched splitU_d=B_d C_d onI=[beta/3,2beta/3] gives integral D_t(Y_d)<=1/2(||y||2^2-||U_dtranspose y||2^2)<=E_y; ||Y_d||infinity<=||y||infinity.

适用条件与限制：

- Y_d=B_dtranspose y,d=+/-; physical time uses theta+/-u modbeta.
- Each instantaneous operation assigned exactly once; exceptional split times are ignored only in the integral.
- Counting norms and the full weighted energy, with killed vectors extended by zero.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/04-bootstrap.tex`，lem:suffix-energy statement lines[428, 437]; full source body previously read and selected scopes reread。

## CLM-271-FR-THM-SPARSE-PINS · 解除归纳的统一稀疏钉估计

For beta>=beta1, every allowedE and nonempty sparseT at a deterministic time disjointE satisfy P_E(T subsetB_E)<=beta^(-9|T|/10); irregular/good bounds then hold withoutI(P).

适用条件与限制：

- Finite downward induction uses estimates for LARGER pin sets, then dense-grid extension; beta1 independent cube/pins.
- Sparse growth counts slot multiplicities across all cosets. This rough beta^(-9/10) statement precedes, and cannot assume, the later sharp singleton bound.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/04-bootstrap.tex`，thm:sparse-pins statement lines[454, 465]; full source body previously read and selected scopes reread。

## CLM-271-FR-LEM-RETURN-EXPANSION · 有限正步返回展开

For singleton eta, v=sum_(n=1)^(K-1)Q^n eta,y=f-eta-v andE_y=<y,(I-Q)y>, q_i<=sum_(n=1)^(2K-1)<eta,Q^n eta>+2<Q^K eta,y>-E_y.

适用条件与限制：

- K>=1 fixed,empty sum0; E_y>=0 and||y||infinity<=K+1.
- Under actual singleton-changed pin law, original hitting f usesUtranspose and Q only enters its real quadratic form.
- A finite expansion, not an infinite Green series or proof of certain killing.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/05-returns.tex`，lem:return-expansion statement lines[26, 38]; full source body previously read and selected scopes reread。

## CLM-271-FR-PROP-LONG-TAIL · 长返回余项及K一致首常数

At fixed integerK>=1, E_P[2<Q^K eta,y>-E_y]<=C*K^(-1/2)*beta^(-3/2)+o_K(beta^(-3/2)).

适用条件与限制：

- C depends only on fixed interaction,spin andgeometry and is INDEPENDENT ofK.
- The little-o is uniform after averaging over cubes,cuts,slots and all finite extra pins for each fixedK, without a uniform-in-K convergence rate.
- Use R_K,good-exposure diffusion and spread-source energy after the sparse-pin theorem; no unregistered finite-beta numerical error follows.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/05-returns.tex`，prop:long-tail statement lines[65, 74]; full source body previously read and selected scopes reread。

## CLM-271-FR-COR-SINGLETON-BOUND · 全钉律的尖锐阶单点稀疏

For all sufficiently largebeta, uniformly in allowedE,cubes,cuts andi outsideE, r(E,{i})<=C beta^(-3/2); avoiding-pin slot probability is also<=C beta^(-3/2).

适用条件与限制：

- Derived withK=1 AFTER rough sparse-pin bootstrap,finite expansion,long-tail and diffusion.
- This order bound is not yet the sharp Bloch coefficient and is not a circular bootstrap input.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/05-returns.tex`，cor:singleton-bound statement lines[175, 186]; full source body previously read and selected scopes reread。

## CLM-271-FR-LEM-IDEAL-KERNEL · 完整色散的理想核系数

For site jump ratesS*J(z), sup p_t<=C(1+t)^(-3/2) andp_t(x,x)=t^(-3/2)(kappa+o(1)),kappa=1/((4pi)^(3/2)*sqrt(detD)). Fixed direction-word diagonals equalell^-1 p_(n beta),n<=2K.

适用条件与限制：

- Full support generatesZ3, yielding the unique Brillouin zero; mere real span gives positiveD but need not give that uniqueness.
- Every full ideal traversal has a fresh uniform seam. Reverse independently averaged traversals do not cancel as fixed permutation matrices.
- Killed diagonal<=full; exponential lower comparison needs the entire bar ball interior. Word/cut/slot errors uniform for fixedK only.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/06-ideal.tex`，lem:ideal-kernel statement lines[50, 75]; full source body previously read and selected scopes reread。

## CLM-271-FR-PROP-FINITE-WORD · 同一暴露先乘后平均的有限词比较

For fixedK and1<=n<=2K, |E_P[(W_R(direction word))_ii]-(idealW_R(word))_ii|=o_K(beta^(-3/2)),uniform allowed extra pins,volume,cut andslot.

适用条件与限制：

- Product is formed BEFORE averaging over the SAME exposure; independent fresh transition randomness within traversals is distinct from independent exposures.
- A coupling giveso_K(1) mass error and midpoint diffusion suppliesbeta^(-3/2); do not interchange averaging and multiplication.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/06-ideal.tex`，prop:finite-word statement lines[123, 134]; full source body previously read and selected scopes reread。

## CLM-271-FR-THM-RETURN-BOUNDS · 带尖锐系数的单槽上下界

At beta>=beta_K, d_E(i)<=beta^(-3/2)[(kappa/ell)sum_(1..2K-1)n^(-3/2)+C K^(-1/2)+epsilon_K]; pin-free interior balls additionally give the lower K-term sum minus epsilon_K.

适用条件与限制：

- C independentK; beta_K andepsilon_K->0 may dependK,not volume/cut/slot or number/locations/times of finite extra pins.
- Upper holds every deterministic slot; lower requires wholemulti-coset bar ball interior and no pins over it. For i outsideE the same bounds apply tor(E,{i}).
- No explicit finite-temperature accuracy threshold or uniformK error is provided.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/06-ideal.tex`，thm:return-bounds statement lines[314, 343]; full source body previously read and selected scopes reread。

## CLM-271-FR-PROP-PRESSURE-EQUIVALENCE · 固定参数下的边界压力等价

For each fixedbeta>0 andh>=0, plus/pinned boundary pressure converges to the original free-boundary thermodynamic pressure asN->infinity.

适用条件与限制：

- Finite interaction range; compare boundary/surface terms at fixedbeta,h.
- Pointwise pressure equality does not itself commute field derivatives or give a uniform joint beta/N error.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/07-pressure.tex`，prop:pressure-equivalence statement lines[35, 42]; full source body previously read and selected scopes reread。

## CLM-271-FR-LEM-PIN-MIXTURE · 保留后验相关性的额外钉混合

At h>=0 the plus colored law mixes zero-field pinned lawsD0 unionF over time-zero slots, with each mixing marginalP(i inF)<=1-exp(-beta h); S-(p_Nplus)prime=volume^-1 sum_i E_F d_(D0 unionF)(i).

适用条件与限制：

- The POSTERIOR mixing law is not an independent product pin law. A union bound, not independence, controls a pin-free ball.
- Integrate finite-volume derivative inequalities in h beforeN,h,beta,K limits; finitebeta,K ball volume remains fixed whenh->0+.
- Do not differentiate a zero-field free-energy asymptotic in an unexamined field.

来源：`math/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/07-pressure.tex`，lem:pin-mixture statement lines[84, 100]; full source body previously read and selected scopes reread。

完整原文散列和本批规范账本：`data/provenance/readings/F-271-finite-range-claims-WP129.json`。所有旧记录/科学输入保持，剩余53条十月来源定位及全族历史仍待。
