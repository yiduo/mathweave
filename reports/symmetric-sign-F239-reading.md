# F239：对称随机符号矩阵的渐近率与迁移边界

由规范阅读台账 `data/provenance/readings/F-239.json` 和图谱导出指标汇总；完整族、历史闭包和数学审核均未完成。

两篇当前手稿全部24TeX／8083行（含278行参考文献与三份TikZ图源）及两份README实际读完。68个手稿限定的结果绑定、16个方法契约入图；其中包括旧定理重述和伴随稿复用，不是68个独立新定理。源码结果、方法、版本与图谱的逐项入口见 [规范族报告](families/F-239.md)。

## 决定应用边界的区别

- 均匀稿给出2^(-n+o(n))，偏置稿对每个固定p给出奇异概率的n次根极限p²+(1-p)²；不是有限维显式失败预算，也不支持任意p(n)。
- 独立的是含对角的上三角条目，不是整行。无偏符号到比特的降维与有偏锚行条件化分别处理；图的固定零对角、正定约束和固定度数模型不能直接替换。
- 逆矩阵的双线性限制秩、实际逆向量范数门槛和最小奇异值是不同输出；概率非奇异并不保证数值好解。
- Reverse Minkowski需要每个子格的行列式下界；极值子格、低高度覆盖和同一次典型事件下的自适应格选择是不同条件。
- 主路径的两稀有事件通过条件概率逐步计价，相邻步骤没有被假称独立。没有运行小矩阵频率来验证渐近锐率或制造应用初检。

## 原始历史范围

本包只核对下列四部作品的选定范围。其他24部外部根正文及递归历史仍未读完。

- [reverse-minkowski-v6](https://arxiv.org/pdf/1611.05979v6)：arXiv1611.05979v6,7Jul2022;numbering distinguished from2024Annals。Extracted lines58-145 and1320-1420;PDF2/3 actually viewed. Theorem1.2 requires det(M)>=1 for every sublattice M, not only totaldet. Scaling yields T/[10(log j+2)] mass<=3/2. Corollary1.4 shifted count has stated radius ranges. Existential quotient minimizer does not establish computation cost.

- [cjms-v2](https://arxiv.org/pdf/2105.11384v2)：arXiv2105.11384v2,8Jun2021;not read as2025JAMS finalbytes。Extracted lines1-150;PDF1/3 actually viewed. Theorem1.1 already gives exp(-cn) for uniform symmetric signs. The sharp exponent constant is not supplied by that statement. The independent-entry sharp-rate discussion is a distinct model; least-singular-value extension is deferred there.

- [talagrand1988](https://www.ams.org/journals/proc/1988-104-03/S0002-9939-1988-0964871-7/S0002-9939-1988-0964871-7.pdf)：PublishedProcAMS104(3),1988,905-909。Fullfive-page extracted text read;PDF2/4 actually viewed,printed906/908. Theorem3 controls a convex Euclidean-Lipschitz function on uniform signs about its median:4exp(-t^2/(8sigma^2)). Convexity is essential. F239 integrates the tail and changes constants to center at the expectation.

- [talagrand1994-v1](https://arxiv.org/pdf/math/9406212v1)：arXivmath/9406212v1,7Jun1994;1995publication scan not downloaded。Selected product notation lines425-440 and section4.1 lines2717-2867,plus introductorycontext;PDF50/51 actually viewed. Theorem4.1.1 controls convex distance in a product space with exp(fc^2/4) integral <=1/P(A). The read version uses common-product notation. The p-or-(1-p) bit arrays needed here reduce to a common Bernoulli law by fixed coordinate complements, preserving convexity and Euclidean Lipschitz constants; this is a local inference, not human approval of arbitrary distributions.

两稿的`Talagrand`同键实际是不同作品：1988年均匀立方体凸Lipschitz定理与1995年产品空间论文。后者本包实际读1994年作者版本；1995年扫描PDF的Content-Length为11153316字节，超过余下预算，在读取正文前拒绝。没有将作者版内容冒充出版版全审。总成功下载2797578字节；八页实际PDF像素已查看。

## 形式化与研究状态

固定CONTENTS的F239没有Lean链接，形式化登记未见两稿匹配条目，docs239不存在；有界challenge文件名检查没有找到对应端点。名称含239或Symmetric的无关文件不充证据。全部68绑定保守C／完整链未知；不把有界检索当全库证明不存在，也没有构建Lean或Comparator。

十领域和F174／F131／F238三组跨族映射保留具体条件缺口。没有准入新的可检验增益假设，候选仍44、初检13、不同假设13，5限定支持／8不利。没有人审、第二供应商或试点升级。

## 回归与恢复

69核心检查已通过；12项新旧依赖路由、完整JSON／GraphML对象一致、来源散列／外键／状态闸门和15归档267源码成员散列通过。所有4627旧规范行、全部旧边、旧代码／测试／实验／语料与52旧族报告保留。

全图7689节点／21698关系；4741规范记录、8357来源注释（8347核心）。58阅读族、53当前源码草稿、1530标签另4无标签，完整族／谱系仍0。

实际运行周2026-W44已抽取5%：APP-119-01, APP-231-01, APP-374-01；仍待真人，事实错误率未知。

第一次完整检查在报告渲染处发现新分析记录缺少既有报告字段；保留精确v1后，在v2添加手稿限定书目别名和无形式端点的说明。没有改测试／验证器或科学断言。另补六条实际高斯计数依赖。两次结果及日志全部保留。

无math干净目录与最终压缩清理的确切结果见同目录质量／存储收据，不用完整性校验代替科学重放。本包不重放未变的实验，不推送GitHub。下一包有界核对真实对称离散矩阵消费者；若精确集合、对角、固定偏置和所需输出不匹配，保留缺口并转向F238未读伴随稿，禁止继续扩大已知小矩阵网格。
