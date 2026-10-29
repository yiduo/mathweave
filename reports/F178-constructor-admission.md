# F178：实际构图与共识实验准入核查

WP130。候选 `APP-178-01` 保持待定，未运行共识目标；原10%轮次收益和含构图总时间条件不变。来源为已固定的自然语言稿，完整证明链仍未知。本次是既有正文草稿的选定重读，不增加成果族阅读或初检数量。

## 实际执行链与成本

| 阶段 | 原文要求 |
| --- | --- |
| 1 | Early pairing minimizes discounted structural/trace/entry/row accounts over O_d(n^2) candidate pairs for O_d(n) steps while retaining both signed precisions. |
| 2 | Cleanup uses prescribed first stubs and eligible clean partners until l0, maintaining separation and analytic caps. |
| 3 | Separated boundary completes using one smoothly tapered stop reference and exact Woodbury continuation; phaseA reduces row energy before phaseB entry control; only final l3 stubs can be matched arbitrarily. |
| 4 | Exact repair needs confinement, all-vertex local mass and typical bulk blocks, then biased simultaneous switches and prime-field seed enumeration; final exact spectral certificate does not replace these stages. |

主定理固定整数d>=3、偶数n且n>=n0(d)，输出完整邻接表。渐近多项式承诺不等于有限规模预算。各阶段选择参数的先后次序、矩阵的对比子空间和同一冻结参考均需保留。

最大主参数的辅助点数为 ceil(10/(.03a))=3,333,334，a=10^-4；两个符号共6,666,668个参数实例，尚未计标签。这里只计算原文的固定 bookkeeping 数量，没有执行构图，也没有证明任何优化实现必然消耗某个内存或时间下界。

- O_d(n^2) pairing candidates times O_d(n) steps, with exact candidate inverses/statistics and account comparisons.
- Rational matrix dimension O_d(n), path recurrence O_d(logn), polynomial-bit determinant/minor arithmetic and discounts; exponent and fixed orders still require choices.
- Colorful bounded-treewidth DP on O_d(logn) vertices and exp(k)*k^O(logk)*logn hash family, not brute-force n^k embeddings.
- Repair rational inertia cutoff search; Bernstein degree ceil(n^(2(c+C))) for Lf<=n^c,target n^-C; fixed c,C not numerically instantiated.
- M=ceil(n^(1/3+10a)) vertex-disjoint switches; prime P~n^Cprime with Cprime sufficiently large; up to P^2 seeds and exact rational spectral verification per retained candidate.

最终精确证书是 Bᵀ(4(d−1)I−A²)B 正定，B列为ei−en；需另查简单性和正则性。证书属于旧线性代数，不能代替前面全部构造。缺失门槛、固定矩阶、误差/素数指数和完整实现逐项保留在规范账本。

## 同阶同度旧基线

Alon作者版本修订于2020-10-04，定理1.3和第3节给出固定d、epsilon>0和足够大可容许n的完整确定性构造；双侧界为2sqrt(d−1)+epsilon。读取了作者原文转换文字并固定散列，没有把摘要或检索结果当完整算法审核。

第3节取 r=ceil(2/epsilon)、s=2r+4，从n+u点近Ramanujan图H开始，u=o(n)，每个s邻域至多一个圈。引理3.1保证至少 |V(H)|/(2d^(2r+3)) 个可删点，邻域无圈且互相分离；删去u点后匹配其邻居，恢复同一度数并得到恰n点。有限输入仍需保证可删点足够及MOP构造的局部圈条件；MOP递归原作没有在本包直接审核。该旧方法是应比较的强基线，但本项目尚未找到其完整可运行实现或数值门槛。

对原计划的偶数n，nd奇偶条件满足；若epsilon<d−2sqrt(d−1)，旧绝对谱界也排除不连通与二分图。它不保证新稿的精确严格树阈值。两侧都必须计构图、验证及通信成本，不能以Theta(n)点替代n点。

## 为什么谱界没有自动给出10%收益

原工作负载是非惰性同步 A/d，不能改成惰性矩阵。最坏误差收缩率r=||A在1的正交补上限制||/d，ceil(log(delta)/log(r))只是充分轮次上界，不是平均观测。新稿的严格界没有固定余量；旧epsilon趋零时，上界包络趋于相同值。两条上界不能给出旧方法的实际下界，因此原10%预测仍需真实检验。

## 决策与重访

暂不启动共识目标，也不做旧小图校准或巨大渐近枚举。需先取得完整新/旧实现、数字化有效输入与预算、真实或明确合成的同阶同度同步工作负载，再另行冻结执行规格。候选保留，不形成正式否定；人工和第二供应商审核仍缺。

规范来源：`EXPLORATION-178-FINITE-ADMISSION`；账本 `data/provenance/readings/F-178-constructor-admission-WP130.json`；原计划 `experiments/plans/MAP-178-001.json` 字节保持。
