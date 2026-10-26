# F239：真实软件分布、输出需求与条件性秩风险接口

2026-10-26 · WP109。由规范图谱节点与其散列绑定的需求台账导出；不是完整成果族研究、应用初检或人审。

三个固定原始项目、17份源码／文档／许可文件，下载 394010 字节，实际选读 2522 行；完整下载不等于完整阅读，没有执行这些软件。恢复时沿用已获取的散列一致来源，没有新增下载或数值实验。

## 已核对的输入与实际调用

| 项目 | 固定版本 | 实际输入／输出 | 本包结论 |
| --- | --- | --- | --- |
| jcmgray/quimb | `1b64353d9e562529694e71abf40a2861ee8dcdfa` | Tensor contraction/permutation invariance in inspected caller | Retain conditional rank-risk metadata mapping;consumer and incremental benefit unqualified |
| JuliaMath/RandomMatrices.jl | `0fde454787f3ccbfcef251e383c12ceb9b80380c` | Continuous Gaussian random matrices/eigenvalues | Does not match selected discrete ensemble;no universal library absence claim |
| reservoirpy/reservoirpy | `1fc11351bfba7f4b9a35464a1b99d804a5d6ccea` | Recurrent matrix-vector dynamics with optional eigenvalue-radius scaling | No mirrored symmetry or inverse demand established;rectangular input and conditioning/eigenvalue targets kept separate |

quimb 每个坐标多重集调用一次标量填充。只有明确指定的实数两索引、Rademacher、loc=0、scale=1、标准填充、保留随机对角时，才对应 F239 无偏模型；概率仍以理想 IID 抽样为前提，不是对有限 PRNG 的独立性认证。普通开边界二维格点的角张量有两个索引，其他边／内部通常为三／四索引。实际已读测试使用 normal 默认值，只检查收缩与置换不变性，没有可逆性请求。

均值平移、自定义填充、复数四相位、固定图对角与高阶展平分别改变前提。MPO 的 Hermitian 加法对称化也不是同一上三角符号分布。偏置接口没有在所选 quimb 标准 Rademacher 工厂中建立；不能把 F239 固定偏置主定理直接套入。

## 保留的候选与尚缺的价值检验

[APP-239-01](cards/APP-239-01.md) 保留为近类比、候选、待定：若消费者必须保持该离散初始化律并要求所选两索引映射可逆，可探索锐渐近精确秩风险作为决策元数据。具体消费者尚未建立。源定理给出 `2^(-D+o(D))`，没有有效有限 D 阈值、条件数、收缩精度或运行收益。

For a consumer that must preserve this raw symmetric-sign law and requires invertible two-index maps,sharp asymptotic rank-loss metadata could improve a predeclared initialization/risk decision beyond old exponential metadata or direct screening. No magnitude or finite-D benefit is established;the actual decision,utility metric,finite-D validity and threshold must be independently frozen before any run. The source-only prediction is -log2(P[exact rank<D])/D ->1,which is not itself an application-value test.

两位隔离 OpenAI 角色都支持窄条件保留。辩护者重视已实现的分布映射；怀疑者强调实际可逆性需求和增量决策价值仍缺，高阶展平可能因重复行退化。完整输出与冻结输入位于 `data/provenance/reviews/APP-239-01-isolated-roles.json.gz`。这是同供应商辅助自查，精确后端未知，不是外部检验或真实人审。

源码中的 sign-to-bit Schur／合同变换属于证明接口，维度 D→D−1；不作为已实现的初始化优化，也不从此导出更快的拒绝采样。

## 强旧基线与零假设

- Exact algebraic rank screening/rejection answers invertibility for each realized integer sign matrix;charge generation and rejected attempts,not only accepted draws.
- Tolerance-aware SVD/QR and least-singular-value criteria address numerical stability if that is the actual request;exact nonsingularity is not an equivalent output.
- Old CJMS exp(-cD) already gives exponential decay for the same uniform symmetric law;source-selected2021v2 scope retained separately from2025 publication bytes.
- Guaranteed-invertible orthogonal/unitary or structured choices only when a changed initializer law and its different symmetry are permitted by the consumer.

零假设仍是旧方法已满足实际输出，锐渐近指数没有改变有用决策。先确定精确秩、数值稳定性或谱半径中实际要哪种输出，再比较同输出的完整成本。没有实际任务、独立裁判与预先冻结的有限维阈值，不运行小矩阵频率作为渐近定理或应用有效性的证明。

## 未完成项与停止决定

- No inspected caller requires invertibility of the qualified raw two-index matrices;quimb actual selected test uses normal law and contracts tensors.
- No fixed operational D range,number/selection of matrices,allowed failure probability,loss/cost,seed policy or law-preservation requirement supplied.
- No independent finite-D bound/calibration,domain judge or same-output costed benchmark admitted. Asymptotic rate cannot select a finite rejection budget.
- Higher-order permutation-symmetric tensor flattening need not have independent upper-triangle entries;duplicate-row flattenings can be singular. No blanket TN-network guarantee.
- Julia selected Wigner implementation is continuous Gaussian. ReservoirPy selected Bernoulli shape/sparsity/recurrent output is not a mirrored symmetric sign model;changes cannot be hidden under the same name.
- Source C/full dependency chain unknown;both isolated roles are same-provider auxiliaries. Human classification/specification and independent provider remain pending.
- Small-matrix frequencies or successful metadata parsing would not count as application-value evidence. No numerical/symbolic experiment was run.

Three-project cap reached;stop expanding similar libraries. Finish package QA then rotate towardF238 unread companions/other lowcoverage before retro039.

本包新增一条条件候选，初检仍13项，五项限定支持／八项不利；没有新增有效线索、独立假设验证、人审、第二供应商复核或试点。58阅读／53源码草稿与 F238 的4/12篇范围保持。GitHub 本批之后不例行推送；公开8700f8b仅包含当时未完成日志，当前规范增量本地保存。

## 实际阅读定位

| 来源节点 | 文件 | 实际范围 | 文件 SHA256 |
| --- | --- | --- | --- |
| `LIT-239-QUIMB-LICENSE` | [jcmgray/quimb / LICENSE.txt](https://raw.githubusercontent.com/jcmgray/quimb/1b64353d9e562529694e71abf40a2861ee8dcdfa/LICENSE.txt) | 1–13 | `e708fa9633397b771e5a7c14fc471e3b2185499e1820fe4b3c7837918918e621` |
| `LIT-239-QUIMB-BUILDER` | [jcmgray/quimb / quimb/tensor/tensor_builder.py](https://raw.githubusercontent.com/jcmgray/quimb/1b64353d9e562529694e71abf40a2861ee8dcdfa/quimb/tensor/tensor_builder.py) | 1–50, 140–240, 1592–1810, 1844–1930, 5258–5360 | `95da6ecd98e882a2611e721962399edf5ccd02b030176d790f975ed03c069ea7` |
| `LIT-239-QUIMB-RAND` | [jcmgray/quimb / quimb/gen/rand.py](https://raw.githubusercontent.com/jcmgray/quimb/1b64353d9e562529694e71abf40a2861ee8dcdfa/quimb/gen/rand.py) | 1–205, 245–373, 443–478 | `4aaa4831876a0ad550f3e51c82295fbc4ddc61303687515ba6e324b8f015df3c` |
| `LIT-239-QUIMB-ARRAYOPS` | [jcmgray/quimb / quimb/tensor/array_ops.py](https://raw.githubusercontent.com/jcmgray/quimb/1b64353d9e562529694e71abf40a2861ee8dcdfa/quimb/tensor/array_ops.py) | 351–372 | `46d700ec14d797a0cf67661e798c77fd9e8687e423dbd8ba2f8c04782e8a0ee9` |
| `LIT-239-QUIMB-TEST` | [jcmgray/quimb / tests/test_tensor/test_tensor_builder.py](https://raw.githubusercontent.com/jcmgray/quimb/1b64353d9e562529694e71abf40a2861ee8dcdfa/tests/test_tensor/test_tensor_builder.py) | 815–837 | `fa81e3efe960f441a815b6445444150db9b3d4b6b7e6507a8dc025d4655bc8ba` |
| `LIT-239-JULIA-LICENSE` | [JuliaMath/RandomMatrices.jl / LICENSE.md](https://raw.githubusercontent.com/JuliaMath/RandomMatrices.jl/0fde454787f3ccbfcef251e383c12ceb9b80380c/LICENSE.md) | 1–23 | `5c9d473ee9f07c7656a1436378cd012d8c434535c825cf0f1798efd628bc089e` |
| `LIT-239-JULIA-README` | [JuliaMath/RandomMatrices.jl / README.md](https://raw.githubusercontent.com/JuliaMath/RandomMatrices.jl/0fde454787f3ccbfcef251e383c12ceb9b80380c/README.md) | 1–92, 126–141 | `93c7738c924de59b8796a0ecc580dfc089df08972b72f23af06820ac720538da` |
| `LIT-239-JULIA-PROJECT` | [JuliaMath/RandomMatrices.jl / Project.toml](https://raw.githubusercontent.com/JuliaMath/RandomMatrices.jl/0fde454787f3ccbfcef251e383c12ceb9b80380c/Project.toml) | 1–26 | `e04d78d6e11950d3e9ea512a4b36a14681e9a2c4750337760d9ec18f08867415` |
| `LIT-239-JULIA-MODULE` | [JuliaMath/RandomMatrices.jl / src/RandomMatrices.jl](https://raw.githubusercontent.com/JuliaMath/RandomMatrices.jl/0fde454787f3ccbfcef251e383c12ceb9b80380c/src/RandomMatrices.jl) | 1–53 | `7784b7dee403ae5905701b1c1b4b6ae109c644d3f1fac165bb53f99589cce13d` |
| `LIT-239-JULIA-GAUSSIAN` | [JuliaMath/RandomMatrices.jl / src/GaussianEnsembles.jl](https://raw.githubusercontent.com/JuliaMath/RandomMatrices.jl/0fde454787f3ccbfcef251e383c12ceb9b80380c/src/GaussianEnsembles.jl) | 1–140 | `b2b0bf5cb513e307b726adb4074c3f848c7c968819fa1480ed678556ece5556b` |
| `LIT-239-JULIA-TEST` | [JuliaMath/RandomMatrices.jl / test/GaussianEnsembles.jl](https://raw.githubusercontent.com/JuliaMath/RandomMatrices.jl/0fde454787f3ccbfcef251e383c12ceb9b80380c/test/GaussianEnsembles.jl) | 1–65 | `a05935714d459e359ac6c3fcda9ecfcd11e8b1e7f9e8e19cf3f16cd11b07a36e` |
| `LIT-239-RESERVOIR-LICENSE` | [reservoirpy/reservoirpy / LICENSE](https://raw.githubusercontent.com/reservoirpy/reservoirpy/1fc11351bfba7f4b9a35464a1b99d804a5d6ccea/LICENSE) | 1–21 | `1c8e82b42d8a3eb1fcd0cb2fd5929b88db76f9a9defc5075bd81137562c52cef` |
| `LIT-239-RESERVOIR-MATGEN` | [reservoirpy/reservoirpy / reservoirpy/mat_gen.py](https://raw.githubusercontent.com/reservoirpy/reservoirpy/1fc11351bfba7f4b9a35464a1b99d804a5d6ccea/reservoirpy/mat_gen.py) | 143–330, 466–584, 727–797 | `953cee31a5ee7209df7aa3f6c9e1c5da272f418e87423f1380cb8038f8dee406` |
| `LIT-239-RESERVOIR-NODE` | [reservoirpy/reservoirpy / reservoirpy/nodes/reservoir.py](https://raw.githubusercontent.com/reservoirpy/reservoirpy/1fc11351bfba7f4b9a35464a1b99d804a5d6ccea/reservoirpy/nodes/reservoir.py) | 1–130, 145–250 | `82e97a95bc425094a49a3ee7573467e7c80c198b8965551bbd205958ed6d7078` |
| `LIT-239-RESERVOIR-OBSERVABLES` | [reservoirpy/reservoirpy / reservoirpy/observables.py](https://raw.githubusercontent.com/reservoirpy/reservoirpy/1fc11351bfba7f4b9a35464a1b99d804a5d6ccea/reservoirpy/observables.py) | 46–124, 484–551 | `75e3ab6e80c035757673c4f23f5f3818c2e2085ea12158399ee97791bc5b2a03` |
| `LIT-239-RESERVOIR-MATGEN-TEST` | [reservoirpy/reservoirpy / reservoirpy/tests/test_mat_gen.py](https://raw.githubusercontent.com/reservoirpy/reservoirpy/1fc11351bfba7f4b9a35464a1b99d804a5d6ccea/reservoirpy/tests/test_mat_gen.py) | 1–143, 164–217 | `4cbd68563f5d8b434a5a5dbb3aca34c33f3709269c6b84ad6f26a0ff9d0a7301` |
| `LIT-239-RESERVOIR-NODE-TEST` | [reservoirpy/reservoirpy / reservoirpy/nodes/tests/test_reservoir.py](https://raw.githubusercontent.com/reservoirpy/reservoirpy/1fc11351bfba7f4b9a35464a1b99d804a5d6ccea/reservoirpy/nodes/tests/test_reservoir.py) | 1–140 | `98538633e69888f4059a338fb6adc39ed990d6ac48161ba5cf368790e7fa9736` |

全量约束、外键、依赖失效、完整导出、归档回解及干净目录检查另见 `reports/reproducibility/20261026-symmetric-consumers/`。检查成功只表明记录和软件约束通过，不能替代应用或数学审核。
