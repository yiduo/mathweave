# F020：真实模重构消费者的有界准入核查

由规范来源记录 `data/provenance/demand/F-020-modular-consumers.json` 及图谱导出。

三个固定项目，10源码／许可文件572605字节，实际选读3863行。未运行这些软件、数值或符号实验。无新候选或初检，APP02001仍待定。Sage与Singular是关联调用层／引擎，不是独立供应商复核。

## 实际文件与阅读范围

| 项目／文件 | 固定提交 | 实读范围 |
| --- | --- | --- |
| sage / COPYING.txt | `601df58edafe95f68597b9dec61e0a75adca8983` | [[1, 105]]；105行 |
| sage / src/sage/rings/polynomial/multi_polynomial_ideal.py | `601df58edafe95f68597b9dec61e0a75adca8983` | [[447, 529], [1353, 1505], [4280, 4425], [4660, 4850]]；573行 |
| sage / src/sage/libs/singular/function.pyx | `601df58edafe95f68597b9dec61e0a75adca8983` | [[1, 110], [1199, 1355], [1730, 1876]]；414行 |
| singular / COPYING | `b501ac240eec83597514c6223a6413790049ef46` | [[1, 118]]；118行 |
| singular / Singular/LIB/modstd.lib | `b501ac240eec83597514c6223a6413790049ef46` | [[1, 190], [275, 535]]；451行 |
| singular / Singular/LIB/modular.lib | `b501ac240eec83597514c6223a6413790049ef46` | [[1, 548]]；548行 |
| singular / Singular/LIB/moddiq.lib | `b501ac240eec83597514c6223a6413790049ef46` | [[1, 322]]；322行 |
| sympy / LICENSE | `cd86f04255d9411f11f32108cfa4ef773e4f401b` | [[1, 153]]；153行 |
| sympy / sympy/polys/modulargcd.py | `cd86f04255d9411f11f32108cfa4ef773e4f401b` | [[1, 1008]]；1008行 |
| sympy / sympy/polys/rings.py | `cd86f04255d9411f11f32108cfa4ef773e4f401b` | [[2810, 2980]]；171行 |

## 输入输出与失配

| 接口 | 输入／输出 | 必需条件与未准入点 |
| --- | --- | --- |
| SAGE-GB-OUTPUT | Polynomial ideal,base coefficient domain,term order,algorithm andoptional degree/multiplicity controls → Immutable polynomial-basis sequence withselectedbackend sorting/field normalization | SelectedgroebnerAPI andbody only;bounds maytruncate output,cache regeneration matters forfuturefairbenchmark；Not an explicitfixedfiniteZpointsetS,completeQevaluationkernel orwhole-state stability certificate. No explicitmodStd-producingcaller identified. |
| SAGE-NATIVE-DISPATCH | Sage objects/ideals andexistingorloadedSingular function name → Typednative ring/argumentcall andreturned result;lib canloadfunctiondefinitions | Externalprocessraw whitelist anddynamicnativefallback differ;librariesmustbeavailable;no installationorcallperformed；MissingmodStd inmenu isnot proofnativecallimpossible;dynamicloadingalone isnot actualF020consumer orvalidity certificate. |
| SINGULAR-PRIME-LAW | Characteristic-zero command/arguments,primefilters andfinitepmax → Sequential3-prime orresource-dependentparallelbatches,CRT/Farey loop andseparaterandompTest | Primecandidates descend withfiltering;earlyretry/stabilization andglobaloptions retained；Notuniformlength overT0consecutiveintegers thenuniformsubset;no fixeddepthall-failure-pathcontract orfiniteF020riskbridge. |
| SINGULAR-LUCKINESS | Inputcoefficients andmodularstandardbases → Discardinputbadprimes andallbutlargestleading-idealcategory | ReadmodernprimeTest_std anddeleteUnluckyPrimes_std;unreadlegacycompatibilitytail notcovered；A commonleadingideal/category doesnot identify same-S nestedcompleteQevaluationkernels orforcealllaterstatesidentical. |
| SINGULAR-CERT-SCOPE | modStd exactness flag,globalprobabilisticoption,inputideal andliftedcandidate → pTest plus selectedfinalcallback accordingtoactualsettings | Genericmodular defaultcallbacks accept;probabilistic skipsfinalTestonly. modStd finalchecksIincludedinG andGbeingGB;selecteddocs retainhigh-probabilitygeneralcase andspecialhomogeneous/localconditions；Do notcall allreturnsideal-equalitycertified orassumeallfalseaccept0;no kernelproof/runtimevalidation ornewbugclaim. |
| SINGULAR-IDEAL-CALLER | RationalpolynomialidealsI,J forquotientorsaturation → modQuotient/modSat routevia modStd andmodular callbackstoidealoperationoutputs | Quotienthasordinaryfallback;modpchecksincludebothdirections,finalquotientandsaturationcallbackscheckspecifiedone-sidedmultiplicativeinclusions；Actualmodularoperationconsumerexists,butcompleteF020kernel/path/risk/costpremises unestablished. One-sidedtestname doesnotcertifyallideal-equalityconditions. |
| SYMPY-MODGCD-STATE | Integerpolynomials f,g inonecommonring → ModularGCD APIsreturngcd/cofactorsaftercontenthandling,degreefilters,CRTstabilizationandtrialdivision | Selected1-1008lines;recursiveFp evaluation mutatesdegree/contentbounds,raisesfailureandresetsCRT. Primesnextprime,notvariableuniformblocks；Fp evaluationpoints varywithp;notfixedZ-S ornestedQkernels. Auxiliaryarithmetickernels/algebraicfunction-fieldtail unread;no resultorperformancewasexecuted. |
| SYMPY-DEFAULT-GCD-DISPATCH | PolyElement gcd/cofactors withZZorQQgrounddomain → Selectedringscallergcd→cofactors→_gcd;ZZtoheugcd,QQclear-denominators thenZZ | Observed2810-2980only;heugcdimplementation notreadorbenchmarked；Do notlabelstandalone modulargcdAPI asdefaultPolyElementGCDcallpath;actualdownstreamF020benefitconsumerstillabsent. |

## 零假设与停止决定

- Directsame-outputstandardbasis/quotient/saturationorGCDalgorithm,withdomain/termination/verificationconditionsexplicit
- ExistingLC/coefficientfilters,leading-idealmajority,degree-boundresets,CRT/Fareyandordinaryresampling
- Exactfinaloutputverificationonlywhenactuallyavailable;genericdefaultcallbacksorone-sidedidealtestsdo notestablishit
- SameinformationandfullcostincludingS,completeQkernel,patches,height/finitecertificate,primegeneration,modulararithmetic,failedretriesandverification

Threeprojectcapreached;do notspendremainingtwofilesasquota. No source-compatibleconsumeradmitted. Rotatealgebraic/complexgeometryF047/F053aftercurrentQA/storageclosure,asglobal040requires.

## 许可和范围

- sage: SelectedCOPYING1-105:wholedistributionGPLv3only,originalSageGPLv2-or-later,docsCC3BYSA,componentsseparate. Do notassumeallsourceApache.
- singular: COPYING118lineswhole:GPLv2orGPLv3,separatebundledcomponents.
- sympy: LICENSE153lineswhole:BSD3andlistedseparatelylicensedsubcomponentnotices.

只发布派生记录、定位与散列；第三方全文临时核查后清理。源方法、未建立前提和实际软件状态分别建图；不将API成功或模型判断计应用验证。
