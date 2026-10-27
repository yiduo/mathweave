# F047：线丛提升的 Picard 历史前提

WP118 专门补历史依赖。实际核对 Traverso 1970 原作的选定转换文字，以及 Stacks 四个官方条目的陈述和所显示的证明。没有新应用候选、数值实验、人审、形式化构建或完整成果族信用。

原稿 `04-bundle.tex:202–263` 使用 Picard 群在加一个变量下不变，继而构造规范线丛提升。此前 Traverso 和 Stacks 仅登记书目，本包保留旧记录后补记实际原始范围。

| 原始来源 | 已核对的范围 | F047 使用条件与边界 |
| --- | --- | --- |
| [Traverso Theorem 3.6](https://www.numdam.org/item/ASNSP_1970_3_24_4_585_0/) | 印刷页586引言的明确陈述、593–595页定理与选定证明文字；约化 Noetherian 环、有限正规化、至少一个的有限变量集下，Picard 不变性与半正规性的关系 | 光滑整仿射复簇的坐标环正则且正规，正规化就是自身，因此原有限性条件满足。不能省略这些前提而推及任意奇异底空间 |
| [Stacks 056S](https://stacks.math.columbia.edu/tag/056S) | 域上光滑蕴含正则 | 对 X 和 A1×X 使用；原条目同时说明局部 Noetherian 性 |
| [Stacks 0AG0](https://stacks.math.columbia.edu/tag/0AG0) | 正则局部环为 UFD | 结论关于局部环；不能误读为光滑仿射坐标环必然全局唯一分解 |
| [Stacks 0BE9](https://stacks.math.columbia.edu/tag/0BE9) | 局部 Noetherian 整概形的局部唯一分解条件，使 Picard 群与除子类群相同 | 正规性本身不够；稿件通过局部正则性满足更强条件 |
| [Stacks 00KV](https://stacks.math.columbia.edu/tag/00KV) | Noetherian 环中主理想的极小素理想高度至多一 | 稿中另外使用整环及非零元素，排除高度零，才能得到所需的高度恰为一 |

Traverso 原作转换文字共592行，本次实际读选定390行，未读的其余正文不计阅读信用。部分显示公式和图表提取缺失；引言独立明确给出定理3.6的映射及假设，但这不能替代完整证明审核。逆向刻画的证明选取一个变量，因此显式保留变量集非空；若变量集为空，恒等映射本身不能刻画半正规性。F047恰使用一个变量，此限定不改变实际准入。初版转述已归档，补充说明见 `F-047-Picard-scope-addendum.json`。原作在正规基例援引已知结果，并使用 Bass–Murthy 的相对 Picard 工具；Endo、Bass–Murthy、Bourbaki、EGA 及未完整核查的内部引理仍是开放的递归输入。四个 Stacks 页面所引用的下层引理也没有全部跟进。

图谱分别记录两条适用范围一致的 Picard 前提路线：Traverso 的正则特例，以及稿中给出的除子论证与四个已核对的原始前提。它们仅支持同一个 Picard 步骤；没有宣称两条路线的证明输入独立或已获接受。单条路线变化不会自动使另一条失效；两条均受影响时，依赖复查传到 Picard 步骤和原线丛命题。

Picard 前提不等于完整规范提升。单位、多参数 cocycle、赋值兼容性仍需分别处理；一般自然语言提升命题与实际 Lean 的不变倍数及最高分量路线也保持区分。原来源等级不变，完整依赖链仍未知。

选定原作检查从此前2/26个历史根扩为4/26个，Stacks 限四个条目。其余22个根及已选来源的递归证明依赖仍未闭合，不能计作完整历史谱系。此前 Suslin TLS、BCW403 的失败证据保留，未在相同条件下重试。

获取原始文件共1,119,546字节，包含 Numdam 入口、原作及四个 HTML 页；保存原文件和转换文字的散列。Numdam 原作及正文不重新发布；第三方临时文件核散列后删除，只保留自有转述、范围、版本与出处。Stacks 是本次观察到的官方页面版本，不冒充2026年9月23日的历史网页快照。

规范依据：`data/provenance/readings/F-047-Picard-history.json`、`data/graph/nodes.jsonl` 和 `data/graph/edges.jsonl`。四条旧记录归档于 `data/graph/history/GEN-20261027-115-before.json.gz`；完整质量和压缩清理状态以本包最终收据为准。
