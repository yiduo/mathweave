# F181：原始历史范围与旧方法对照

由规范文献节点、ANALYSIS-F-181与WP128后续阅读账本导出。此报告不计新应用卡片、初检、完整成果族或完整历史谱系。

此前核对4部原作的选定范围；本包新增4部，合计8/11部。Lovasz仅核对原作术语，数值公式未核实；AH与Pyber原作正文仍缺。旧账本保持不变，新观察单独版本化。

| 原作 | 已读范围与作用 | 保留的限制 |
| --- | --- | --- |
| BKS2012 | arXivv1 pp7-8 Claim2.2/Lemma2.3, actual statement and selected full proof; model definitions pp2-3；Directed path of edge length at least2t-4k+3; DFS stack contains at least2t-4k+4 vertices. | A directed path is not an undirected simple cycle. No general digraph resilience or whole main proof review; not a mandatory proof input to the self-contained F181 lemma. |
| KKS2015 | Published pp857-859 Theorem1.1,Corollary1.2,definitions and proof outline; main theorem proof not read；Edge partition into odd(G)/2+np/2+o(n) cycles and single edges. The n/4+np/2+o(n) corollary also needs p<1-omega(1/n). | No deterministic arbitrary finite graph guarantee,effective n0,or implementation runtime. Do not replace odd(G)/2 by n/4 arbitrarily near p=1. |
| AABC2025 | arXivv2 pp1-4 definitions,Theorems1.3/1.5/1.7 and selected1.3 proof; pp9-10 Theorem5.1 and selected1.7 proof；Theorem1.3 f_ce<=n-1 for maxdegree<=4; Theorem1.7 g_ce<=n-2 for a graph that is not a tree. f_ce partitions cycles/edges; g_ce covers and may repeat edges. | Overlap cover is not edge partition; a 2-regular subgraph need not be one simple cycle. Source positive-order qualification retained. Theorem1.7 invokes Fan and3.1; original Fan and full3.1 proof remain outside this reading. |
| Krivelevich2019 | arXivv2 p2 Theorem1;pp5-7 Propositions2.1/2.2 and DFS;pp7-8 full selected Theorem1 proof；A simple cycle of length at least t+1. | External neighborhood convention differs from F181 N(U) before subtracting U. No claim about general cycle decomposition,finite C,fast optimization,or applications sections not read. |

仅阅读转换文字。四部PDF和转换文本均有独立SHA256；LF行号按`nl -ba`定义，下载脚本的`splitlines`计数还拆分了换页符，两种口径已明确区分。版本以实际页眉/页脚和下载地址记录，不能将arXiv生成日期、提交版本、刊年或作者PDF当作同一字节制品。

## 适用范围如何改变判断

BKS的双向邻接条件产生有向长路径，不能直接当作无向简单环。KKS的独立边随机图与高概率渐近计数不是任意有限图保证；接近p=1时不能无条件把奇度项替换为n/4。AABC把允许重复的覆盖、互斥边分解和2-正则子图分别计数；一块2-正则图可能含很多环，删除覆盖中的重复边也可能破坏环。

AABC的1.3和1.7证明选段已读，但没有完成递归证明审核或数学接受。其Eulerian要求连通且偶度，F181与KKS只要求偶度，迁移时必须对照实际定义。原作1.7的非树范围还包括多分支森林；F181仅引用含环子集，不将较宽原作范围改写成源定理。

## 旧局部扩张结果已足够

F181的引理在足够大u、alpha=(1/32)/log₂²u、每个0<|U|≤u/2有至少alpha|U|个外邻居时，给出长度大于alpha²u/100的简单环。Krivelevich旧定理只要求整数k>0、t≥2、图阶>k，以及每个k/2≤|W|≤k的集合有至少t个外邻居，结论为环长至少t+1。

静态代入k=floor(u/2)、t=ceil(alpha*k/2)，对足够大u有t≥2。源扩张假设覆盖该区间，整数外邻居数至少ceil(alpha*k/2)。旧定理给出至少ceil(alpha*k/2)+1；又k≥u/3且0<alpha≤1，所以这一界大于alpha*u/6，强于源引理的alpha²u/100。

这只是原稿已经引用的旧结果的适用范围比较，不是项目新定理或数值实验，也不说明旧方法独自解决完整Cn分解或给出实用运行时间。源引理字面陈述、C级和未知完整依赖链保持；图中旧准则连为历史对照，没有误加为自包含DFS/bypass证明的强制依赖。

## 尚未核实与复现

- Lovasz：缓存的作者原作转换文本明确有限简单无向图、边不交与简单路径；原Theorem1数值公式转录损坏，原PDF散列未知，不从后来重述补记原作精确界。
- AH：出版社PDF入口实际回到摘要页，作者主页403；没有核对原作正文。F181的有界秩、每个非空指标集合与严格匹配不等式、每个边出现的私有填充顶点单独保留。
- Pyber：出版社正文不可得，作者主页发现的真实出版列表返回403；不将后来论文的引用当作原作证明阅读。
- 所有递归历史、真人规格/分级与第二供应商复核仍未完成；没有Lean构建、Comparator或工程试点。

规范依据：`data/provenance/readings/F-181-history-WP128.json`，文献/比较节点位于`data/graph/nodes.jsonl`。最终图谱、来源、版本、传播、导出、核心/干净目录、代表归档重放与压缩收据见`reports/reproducibility/20261027-F181-history/closure.json`；闭包存在前本包未完成。


WP128与全局045最终闭包（2026-10-27T10:35:58.870542+00:00）：新增四原作选段，F181为8/11选定原作；另Lovasz原作仅术语，AH/Pyber正文与Lovasz精确界、递归历史仍缺。旧局部扩张准则已足够且更强，不宣称新数学或完整Cn分解/运行时间。GEN125新增3规范8显式边，9旧记录版本化、5615旧行与1327保护文件保持；两初版标题纠正留档。完整图8874/26094、9845核心来源、9858全审计/2090来源制品，181单种子2多种子/完整导出，18科学归档378源码，本地95/无math干净95无跳过通过；F149支持与F325不利代表完整raw/summary源码重放、原资源通过。原作临时制品与自有辅助均按本包storage收据核散列压缩/清理。64阅读59草稿、47候选15初检15不同7限定支持8不利、另1诊断保持；完整族/历史/人审等仍0。计数归零，下一WP129四篇F271实际源文预算，正文阅读信用0，不推GitHub。
