# GitHub publication scope

Authorized by the project owner on 2026-10-22: publish the existing Chinese charter, an English translation, and related research progress as an open-source GitHub repository. The owner explicitly excludes redeployment of OpenAI's official `math/` directory.

## Included

- Original Chinese charter, English charter, bilingual entry documentation, and English progress snapshot.
- Original project source, tests, schemas, research configurations, and workflow.
- Versioned corpus identifiers, reconciliation and checksum manifests; canonical research graph; generated cards, family drafts, navigation, and compressed exports.
- Registered experiments, compressed numerical outputs and source snapshots, adverse outcomes, attribution, and reproducibility receipts.
- Project checkpoints and backlog describing actual work and remaining requirements.

## Excluded

- `math/` in its entirety, including upstream manuscripts, formalization files, and Git metadata. Existing upstream links and pinned hashes identify original sources.
- External-paper downloads, temporary renders and replays, virtual environments, model or Lean caches, and local credentials.
- Local Git history as a bulk upload. The initial public branch is a snapshot with no parent commit, reusing the reviewed current tree. This keeps publication small and avoids publishing unreviewed historical files. Required research prior versions and experiment source snapshots remain included explicitly.

The local research branch retains its history. The public branch records the actual publication snapshot and future publication updates. This is a source repository publication, not a website hosting deployment, engineering pilot, or declaration of completed research. Open `reports/graph/index.html` after downloading the repository to use its existing offline viewer.

## License

Project code, original documentation, and original derived records use Apache-2.0. `NOTICE` identifies separately licensed third-party sample data and small source-inspection tools. Upstream mathematics and external papers are not relicensed. The public repository is an independent research effort with no claimed upstream endorsement.

## Verification

Before pushing: complete the core checks, graph/source/foreign-key checks, dependency-impact checks, compressed archive checks, and a clean-directory run without `math/`. Audit the exact publication tree for excluded paths, credentials, controlled material, and oversized files. Record the tree and commit identifiers.

After pushing: verify the repository's public visibility and remote branch commit. Save the observed URL, commit, and verification time in `state/publication.json`. A prepared tree is not a successful push; a push is not a successful CI run. Remote CI status is reported only after an actual run. Research completion and review counts remain independent of publication.

## Actual first CI and platform limit

The first Ubuntu 24.04 / Python 3.14.8 run passed all 68 core tests and the first 11 archived replays, then failed EXP-076-002's strict raw-data comparison; its summary matched. The preregistered experiment explicitly freezes its environment because floating-point trigonometric optimization may drift across platforms. A new strict replay on the original macOS / Python 3.14.7 environment matched both complete raw and summary payloads. The Linux difference has not been localized to every field, so no assertion is made that all chosen outputs or certificates are identical there.

The Linux `portable-core` job now explicitly covers 13 other archived checks. EXP076 is excluded from that portability claim; its original data and strict comparator are unchanged. The optional NumPy bosonic archive also has a separately pinned runtime. Failed remote logs and the successful macOS receipt are retained, compressed, under `reports/reproducibility/20261022-publication/`. See [retrospective 031](../reports/retrospectives/031-publication-and-platform-scope.md). A green scoped workflow does not mean every archive is portable or mathematically reviewed.

## Publication cadence

The owner requested fewer GitHub updates on 2026-10-22 and reaffirmed this preference on 2026-10-23. Routine work packages, reading journals, checkpoints, and local commits stay local. Consider a reviewed publication batch after a meaningful milestone; neither a retrospective nor a completed package automatically triggers a push. An explicit publication request can override this cadence. The policy is recorded in `configs/research.json`; this configuration records the execution rule and does not itself schedule publication. On October 23 the owner explicitly requested a batch through WP-107 / retrospective 038, including the incomplete WP-108 reading journal. The existing repository was renamed to [MathWeave](https://github.com/yiduo/mathweave); its stable repository ID is 1429150108. The previous verified snapshot was `f0c3ddc` through WP-092 / retrospective 033. Exact new commit and CI observations are recorded separately in `state/publication.json`, without inheriting the old CI success. The official `math/` directory remains excluded.

## October 26 owner-requested batch

The owner requested publication of current progress and an easy-to-share project name. The existing name **MathWeave (数学织网)** is retained: “math” identifies the source material and “weave” describes linking results, historical methods and testable applications. The public repository and local origin already use `https://github.com/yiduo/mathweave`; no duplicate repository or local directory rename is needed. This batch adds WP108 canonical F239 reading and evidence, plus WP109's explicitly unfinished selected-source qualification journal. It adds no application-check or human-review credit. The official `math/` tree and bulk local history remain excluded. Post-push verification receipts are retained locally for the next meaningful batch, avoiding a second routine push.


## Current explicit owner request: WP109 and unfinished WP110

The owner again requested current progress on GitHub. Retain **MathWeave (数学织网)** and the existing repository address; no duplicate repository or directory rename is needed. Include completed WP109 canonical records and its conditional APP23901, plus the WP110 reading checkpoint (36/38 files,10014/10336 lines; canonical F238 coverage still4/12). WP110 is not a completed package and adds no application validation. Create one reviewed public commit parented by the previous public branch, excluding bulk local history and official math. Record post-push verification locally for the next meaningful batch to avoid a second routine push.


## Current owner-requested batch: completed WP110 and unfinished WP111

Retain **MathWeave (数学织网)** and the existing public address [yiduo/mathweave](https://github.com/yiduo/mathweave), whose stable repository ID is 1429150108. The repository and local origin already use this name, so no duplicate repository or local checkout rename is needed. Publish completed WP110 / GEN107 and retrospective039, plus WP111’s incomplete source-reading checkpoint: 15 complete TeX files / 4,500 lines and a further 245-line partial range, totaling 4,745/7,647 lines. No new application check or human/provider review is claimed. Create one reviewed public commit parented by the last public commit, excluding the official math directory and bulk local history. Save post-push verification locally for the next meaningful batch; routine publication remains disabled.
