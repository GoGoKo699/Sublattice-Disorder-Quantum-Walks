# Sublattice Disorder Quantum Walks

**Can a quantum walk remain fast when microscopic disorder destroys the symmetry used to analyze its clean motion?** On an explicit hidden graph, bounded positive onsite potentials on one sublattice preserve polynomial entrance-to-exit traversal even when different vertices in the same layer receive different potentials.

The clean graph has exponentially many vertices but only linearly many uniform layer states. Disorder breaks that small invariant space, so the clean chain calculation no longer describes the motion. A protected zero mode survives. The key additional step is to bound how strongly all the other modes can cancel its endpoint contribution over a finite time.

## Principal result

Write the fixed Hamiltonian in its two bipartition blocks:

```math
H=\begin{pmatrix}0&B\\B^\dagger&V\end{pmatrix},
\qquad 0<vI\preceq V\preceq WI.
```

For a source on the first block, the [local inverse-moment theorem](science/inverse_moment.md) gives

```math
\langle s|\,|H|^+\,|s\rangle
\leq W\|B^+s\|^2+\frac{2\|s\|^2}{v}.
```

Zero-eigenvalue components are omitted by the pseudoinverses. The estimate controls source-weighted slow modes without a minimum gap in the complete spectrum. On the [degree-six graph family](science/graph_family.md), it yields the following upper bounds at fixed positive $v,W$ and failure probability $0<\delta\leq1/3$.

| Charged resource | Sufficient bound at depth $n$ |
|---|---:|
| Physical vertices | $20\,4^n-16$ |
| Evolution horizon per run | $O(n^2)$ |
| Runs, including failures | $O(n^2\log(1/\delta))$ |
| Total prescribed-Hamiltonian evolution | $O(n^4\log(1/\delta))$ |
| Coherent input-oracle calls | $\widetilde O(n^4\log(1/\delta))$ |
| Additional elementary gates | $\widetilde O(n^5\log(1/\delta))$ |
| Logical workspace for oracle simulation | $O(n)$ qubits |

The walk prepares the known entrance label, samples an evolution time, evolves under the same disordered $H$, measures a vertex, and checks exit membership. It learns or cancels no onsite potential. Finite random bits, value precision, simulation error, reset, output and oracle implementation are charged in the [resource account](science/resources.md). These are upper bounds, not optimal exponents.

The quantum guarantee is uniform over the permitted positive odd-site potentials. The classical comparison uses independent binary potentials, random labels and random local ports. Such potentials supply no hidden direction or layer information. Arbitrary adaptive classical algorithms require exponentially many queries on the specified hard distribution; the [classical account](science/classical_lower.md) gives the exact probability bound and its inherited graph-exploration method.

## Read the science

| Question | Authoritative account |
|---|---|
| What is supplied, measured and charged? | [Model and task](science/model.md) |
| Why are slow bulk modes harmless at the endpoints? | [Local inverse moment](science/inverse_moment.md) |
| Which exact graph realizes the endpoint bounds? | [Graph family and flow calculation](science/graph_family.md) |
| How do sampled times produce a finite-time success guarantee? | [Traversal theorem](science/traversal.md) |
| What can an arbitrary classical algorithm observe? | [Classical lower bound](science/classical_lower.md) |
| How much precision and circuit overhead are required? | [Resources](science/resources.md) |
| Which restrictions are essential? | [Interpretation](science/interpretation.md) |
| Which ingredients are prior work? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| What is checked computationally? | [Verification](verification/README.md) |

The [reading guide](llms.txt) maps the scientific questions to their proof sources.

## Learn the result

The single educational anchor is Andrew M. Childs' *Lecture Notes on Quantum Algorithms*, dated 17 April 2025. Start with the [Childs bridge](learning/CHILDS_BRIDGE.md), which connects the clean hidden-graph walk to the full-space disorder argument and a complete three-site example. The [30-milestone common map](learning/MILESTONES.md) then organizes the project's understanding targets into 12 background and 18 narrative milestones, with exact anchor sections and canonical proof pointers.

## Reproduce the finite checks

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The checks inspect explicit small matrices, graph regularity, lost layer invariance, endpoint projectors, inverse moments and precision budgets. The general theorems and classical asymptotics rest on the written arguments, not on finite numerical agreement.

## Scope

The contribution is robustness of the **prescribed disordered walk**. The noiseless navigation advantage, hierarchical-graph framework and dark-state protection are credited foundations. An active quantum algorithm with adjacency access could omit the potential; the project does not claim a new unrestricted graph-query separation.

The even onsite block remains exactly zero, and the odd block has a fixed positive lower bound. Arbitrary signed potentials, generic all-site disorder and hopping perturbations are outside the guarantee. The graph is an implicit oracle input; no QRAM loading, industrial application or physical crossover is assumed.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
