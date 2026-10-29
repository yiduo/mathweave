# MathWeave · 数学织网

[English overview](README.en.md) · [English charter](CHARTER.en.md) · [English progress](PROGRESS.en.md) · [中文纲领](722篇AI数学论文应用价值挖掘纲领.md)

**连接数学成果、历史方法与可检验应用的证据网络。**

研究单位是“成果族 + 历史谱系 + 应用问题”。项目使用固定来源、版本化知识图谱和可复现实验，保留适用条件、失败证据与审核缺口。第一阶段仍未完成。

仓库：[yiduo/mathweave](https://github.com/yiduo/mathweave)。本版整理至WP130构图准入审计、全局复盘047及F271修正稿23条命题／71条证明接口；球面稿30条仍未规范入图。实际远端提交、核验和CI见[发布状态](state/publication.json)。第一阶段仍未完成。

| 指标 | 当前记录 | 验收边界 |
| --- | --- | --- |
| 固定语料 | 372成果族、719篇当前手稿 | 登记不等于研究完成；历史722口径逐项核对 |
| 原文阅读与草稿 | 64族实际阅读、59族当前稿全文草稿 | 完整成果族、完整历史和六阶段完成均为0 |
| 知识图谱 | 9,065节点、26,681关系 | 保留来源与版本；图谱规模不代表数学或应用有效性 |
| 候选连接 | 48／500 | 十领域尝试与命题绑定不计候选 |
| 合格初检卡片 | 15／100 | 15个不同假设：7项限定支持、8项不利观察 |
| 其他检查 | 1项诊断、2项组件检查 | 不额外计入应用假设计数 |
| 真实人工分级 | 0／150 | 第二供应商、规格人审和试点也仍为0 |

公开3a4d5ce已包含[十领域与跨族对照](reports/F271-application-mapping.md)及[有条件候选](reports/cards/APP-271-01.md)，48候选、15初检。该版CI的EXP119严格raw比较失败；新上传的[失败证据](reports/reproducibility/20261029-CI40842772641/payload-inspection.json.gz)核实4处浮点中点差异各1ULP，其他raw和summary相等，具体运算原因未定位。当前本地[APP178构造准入](reports/F178-constructor-admission.md)保留原10%/全成本假设且无新实验。

近期可核对的成果：

- [F149反应网络检验](reports/retrospectives/045-old-method-sufficiency-and-history-scope.md)：72个合成实例、401次精确更新，27例负浓度事件；旧逐坐标基线全部捕获，没有确认2026数学的额外计算收益。
- [F181历史范围](reports/F181-historical-scope-followup.md)：选定原作由4／11补至8／11；旧局部扩张准则在对应接口上更强。剩余原作、精确转录与递归证明缺口保留。
- [F337实际AD诊断](reports/F337-AD-execution.md)：192项参考有效，但16个零点后端异常使冻结主预测待定；独立列为诊断，不增加初检。
- [F271当前阅读检查点](state/reading-progress/WP-129.json)：四当前稿46源文件14,199行均已实际读完，五部历史原作仅核选定范围。已规范整理8个方法接口及九月基础稿34条来源命题；另已绑定有限容量引理及有限程30条和修正稿23条，累计88语义绑定、剩球面稿30条定位待整理；十领域/三跨族探索已进行，整族与历史仍未完成。不增加完整族、全文草稿或应用计数。见[方法接口](reports/F271-partial-methods.md)和[基础稿命题](reports/F271-foundation-claims.md)。

最新本地回归有97项核心检查、无math干净环境检查、18个科学归档／378源码成员及代表性严格重放证据；本批发布检查另见[发布核验目录](reports/reproducibility/20261029-F271-mapping/)。软件检查不证明数学结论或业务收益。[验收矩阵](reports/acceptance.md)、[机器指标](reports/metrics.json)、[全局复盘045](reports/retrospectives/045-old-method-sufficiency-and-history-scope.md)保留完整差距。

**OpenAI官方的 `math/` 目录不包含在本仓库中，也不复制或重新部署。** 原作通过固定[上游提交](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a)、标识和校验清单引用。第三方全文、缓存和批量本地历史同样排除。英文纲领已提供；详细研究账本主要为中文。

## 快速开始

运行核心检查和原有标准库实验复现只需要 Python 3.11+ 标准库，无模型凭证、无需下载 `math/`，也无需安装依赖。最新本地核心及代表性重放环境为 Python 3.12.14 / Apple Silicon macOS；各归档仍以其原规格和实际重放范围为准，远程 CI 环境另见工作流。

```sh
python3 scripts/check.py
python3 scripts/replay_run.py experiments/runs/EXP-128-001-adf42abc31aca23e
python3 scripts/replay_run.py experiments/runs/EXP-097-001-f4db184a4c5e6d4d
python3 scripts/replay_run.py experiments/runs/EXP-130-001-eadb2e7b3a00d556
python3 scripts/replay_run.py experiments/runs/EXP-374-001-bc1d2887fa6a5d33
python3 scripts/replay_run.py experiments/runs/CHK-374-MOMENTS-001-67a3ef843df4bf9f
python3 scripts/replay_run.py experiments/runs/EXP-238-001-a1d52c04aeb9b1ba
python3 scripts/replay_run.py experiments/runs/EXP-200-001-a8300854205212bf
python3 scripts/replay_run.py experiments/runs/CHK-200-LEX-001-433f4f99a2d5ac2e
python3 scripts/replay_run.py experiments/runs/EXP-221-001-be34f84b97b2e9a9
python3 scripts/replay_run.py experiments/runs/EXP-314-001-ce8cf18c32275b81
python3 scripts/replay_run.py experiments/runs/EXP-325-001-9bedfaa5ac3a53d0
python3 scripts/replay_run.py experiments/runs/EXP-076-002-1f8537b7fd40d564
python3 scripts/replay_run.py experiments/runs/EXP-119-001-e9d098be0b1dda8f
PYTHONPATH=src python3 -m ai_value.cli query F-128
PYTHONPATH=src python3 -m ai_value.cli export-graph
python3 scripts/audit_graph_provenance.py
```

打开 `reports/graph/index.html` 可离线检索全部成果族、沿手稿—命题—零件—应用链查看出处和限制。GraphML 和完整图谱 JSON 以 gzip 输出到同目录，可导入其他工具。图谱由规范记录生成，不手工改导出文件。全文拆解报告见 `reports/families/`；同名标签按手稿与来源文件分别绑定，文献身份按 DOI/标题区分，避免混并。

使用本地现有上游重新做全量文件盘点：

```sh
PYTHONPATH=src python3 -m ai_value.cli inventory
PYTHONPATH=src python3 -m ai_value.cli audit-versions
```

上游必须是 `1581d4cbdd69a0faf34b2089614fe2a814316a6a` 且工作区干净。其他版本会被拒绝，必须建立独立更新批次。初次获取上游见 `scripts/fetch_upstream.py`；全量约 3.1 GB，默认不下载。研究命令会压缩数值输出，并以内容散列创建新运行目录；原运行不覆盖。

```sh
PYTHONPATH=src python3 -m ai_value.cli experiment all
PYTHONPATH=src python3 -m ai_value.cli validate
PYTHONPATH=src python3 -m ai_value.cli report
```

`experiment all` 在当前代码下重新运行十二项应用检验与两项零件检查，包含新的可选玻色子实验，因此需要Python3.12.14与NumPy2.3.5；标准库核心检查与上列历史单项重放不受影响。新实验的独立运行入口见[有限玻色子回归](docs/bosonic-regression.md)。它不会新增线索，也不构成全量 372 族研究。小样本程序有明确规模限制；扩大研究需要新增真实阅读、规范节点、预注册规格与独立输入，不靠复制卡片扩数。

## 图谱与证据

- 规范来源是 `data/corpus/` 的版本化语料节点表，以及 `data/graph/` 的研究节点、关系和阅读覆盖记录。图谱加载器从外键投影归属关系，不凭目录标题推断数学结论。
- 来源节点保留每条引用的定位、版本与散列；未固定字节或版本的外部 URL 保持为观察记录。节点字段、前版归档和全量引用回查纳入核心检查，详见 [来源与版本审计](reports/provenance-audit.md)。
- 原文主张、已核对的来源内容、模型假设、实验观察、真人决定分别记录。B 级上游声明不能当作本地 Lean 构建通过；未知依赖会让整条应用链保持未知。
- 真人审核和第二供应商目前由用户明确延后。持续进行可独立完成的工作，不伪造审核；同模型辩护/怀疑仅作辅助自查，检验前或结果已知后的实际生成时点按卡片分别记录，未隔离的意见不称独立评审。
- 失败保留为“观察”，正式否定要求两名真实审稿人。试点要求完整 A 级依赖和真实人工授权。
- 卡片附原文定位、输入与代码压缩快照、配置、随机种子、原始输出、环境、运行时间和 Python 分配内存。旧标准库实验只记录Python分配；EXP273另实际记录完整进程峰值RSS（含NumPy／原生分配），不是子进程总量。

族 221 已读完全部正文，26 项结果、11 个源文方法契约入图谱。`EXP-221-001` 已完成27个固定合成算例并独立重放：符号检查拒绝9项错误上界迁移，18项对照未违反。旧PT条件已经足够指出该边界；没有验证2026全层级等式、有限规模收敛率或译码收益。

有明确对象映射、额外前提和检验方案但尚未运行的条目可以成为“待定候选”；它们仍不计入已初检卡片、有效线索或数值验证。

族314的六个合成小群、61个嵌入子群及108条正规循环商关系已从实际计算写入图谱，带完整乘法表、嵌入集合、链证据和运行出处；它们不是谱对象或新谱定理验证。149/124/276/178/021、076的另一条波形审核及333周期标定候选尚无外部检验。

每三项实质工作包或重要数据问题触发全局复盘。当前任务队列见 `state/backlog.json`，恢复入口见 `state/checkpoint.json`。

## 磁盘、许可与发布

不复制上游、不自动下载 Lean 缓存或大型模型。全量文件散列清单约 7 MB，数值输出和输入代码快照均压缩，238 的完整小排列概率表由约 21.9 MB 压到约 684 KB；临时复现目录自动清除。压缩先校验解压 SHA-256，保留恢复入口，不能以节省空间为由丢弃不利证据。

本项目代码、原创文档与原创派生记录采用 Apache-2.0，见 `LICENSE` 和 `NOTICE`。上游仍保留自身许可；外部论文仅保存书目信息、必要转述和定位，不能推定其全文采用同一许可。`math/` 排除于本项目历史，按 commit 和清单引用。

本项目已公开发布至 [GitHub](https://github.com/yiduo/mathweave)；远程提交及匿名核验记录见 [发布记录](state/publication.json) 与 [发布范围](docs/publication.md)。OpenAI 官方 `math/` 目录不上传、不复制或重新部署，仅引用其链接、固定版本和来源散列。`0.1.0` 不是已发布的正式版本声明。

## English overview

A local, evidence-preserving application-mining project for a pinned mathematical manuscript corpus. It stores typed claims, sources, transferable components, hypotheses, conservative dependency grades, and reproducible numerical checks. The full phase-one goal remains open. Human reviews, independent second-provider checks and engineering pilots remain outstanding. The public repository scope and last verified snapshot are recorded separately. The offline standard-library checks and archived-source replays require no model credentials.

F115的实际表/流工具反查见 [第四次需求反查](reports/table-flow-demand-F115.md)：固定SciPy阶乘表律与NetworkX最优流接口后，候选继续待定；历史文档的精确代数见证不增加应用初检。

WP068 [矩形归一化接口核查](reports/F294-scaling-interface-audit.md)已入图：部分匹配、强旧边际缩放和基线资格缺口分别记录；没有新数值实验或初检。

[F049两稿与证书范围](reports/stable-coordinate-F049-reading.md)新增18结果／18契约，保留两个不同反例与任意交换环无除法提升的适用条件；实际应用消费者待核，无新实验。

[F049实际CAS接口](reports/F049-cas-interface-audit.md)确认旧映射证书已区分商环与环境；[复盘025](reports/retrospectives/025-cas-contracts-and-coverage-priority.md)转回低覆盖源文，未新增应用验证。

[F210六次幂比较、指定映射与计算证据范围](reports/foulkes-F210-reading.md)

[F317任意严格目标、呈示与Thomason结构](reports/thomason-F317-reading.md)

[替代证明路线与前提变化影响预览](docs/proof-route-impact.md)已支持CLI及页面操作；[复盘026](reports/retrospectives/026-proof-routes-and-application-readiness.md)记录当前覆盖、应用差距和下一包。

[周期标定的同约束KKT基线审核](reports/F333-calibration-baseline-audit.md)保留原预测，明确投影／完整速度目标及无新增数值检验。

[F085连续圆盘端点与多尺度消去](reports/disk-maximal-F085-reading.md)：21来源结果／21契约及直接和旧条件正则性替代路线，连续／离散及BV范围分开。

[F025短单位分数与精确标记](reports/egyptian-F025-reading.md)：19结果／22契约，项数与位成本、自然与形式化不同供给路线分开；[全局复盘027](reports/retrospectives/027-baseline-identity-and-exact-marker-costs.md)转真实符号库消费者核查。

[F025实际符号库接口](reports/F025-symbolic-consumer-audit.md)：固定源码／测试／许可核查，新增一条精确标记待定候选；真实调用方、运行环境和完整成本尚待建立，不计初检。

[F273熵光子数与四权重零件](reports/entropy-photon-F273-reading.md)：17项来源结果、21契约；端口独立／内部纠缠及形式化范围分开，新增一条待定远类比，不计初检。

[F094大胆应用的实际数据与构造核查](reports/F094-bold-readiness-audit.md)：许可明确的小型数据已取得，关键标签与有限共同分布仍待建立；两个未建立前提与强旧基线已入图，原预测未检验。[全局复盘028](reports/retrospectives/028-small-data-and-executable-constructors.md)已完成。

[F273有限玻色子回归](reports/bosonic-regression-F273.md)：36场景／252固定故障，新旧熵界均62检出、额外0，完整矩阵已足够。新增实际初检卡保留不利观察，数值与源码压缩并独立重放；[固定可选运行时与边界](docs/bosonic-regression.md)。

[F231自由生成森林与联合创新](reports/fusf-F231-reading.md)：14来源结果、18契约与关键旧范围入图；普通Borel与有限查询成本分开。新增待定无根查询候选，没有新初检；补齐关键历史依赖后全局复盘。

[F231关键历史接口](reports/fusf-F231-key-history.md)：三项原始来源拆为11项范围，BBL齐次化、旧布朗构造与群作用条件分开；6/16选定文献根不等于完整谱系。[复盘029](reports/retrospectives/029-historical-interfaces-before-more-drafts.md)调整投入，优先已有历史缺口并保留低覆盖探索。

[F231算子与观测历史接口](reports/fusf-F231-operator-history.md)：补核可数DPP／有限维经典创新／有限与周期图转移电流，作者勘误与未确认的局部归一化疑点分开保留；旧查询公式具体连边，9/16选读根不等于完整谱系。

[F332期望中位数与扩张范围](reports/metric-Markov-cotype-F332-reading.md)：七项自然结果与14契约、三个历史原文范围；去噪候选保持待验证，概率质量／形式化／成本缺口明确入图。

[F332固定去噪实验](reports/F332-finite-denoising-experiment.md)：9/18胜例、2损失例，原预测未支持；实际旧基线、加权中位数退化和有限风险口径公开保留。[复盘030](reports/retrospectives/030-denoising-risk-and-old-baselines.md)转向有界完整族验收闭合。

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/replay_run.py experiments/runs/EXP-332-001-b2607a9926c44586
```

EXP332按原始源码快照重放全部科学输入／输出／风险与结论，仅排除规格事先声明的测时／RSS字段；其他旧归档默认完整JSON严格比较。实际验证Python3.14.7标准库；使用记录的运行环境复现，不因当前源码指纹变化重新生成run替代原证据。

[F332完整族验收审计](reports/F332-family-acceptance-audit.md)：实际补读MN有限扩张证明，记录原书仅两页预览、Ball正文获取上限及全域桥接缺口；完整族与历史仍0。下一研究包转低覆盖F153。

首次Linux CI的68核心及11归档重放通过，F076原始数据逐值比较失败但汇总一致；原macOS/Python3.14.7严格重放两者均一致，原数据／比较器未改。Linux CI明确覆盖其他13归档，不宣称F076跨平台可重现；失败证据与范围见[发布核验](docs/publication.md)。公开交付触发[全局复盘031](reports/retrospectives/031-publication-and-platform-scope.md)，后续恢复F153研究。

[F153算术分类与有限证书](reports/bernoulli-F153-reading.md)：全部2579行TeX＋252行书目＋487行验证器已读，24来源结果／19方法契约及三个未建前提入图；无限判据不等于有限分类器，验证器静态核对不等于执行，AR(1)类型联系不等于有限收益。本包无新候选或数值实验。

[APP09402元数据就绪核查](reports/F094-metadata-readiness.md)：真实14个字符串字段已读通，8984细胞ID唯一，48组重复读出中40组有不同扰动标签。仅解除可读性前提，生物判据、零距离规则与有限共同分布构造仍缺；原10%预测未运行，不增加初检。

WP089 [真实符号需求核查](reports/F025-demand-followup.md)找到带第二大分母约束的旧调用，当前单标记包装不满足其额外要求，候选保留待定而不增加初检。[复盘032](reports/retrospectives/032-demand-constraints-and-next-counting-route.md)完成，下一包实际读未拆解 F113 两篇；官方 math 持续只读且不部署。

[F113两稿全文与计数接口](reports/perfect-matching-F113-reading.md)：62项结果、26契约及三前提缺口已入图；无权相对计数／二进制粗计数、最大律熵／任意观测熵、保见证／保计数分别保留。六个选定形式规格局部B，未构建／无人审；没有新候选或应用实验。

[F113真实计数接口与光子标定联系](reports/F113-counting-demand.md)：实际三来源核对产生一条待定近类比候选，字面副本采样成本不准入，没有运行或新增初检；旧精确／随机计数与一般量子采样边界分别保留。

[F139精确查询模型与旧法边界](reports/log-concave-F139-reading.md)完成39结果与16契约的当前全文草稿；任意正维度幂的查询上界不代表运行时间改进。GitHub按实质里程碑批次降频，本包保持本地，官方math仍只读且不发布。

[F273四权重真实需求核查](reports/F273-fourweight-demand.md)核对原始LipSDP与CVXPY接口：相关用途存在，但现成四前提证书、认证裁判和完整成本仍未准入。候选与原预测保留，无新数值运行或初检。下一包转低覆盖的代数与复几何F058两稿。


本地新增[有限程30来源陈述](reports/F271-finite-range-claims.md)与44选定证明接口，累计65语义绑定，均不作完整证明审核或额外应用信用。下一独立APP178构造准入后全局047，再续整族；尚未推送。


本地修正稿部分整理：新增[23条来源陈述](reports/F271-correction-claims.md)和71选定证明接口，已有容量引理保持，累计88/118语义绑定，剩球面稿30条。固定S、全Bose和、体积/场/低温次序、后验钉扎非独立及双残差均保留；不增加阅读、完整族或初检信用。97核心/干净97及完整图谱/来源/依赖/归档检查通过，下一继续球面稿。
