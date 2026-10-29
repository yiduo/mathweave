# MathWeave

[中文](README.md) · [English charter](CHARTER.en.md) · [Original Chinese charter](722篇AI数学论文应用价值挖掘纲领.md) · [Progress and limits](PROGRESS.en.md)

**Weaving mathematical results, historical methods, and testable applications into an evidence graph.**

The research unit is **result family + historical lineage + application problem**. Versioned records connect source propositions, transferable methods, concrete hypotheses and reproducible checks, retaining conditions and adverse evidence.

**Phase one is incomplete.** Current canonical records contain 48 candidate connections, 15 preliminary checks of distinct hypotheses, seven narrowly supported predictions and eight adverse observations. There are 64 actually read families and 59 current-source drafts. No family has completed its full lineage or all six stages. Real human classification, specification review, second-provider review and pilots remain zero.

The graph contains **9,028 nodes and 26,511 relations**. Its size measures records, not established mathematics or engineering value. A separate diagnostic and two component checks do not inflate the hypothesis count.

This October 29, 2026 owner-requested publication batch includes completed work through **WP128 / global review045** and the **unfinished WP129** journal. Four F271 manuscripts, 46 source files and 14,199 lines were read; five historical originals were checked only in selected scopes. Eight method interfaces and 34 September foundation statements are now curated with conditions and source locations. The October companions retain 84 lexical result locators pending semantic curation; historical and application mappings remain unfinished. This partial work adds no complete-family, source-draft or application credit. See [method interfaces](reports/F271-partial-methods.md) and [foundation statements](reports/F271-foundation-claims.md). See [the journal](state/reading-progress/WP-129.json).

Local work after public snapshot f2aa303 adds [ten-domain and three cross-family comparisons](reports/F271-application-mapping.md), one conditional [killed-return certificate candidate](reports/cards/APP-271-01.md), and a selected capacity-lemma binding. No numerical target or new preliminary check was run; current local counts are48 candidates/15 checks. The public snapshot remains47 candidates and its latest CI failed EXP119 raw equality (summary matched). Local failure-retention edits are not deployed.

Recent checks preserve the old-method null hypothesis. The F149 synthetic reaction-network audit found 27 negative-concentration cases among 72 fixtures and 401 exact updates; the old coordinatewise baseline caught every one. F181's historical comparison found an older local expansion criterion already stronger at the selected interface. Neither establishes incremental 2026 engineering benefit. The F337 AD run remains a separate diagnostic because backend exceptions prevent adjudicating its frozen main prediction.

Repository: [yiduo/mathweave](https://github.com/yiduo/mathweave). Exact public commit, readback and CI observations are tracked separately in [publication state](state/publication.json). Previous public CI success does not apply automatically to this batch. Routine package pushes remain disabled.

## Corpus and upstream boundary

The historical charter refers to 722 manuscripts. The pinned revision `1581d4cbdd69a0faf34b2089614fe2a814316a6a` contains 719 current manuscript records in 372 result families. Reconciliation preserves 692 unchanged paths, 27 linked version updates, and three proof withdrawals. PDF-file counts are not manuscript counts. The approximately 4,000 original questions mentioned in the charter were not fabricated into a dataset.

**OpenAI's official `math/` directory is not included, copied, hosted, or redeployed here.** Read the originals in [openai/math](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). This repository retains identifiers, source locations, version mappings, and checksums. Offline checks can use the pinned checksum manifest without downloading the upstream corpus; this is not a fresh reading of the originals.

This is an independent application-research project. It does not claim OpenAI endorsement or authorship of the upstream results.

## Run without downloading the corpus

Python 3.11+ and its standard library suffice for core checks and the historical standard-library experiment replays. JavaScript viewer tests also need an existing Node.js runtime. No model credentials or Lean installation are required. See the workflow for the actual CI environment; successful software checks do not certify the mathematics.

```sh
python3 scripts/check.py
python3 scripts/replay_run.py experiments/runs/EXP-332-001-b2607a9926c44586
PYTHONPATH=src python3 -m ai_value.cli query APP-332-01
PYTHONPATH=src python3 -m ai_value.cli export-graph
```

Open `reports/graph/index.html` locally to browse the graph. Download the repository ZIP, extract it, and open that file; GitHub's source viewer does not execute the HTML. Compressed JSON and GraphML exports are in the same directory.

The optional finite-bosonic experiment uses the separately documented, pinned Python/NumPy runtime. Do not run `experiment all` expecting a standard-library-only environment. See [runtime and scope](docs/bosonic-regression.md).

The Linux workflow covers 13 archived replays. EXP076 matched complete raw and summary payloads on its original macOS/Python 3.14.7 runtime, but failed raw equality on the first Linux run while its summary matched. It is not claimed portable. The original comparator and archive remain unchanged; [both outcomes and CI scope](docs/publication.md#actual-first-ci-and-platform-limit) are retained.

## Read the evidence

| Resource | Purpose |
| --- | --- |
| [English charter](CHARTER.en.md) | Full translated program, principles, stages, targets, and review gates |
| [Current progress](PROGRESS.en.md) | Evidence counts, adverse outcomes, remaining work, and next package |
| [Acceptance matrix](reports/acceptance.md) | Target-by-target status, generated from canonical records |
| [Machine-readable metrics](reports/metrics.json) | Current counts; registration and reading are kept separate |
| [Graph navigation](reports/graph/navigation.md) | Family and candidate index with explicit conditions and gaps |
| [Canonical graph](data/graph/) and [corpus records](data/corpus/) | Versioned source of records; exports and cards are derived |
| [Application cards](reports/cards/) | Hypotheses, dependencies, objections, and actual checks |
| [Experiment archives](experiments/runs/) | Specifications, compressed raw results, source snapshots, and manifests |
| [Retrospectives](reports/retrospectives/) | Comparisons of different routes and the possibility that old methods suffice |
| [F332 audit](reports/F332-family-acceptance-audit.md) | Actual proof reading and reasons complete-family credit remains zero |
| [F153 reading](reports/bernoulli-F153-reading.md) | Infinite classification, limited verifier scope, and the unestablished AR(1) benefit |
| [Real perturbation metadata](reports/F094-metadata-readiness.md) | Resolved decoding, actual label collisions, and remaining application prerequisites |

Most detailed research records are in Chinese. This release provides English entry documents, rather than claiming every historical record has been translated.

## Evidence and storage rules

Source assertions, selected proof statements, full dependency grades, external checks, and human decisions are separate records. A Lean catalogue entry is not a successful local build, and a model self-check is not human review or a second provider. Unknown prerequisites stay explicit. Formal rejection requires two real reviewers; pilots require complete A-grade dependencies and real authorization.

Register numerical specifications before running experiments. Retain adverse and failed results. Compress numerical payloads and source snapshots, verify decompression hashes, and remove temporary plaintext. Avoid duplicate upstream checkouts and large dependency downloads. Replays use isolated temporary directories that are cleaned afterward.

## License and publication

Original project code, documentation, and derived records are licensed under [Apache-2.0](LICENSE). Third-party items keep their own licenses and attribution in [NOTICE](NOTICE); this license does not relicense upstream manuscripts or external papers. Sensitive directions are represented only by necessary routing information in the public graph.

Publication status and its verification receipt are recorded in [state/publication.json](state/publication.json). Publication does not complete the research program, grant a mathematical credibility upgrade, or imply approval for engineering deployment. See [publication scope](docs/publication.md).


Local generation129 adds [30 finite-range source statements](reports/F271-finite-range-claims.md) with44 selected proof interfaces, all sourceC/full chain unknown. There are65 semantically bound statements and53 October locators still pending. Counts remain48 candidates/15 checks. Next is independent APP178 constructor/cost admission and global047,then remaining F271 scope. These additions are not pushed.
