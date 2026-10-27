# F181: few decomposition parts and the cost of finding them

WP122 / GEN-20261027-119; pinned upstream `1581d4cbdd69a0faf34b2089614fe2a814316a6a`.

All nine current TeX/Bib files (2,566 lines) and the README were read. Sixteen labelled results and twelve conditional method contracts are recorded in `data/provenance/readings/F-181.json` and the canonical graph. This is a current manuscript decomposition draft; complete family history, recursive proof review and human acceptance remain unfinished.

The main claim gives one absolute constant C such that every finite simple undirected graph on n vertices has an exact edge partition into at most Cn simple cycles and singleton edges. Vertices may be shared across parts. Repeated edges are forbidden, isolated vertices need not be covered, and an edgeless graph permits an empty partition. The claim counts parts, not time, bits, total traversed route length or concurrent scheduling capacity.

The proof's transferable interfaces retain their conditions:

- Team-constrained routing requires cut expansion, bounded global endpoint load, bounded team size and forbidden interior sets. With its specified route length ell, the requirement is `h >= 64*(ell^2*(k+b)+z)`. Global edge disjointness alone does not ensure a lifted quotient cycle is simple.
- Pair folding requires both low degree at every active vertex and a bound on every vertex's neighbors into each folding set. The manuscript's complete-bipartite warning shows why the first requirement alone is insufficient. Error edges are explicitly retained as singleton parts; quotient edges keep unique original representatives.
- Batches may overlap in vertices while their assigned edges remain disjoint. Loads are measured over the union of all batches in the earlier box. Reserved router edges are consumed once; a separate spanning expander survives for processing the remainder.
- Fixed sampling probabilities, common sufficiently large scale cutoffs and the order in which constants are chosen are essential. The recursive potential bounds the number of parts. It does not certify practical construction cost.

Four original historical works were checked only in selected converted-text scopes, with source and text hashes: Erdős–Goodman–Pósa's 1966 distinction between covers and partitions, Conlon–Fox–Sudakov's general and special-class bounds, Bucić–Montgomery's iterated-log bound and stated auxiliary inputs, and Girão–Granet–Kühn–Osthus's dense-graph bounds and equivalence proposition. Seven of eleven original roots remain unqualified. Reading the Aharoni–Haxell and Lovász restatements in Bucić–Montgomery does not count as reading their original proofs; the attempted Lovász original download returned 403.

The older dense-graph result already gives a linear count with an asymptotically sharp coefficient under linear minimum degree. The source's weak-cut Eulerian corollary uses the historical equivalence proposition; it must not be described as an already unconditional older theorem with no minimum-degree condition. Generalizing the count to all simple graphs does not itself establish a better practical algorithm.

Actual Main, decomposition definitions, Comparator wrapper/config and selected routing signature were read. The selected main endpoint receives source grade B; the other fifteen natural-language result bindings retain C, and all complete dependency grades remain unknown. The import index covers 34 local files and 1,270 lexical declarations; it is not a Lean build, Comparator execution or full proof/axiom audit. The Comparator challenge's placeholder is a statement template, separate from the indexed solution closure. The noncomputable `decompositionCost` existence interface supplies no executable complexity claim.

Ten domain explorations and two cross-family comparisons are retained separately. Two concrete gaps concern construction cost and route/lifting certificates. No new application card, numerical run or initial-check credit was added. Counts remain 47 candidates and 14 qualified initial checks, with one separately recorded diagnostic execution. The next global review compares work on existing unchecked cards, historical closure and low-coverage sources.

Evidence: `reports/reproducibility/20261027-F181-source-scope/`; canonical records: `data/graph/`; source ledgers: `data/provenance/readings/F-181*.json`. Research remains local after the last verified public snapshot; the official `math/` corpus is excluded from publication.
