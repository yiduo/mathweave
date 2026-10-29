# F271修正稿：23条来源陈述及选定证明接口

固定上游1581d4cb；来源C、完整依赖链未知。本文由规范账本导出。已有容量引理不重复登记，修正稿24定位均已语义绑定；全族累计88/118，剩球面稿30条。没有新增应用初检、完整族/历史或形式审核信用。

模型：Nearest-neighborZ3 quantumHeisenbergferromagnet,fixedpositivehalf-integerS,ell=2S,unorderededgeonce,slotrate1/2,freefinitecubes

极限：Integratefinite-volumefieldderivative;Ninfinityatfixedbeta,h;h0+atfixedbeta;betainfinityatfixedS. No effectivefinite-beta threshold orjointSlimit.

注意：原物理结论余项为o((betaS)^(-5/2))，不能移用理想密度的O((betaS)^(-7/2))。双残差、全正周期、后验钉扎不独立、严格源切片次序和最后区块复制预算均保留。

## CLM-271-CORR-THM-MAIN — 固定自旋的第一晶格修正与完整理想磁振子密度

At fixed S, lim_(beta->infinity) (beta*S)^(5/2)[S-m_S(beta)-n_sw_S(beta)]=0.

- Nearest-neighbor isotropic quantum Heisenberg ferromagnet onZ3,free finite cubes,each unordered edge once; fixed positive half-integerS.
- m_S(beta) is the right zero-field derivative of thermodynamic pressure. Integrate the finite-volume field derivative first;N->infinity at fixedbeta,h;thenh->0+ atfixedbeta;finallybeta->infinity. No joint S/temperature or simultaneous field scaling is asserted.
- n_sw is the FULL lattice Bose integral with epsilon_S(k)=2S*sum_j(1-cos k_j),including all positive return periods. No effective beta0 or finite-size engineering tolerance is supplied.
- The posterior field-pin set is not Bernoulli after partition reweighting. Its single-slot inclusion bound<=1-exp(-beta*t) and uniform deterministic-pin comparison are used before taking limits.

来源：`math/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/01-introduction.tex`，thm:main statement lines[45, 51];complete containingmodule/definitions/proof actuallyreread。

## CLM-271-CORR-COR-EXPANSION — 晶格两项展开的物理余项范围

S-m_S(beta)=zeta(3/2)/(8*pi^(3/2))*(beta*S)^(-3/2)+3*zeta(5/2)/(128*pi^(3/2))*(beta*S)^(-5/2)+o((beta*S)^(-5/2)).

- Same fixedS,nearest-neighborZ3 model and pressure-limit definition as thm:main.
- The ideal-density heat-kernel expansion has O((beta*S)^(-7/2)) remainder; the interacting magnetization conclusion has only the stated little-oh remainder. Do not transfer the sharper ideal remainder to the quantum model.
- The manuscript attributes the lattice coefficients to earlier spin-wave theory; this package does not newly verify Dyson originals or claim a new coefficient discovery.

来源：`math/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/01-introduction.tex`，cor:expansion statement lines[55, 63];complete containingmodule/definitions/proof actuallyreread。

## CLM-271-CORR-PROP-LOOPINPUTS — 有限体积圈/钉扎输入与改变后的返回律

Tr exp(-beta*H)=exp(beta*qLambda/4)*E_base2^cycles; d_E(i)=r/(1+r),r=E_(E+i)q_i. For simultaneous finiteT at one time,P_D(T subsetB_D)<=(2r_T)^|T|; j-mark factorial measure<=2^j times base.

- Finite cube,beta>0,ell=2S slots,nearest-neighbor slot-edge rate1/2,independent uniform site seams. AllowedD is all-time inner-boundary pins plus finite deterministicF.
- q_i is a STRICTLY positive-elapsed return of the fresh walk,periodic exposure but fresh transition randomness each turn,beforeE killing. Exposure sampled under CHANGED pin law E union{i}.
- SimultaneousT consists of distinct slot-time points at ONE deterministic time,disjointD; no spatial separation required. Distinct marks/factorial measures do not imply independent trajectories or snapshots.
- All-time boundary inputs use the companion dense-boundary limit; these imported statements are source assertions,not a complete companion-proof audit.

来源：`math/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/02-loops.tex`，prop:loopinputs statement lines[75, 108];complete containingmodule/definitions/proof actuallyreread。

## CLM-271-CORR-LEM-KERNELENERGY — 双次随机收缩与一个周期能量

Every killed interval kernel and adjoint are doubly substochastic and contract counting l1,l2,linfinity; smooth norm loss is -2D_t(v). For U_d=U orU*,int D(Y)<=e_y and ||y-U_d^* y||_2^2<=2e_y.

- Forward kernels act on COLUMNS with counting measure; killing is a projection,exit killing retains diagonal exit rates. y vanishes on cut killing slots.
- Adjoint reverses factor order,inverts transports,transposes seams and reverses killings. Two sides of an instantaneous operation remain distinct; each seam appears once per traversal.
- Energy integral is for ONE complete traversal,not an arbitrary sum of repeated budgets. Instantaneous contractions only decrease norm. Extra spatial killing and cuts are permitted.

来源：`math/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/02-loops.tex`，lem:kernelenergy statement lines[141, 165];complete containingmodule/definitions/proof actuallyreread。

## CLM-271-CORR-PROP-GEOMETRYINPUTS — 导入的稀疏几何、局部Nash和无穷远流

For p=(5/beta)^(10/11), nonregular-slice probability<=C*R0^3*p^6+C*exp(-c*R0^xi). Local regularity gives counting Nash ||v||2^(10/3)<=C*D(v)*||v||1^(4/3),local paths and unit flows with near inverse-square/far exponent199/100 envelopes.

- FixedS,sufficiently largebeta,allowedD,deterministictime,anchor andR0 above a fixed threshold. Local regularity excludes6blocked sites in fixed Mstar balls; distant blocked components have the specified radius growth.
- Nash uses vectors supported aboveB_R0. Full regularity is needed for flows to infinity on the exterior-extended available-slot graph; local regularity alone is not full global geometry.
- Near flow bound C(1+b)^(-2) only for b<=R0; global bound is C(1+b)^(-199/100). Constants uniform volume,pins,anchor,time,not uniformS. Imported original companion scope remains conditional.

来源：`math/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/03-geometry.tex`，prop:geometryinputs statement lines[31, 61];complete containingmodule/definitions/proof actuallyreread。

## CLM-271-CORR-PROP-SNAPSHOT — 至多六个同时点的扩散密度稀疏界

With lambda=beta^(-3/2),P_D(T subsetB_D)<=C*lambda^|T| for1<=|T|<=6 distinct slots at one deterministic time.

- Uniform finite cube,allowed deterministicD,time andpointlocations; distinct slots at one site are included. IfT meetsD the event is empty.
- Proof first uses older one-turn localization/diffusion/spread-source estimates under changedPprime=D unionT and boundary-only killing; it does not assume the refined good event or final Bloch comparison it later helps prove.
- No multi-time independence,unbounded-orderjoint bound or deterministic pointwise density follows.

来源：`math/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/03-geometry.tex`，prop:snapshot statement lines[93, 101];complete containingmodule/definitions/proof actuallyreread。

## CLM-271-CORR-LEM-ISOLATEDPATH — 孤立暴露轨迹的联合事件支配

P_P(isolation and X inA)<=2*P_base(tagged X inA),in either direction,for the specified interior path events.

- Deterministic starting slot and an interval of positive length<beta with NO seam in its interior; X is the actual picture strand and isolation requires no other exposed slot at its site or adjacent sites on both sides of jumps.
- Paths inA stay interior. A seam at an endpoint is excluded by using post-seam atstart/pre-seam atend,also in reverse tracing.
- This bounds the JOINT event of isolation and pathA; it is not domination of the conditional strand law given isolation,or of arbitrary exposed strands.

来源：`math/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/03-geometry.tex`，lem:isolatedpath statement lines[216, 235];complete containingmodule/definitions/proof actuallyreread。

## CLM-271-CORR-PROP-GOOD — 双向周期好暴露及小于修正阶的坏集

UnderP_(E+i),there is periodicG withP(Gc)=o(beta^(-5/2)); both directions have block/bin step bounds,at most5local obstacle slots,all-time local regularity,at least half regular time perblock,and isolated-strand displacement<=C*L^(3/4).

- Injectioni is post-seam at0 overx;B_(50Rstar)(x) interior and noE pins above it. FixedS; Dstar=sqrt(beta),L=beta^(1/200),R=beta^(3/2+1/800),Rstar=ceil(beta^(5/3)).
- Half-period partitions have blocklengthL..2L,bins1..3; seam sides assigned once as specified. Counts include different strands of the SAME cycle separately. Constants chosen c0,then c2,then c1.
- Isolation at blockstart uses c2L separation; onG strands stay>2fromotherobstacles. Snapshot union gives beta^(-2.91) six-failure bound; isolated-path JOINT domination controls exceptional displacement before conditioning onG.

来源：`math/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/03-geometry.tex`，prop:good statement lines[302, 325];complete containingmodule/definitions/proof actuallyreread。

## CLM-271-CORR-LEM-HEATBOUND — 固定好暴露的局部热核

OnG,an interval kernel killed on exitB_Rstar has maximum entry<=C*(1+elapsed)^(-3/2).

- Either direction,anystarting slice,extra spatial killing andcopiedperiods; actual kernels kill onE,not onthe injectioni.
- Deterministic fresh-walk statement at a fixed good exposure,from all-time local Nash andnorm contraction; not an independent Poisson law conditioned onG.

来源：`math/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/03-geometry.tex`，lem:heatbound statement lines[404, 412];complete containingmodule/definitions/proof actuallyreread。

## CLM-271-CORR-LEM-LOCALIZATION — 好暴露下新鲜游走的亚弹道定位

For elapsedu<=2beta fromaboveB_6R,onG excessive displacement beyond C*(1+u/L)*L^(3/4) has rapidly small probability;adding exit killing atB_Rstar has rapidly small mass loss.

- Both directions,arbitrary starting slice,probability of excessive displacement BEFORE killing,uniform overfixedgoodexposures. Rapidly small meansO_j(beta^(-j)) for everyfixedj,not a numerical finite-beta threshold.
- Forced transport times are deterministic afterexposure. Occupation andforcedstep estimates use localheatbounds andthe Markov property ofthe freshwalk; no conditional-Poisson assertion is used.

来源：`math/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/03-geometry.tex`，lem:localization statement lines[428, 440];complete containingmodule/definitions/proof actuallyreread。

## CLM-271-CORR-LEM-FLOWOVERLAP — 全正规切片的分离流重叠

For availablea,aPrime overB_6R at a fully regular slice onG,sum_e |J_a(e)*J_aPrime(e)|<=C/(1+site_distance(a,aPrime)).

- Flows live onthe exterior-extended holegraph. Slot multiplicity retained;distance isbetween sites.
- Uses inverse-square near envelopes and exponent199/100 far tails plusR=o(Rstar); not a generic statement for arbitrary networks or local regularity alone.

来源：`math/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/03-geometry.tex`，lem:flowoverlap statement lines[522, 531];complete containingmodule/definitions/proof actuallyreread。

## CLM-271-CORR-PROP-COMPARISON — 无局部钉扎区域的统一返回/下自旋比较

For sufficiently largebeta, |d_E(i)-n_sw_S(beta)/ell|<=epsilon_S(beta)*beta^(-5/2),epsilon_S->0. Same error for |E_(E+i)q_i-n_sw_S(beta)/ell|.

- Fixed positive half-integerS,anyfinitecube,allowedE=D0 unionF,i=(x,a)post-seam0. B_(50Rstar)(x) interior andE has no point above this ball;Rstar=ceil(beta^(5/3)).
- Uniform overthe number andlocations ofpins OUTSIDE the ball;effectivebeta0,epsilon curve andfinite-size constants are not supplied.
- Uses one scalar absolute residual pairing and BOTH forward/adjointenergy certificates;good-eventcomplement chargedbyits probability. Small v~beta^(-3/2) allows rational r/(1+r) corrections O(beta^(-3)),below beta^(-5/2).

来源：`math/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/04-capacity.tex`，prop:comparison statement lines[10, 26];complete containingmodule/definitions/proof actuallyreread。

## CLM-271-CORR-LEM-FREEBOUNDS — 全正周期自由势的空间/时间包络

For free profiles,smooth value/difference/time derivative<=C*(G,W,W/Dstar); pointpart atd=sqrt(1+s)<=C*(P_d,W_d,W_d/d). For s>=a*beta,pointpart also has smooth bounds.

- FixedS,sufficiently largebeta;G=beta^-1/(Dstar+r),W=beta^-1/(Dstar+r)^2,P_d=d^-3*(1+r/d)^-12,W_d=d^-4*(1+r/d)^-12. Bounded-distance differences include same-site slotdifferences.
- Free v=(1/ell)sum_(n>=1)p_(n beta),c=(1+v(x))^-1,h=c*chi*(eta+v),0<=h<=1. Keep ALL positive periods; ell*v(x)=n_sw exactly.
- Uncutv need not lie inl2;define it by pointwise positive convergent series. Trial/restricted finitecubeprofiles have finite support. Smoothpart is seam-invariant;pointslotseam changes obeydifferencebound; each traversal contains seam exactlyonce.

来源：`math/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/04-profiles.tex`，lem:freebounds statement lines[116, 136];complete containingmodule/definitions/proof actuallyreread。

## CLM-271-CORR-LEM-SIGNEDSOURCE — 孤立轨迹的带符号源守恒

The total SIGNED assigned source mass on directedblock[u,v] equals phi_v(Z_v)-phi_u(Z_u)+integral gamma_s(Z_s)ds.

- Fixed pictureinG,isolated obstacle strand starting aboveB_4R,oneblock,either profilepart,eitherelapsed direction. Profiles evaluated FULL before restrictiontoholes;gamma iscutoffcommutator.
- Includes removed-edge,forcedholetransport andassigned seam sources withspecified endpoint sides. Identity is for net signedmass,not totalvariation.

来源：`math/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/05-sources.tex`，lem:signedsource statement lines[98, 110];complete containingmodule/definitions/proof actuallyreread。

## CLM-271-CORR-LEM-CANCELLATION — 区块源总变差与孤立净质量分开

One strand source is supportedwithinCL of itsanchor,hasTV<=C*L*Wcal(anchor); ifisolated,its signednetmass<=C*L^(3/4)*Wcal(anchor).

- OnG,blocklengthL..2L,anchoraboveB_4R. SmoothWcal=W. Pointprofile usesW_d onlywhendcomparablethroughblock andinf d>=L.
- Pointprofileinsecondelapsedhalf also usesW;sumofpartsallowed. Earlypointtimesdo NOT automatically satisfyblockcancellation and instead needbin/diffusionarguments.
- Smaller signedmass comesfromendpointdisplacement andtime/cutoff/seamterms;TVstillcountsalljumps.

来源：`math/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/05-sources.tex`，lem:cancellation statement lines[148, 167];complete containingmodule/definitions/proof actuallyreread。

## CLM-271-CORR-LEM-SOURCEBINS — 短时间分箱的源总变差

Inone directedbin,theassignedsourceTV<=H_beta*(W+W_d)(anchor),d=sqrt(1+s);sourcesites withinC*log(beta)ofanchor.

- OnG,binlength1..3,anchoraboveB_4R;eachprofilepartseparatelyusesitsownweight. H_beta isafixed logarithmicpower,notuniformarbitrarypower.
- No signedcancellationisclaimedforthese earlybins;supports/timeweightsvarybyatmostcontrolledlogfactors.

来源：`math/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/05-sources.tex`，lem:sourcebins statement lines[212, 221];complete containingmodule/definitions/proof actuallyreread。

## CLM-271-CORR-LEM-DUHAMEL — 严格切片次序的双源Duhamel恒等式

<mu_plus,h>=integral<s_plus(ds),bbar_s>+doubleintegral_(s precedes t)<T_(t,s)s_plus(ds),s_minus(dt)>.

- Sources arecontinuousgenerator-minus-profileerrorsandatomicK*phi_minus-phi_pluserrors. Reverseatomsarebeforetheoperationinforwardphysicaltime;profilesretainbothsides.
- Strict insertion-sliceorder excludes theforward/reversepairfromtheSAMEoperation. ForatomicpairsT runsafterthefirstoperationtobeforethelaterone. No doubleseamcrossing or same-operation diagonal term.
- Purefinite linear telescoping/variation-of-constants identity;doesnotrequire reversibility orindependentsourcecollections.

来源：`math/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/05-sources.tex`，lem:duhamel statement lines[267, 281];complete containingmodule/definitions/proof actuallyreread。

## CLM-271-CORR-PROP-SCALAR — 真实钉扎律下的标量绝对残差

E_P[1_G*|<mu_plus,h>|]=o(beta^(-5/2)),uniform ineligiblefinitecube,deterministicpinsandinjectionslot.

- FixedS,scales,interior/no-pinball andactualP=E union{i} exposurelaw;absolutevalueisINSIDE expectation.
- Uses signedisolated cancellationinthecentralinterval,binboundsnearendpoints,cutoffcommutator,two-source orderedidentity,heatdecay/localizationandtwo-timeboxCauchy-Schwarz. No independence ofobstacles across times.
- Smallestgainsinclude L^-1/4=beta^-1/800. This isasymptoticexpectedcontrol,notanexplicitfinite-betaerrorcertificate or deterministicpointwisebound.

来源：`math/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/06-scalar.tex`，prop:scalar statement lines[11, 20];complete containingmodule/definitions/proof actuallyreread。

## CLM-271-CORR-LEM-BOXMOMENT — 无需跨时间独立性的盒二阶矩

For deterministicfinite-supportw>=0,A_Q=sum_(obstaclesinzQ)w(z),sqrt(E sum_Q A_Q^2)<=C*(sqrt(lambda)*||w||2+lambda*sqrt(sum_Q(sum_(zQ)w(z))^2)).

- One deterministicslice,cubesofsidecomparableF>=1,slotmultiplicityincluded;lambda=beta^-3/2. Same-slotanddistinct-slottermschargedseparately.
- Products of anchor sums at two deterministic slices withdistance<=CF are boundedbytheproductof their ownRHSsusingCauchy-Schwarz. No joint-time independence law isneeded;sitecounts preservedacrossseam.

来源：`math/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/06-scalar.tex`，lem:boxmoment statement lines[139, 157];complete containingmodule/definitions/proof actuallyreread。

## CLM-271-CORR-PROP-DUALENERGY — 两个方向的统一测试类能量残差

OnG,|<mu_d,y>|<=X_d*sqrt(e_y)+C0*rho(beta),d=+,-;E_P[1_G*(X_plus^2+X_minus^2)]=o(beta^(-5/2)).

- Everyrealcuty vanishingonkillingcoordinates with||y||infinity<=C0. MeasurableX_d>=0 dependonexposurebutNOTonyorC0;rho deterministicrapidlysmall. Countingoneperiodenergye_y=<y,(I-U)y>.
- FixedS,eligibleinterior/no-pinball andscales. NotpointwiseX_d=o(beta^-5/4),notonlyanexpected signedpairing,andnotaforward-onlycertificate.
- Proofsharesatmost2e_yacrossdisjointnext-blockwindowsintwoperiodcopies,withseparatefinalblockcorrectionK_n. A naivemultiplier equal tothenumberofblocks isnot the statedestimate.

来源：`math/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/07-energy.tex`，prop:dualenergy statement lines[14, 37];complete containingmodule/definitions/proof actuallyreread。

## CLM-271-CORR-LEM-BLOCKFLOW — 一个区块的局部与净质量流预算

Localizedpropagatedsource atany fullyregularsliceofnextblockhasflowenergy<=F_j=C*(L^6Q_j+L^2C_j+L^2*b_star^2*R^5),up torapidlysmalll1loss;final-cutlocalizedmassnorm2^2<=K_n=C*L^5*(Q_n+b_star^2R^3).

- Firstsourcecollection:cutoff+smoothobstacles+pointobstaclesinsecondelapsedhalf,onG. Q_j=sum W(anchor)^2;C_j=sum theta_alpha theta_alphaprime W*Wprime/(1+anchorseparation),theta=L^-1/4ifisolated else1;b_star=beta^-1R^-3.
- E[1_G F_j]<=C*(L^6*lambda*beta^-2/Dstar+L^2*(L^-1/2*lambda^2+L^3*lambda^3)*beta^-2R+L^2*b_star^2R^5). Onlyone-time snapshotboundsareused.
- Nextblockoflastblockisinacopiedperiod. Routesusefullregularity,available localpaths andflows toinfinity;nonzeronetsource mass isallowed. Flows neednotbechosenmeasurablybecause coefficientsarefinite snapshotbounds.

来源：`math/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/07-energy.tex`，lem:blockflow statement lines[118, 144];complete containingmodule/definitions/proof actuallyreread。

## CLM-271-CORR-LEM-EARLYSOURCEENERGY — 早期点源的二阶矩与后段扩散

Forpoint-profileobstaclesourcesatelapsed[0,beta/2),theirprepropagationTV M hasE_P[1_G M^2]<=H_beta*beta^-3/2;onG |<mu_early_d,y>|<=C*M*beta^-3/4*sqrt(e_y)+C0*rho(beta).

- Testvectorsaretheboundedrealcutclass,notavector-dependentchoiceofM;eitherdirection. Sourcevariationusesbins,notunavailableearlyblockcancellation.
- ProofusesMinkowskiforsnapshotswithnoindependence;propagatesforatleastbeta/4tolastquarterandaveragesoverfullyregulartimes. Heatboundandsubstochasticitygive massspreadbeforeflowpairing.
- The referenceddual-energypropositionidentifiesONLYthetestvectorclass;thislemmasproofdoesnotassumethedual-energyconclusion ithelpsprove.

来源：`math/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/07-energy.tex`，lem:earlysourceenergy statement lines[369, 382];complete containingmodule/definitions/proof actuallyreread。

## CLM-271-CORR-LEM-SURFACECOST — 全时边界钉扎的表面压强代价

0<=p_N(t)-p_N_plus(t)<=(log2)*(ell/beta+24ell^2)*|innerboundaryLambda|/volume;hencep_N_plus(t)->p_S,beta(t).

- Everyfinitebeta>0,t>=0,finitecube;ell=2S,fixednormalization. Thisisapressureboundatfixedparameters,notuniformconvergenceofitszero-fieldderivatives.
- Usesfieldtiltedcycleweight andPoissonmarkinsertionbound4;all-timeboundarycyclescountedbyboundaryslotsplusincidentmarks. Volume limit stillprecedesfieldderivative.

来源：`math/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/08-pressure.tex`，lem:surfacecost statement lines[102, 111];complete containingmodule/definitions/proof actuallyreread。

已有通用容量引理 `CLM-271-CORR-CAPACITY` 原字节保持；上述物理比较依赖它，但孤立源/热核改进不自动变成该通用零件的新前提。

来源账本：`data/provenance/readings/F-271-correction-claims-WP129.json`。只有选定证明使用接口，历史原作、完整依赖审核、人审/第二供应商仍缺；不以23条登记数代替完整研究。
