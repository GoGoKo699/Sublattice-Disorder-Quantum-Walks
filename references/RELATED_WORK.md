# Foundations and the added finite-time statement

The contribution is a robustness theorem for a prescribed continuous-time walk. The hard graph-navigation task, its noiseless quantum advantage, dark-sublattice zero-mode protection, and source-dependent spectral reasoning have substantial precedents. The result here combines an explicit local absolute-inverse-energy bound with a full-physical-space navigation guarantee after vertex-dependent potentials destroy the clean invariant layer space.

## Hierarchical navigation

Childs, Cleve, Deotto, Farhi, Gutmann, and Spielman established an [exponential algorithmic speedup by a quantum walk](https://arxiv.org/abs/quant-ph/0209131). Balasubramanian, Li, and Harrow's [random hierarchical graph framework](https://arxiv.org/html/2307.15062v2) supplies broader balanced graph constructions, zero-mode traversal methods, and the classical hidden-graph proof framework. Their Section 7 onsite construction retains an invariant space of uniform supervertex states. The present potentials vary between physical vertices inside a layer and generally destroy that reduction. Their general framework and classical method are credited ingredients; the exact instance and lower-bound specialization are stated in this repository's [graph](../science/graph_family.md) and [classical account](../science/classical_lower.md).

## Partial chiral protection

Poli, Schomerus, Bellec, Kuhl, and Mortessagne, [*2D Materials* **4**, 025008 (2017)](https://www.lancaster.ac.uk/staff/schomeru/publications/poli2017partial.pdf), already preserve opposite-sublattice zero modes under inhomogeneous onsite terms. Their Section 3.3 and Appendix A cover this point explicitly. Zero-mode invariance is therefore inherited. The [new estimate](../science/inverse_moment.md) controls the absolute inverse spectral weight seen by endpoints, which makes that invariance useful within a polynomial evolution time.

## Microscopic disorder and leakage

Jackson, Khoo, and Strauch, [*Physical Review A* **86**, 022335 (2012)](https://arxiv.org/abs/1206.3178), study physical-site disorder in the full Hilbert space and distinguish it from column-correlated disorder. Their numerical decay, diffusion, and localization results identify the danger of leakage from the column space. This project establishes a positive result under a narrower promise: bounded positive potentials on only the dark sublattice. It does not contradict their generic all-site disorder findings.

## Spectral averaging and source-dependent analysis

Atia and Chakraborty, [*Physical Review A* **104**, 032215 (2021)](https://arxiv.org/abs/2005.04062), improve hitting-time bounds by averaging relevant spectral sectors rather than using the smallest pairwise spacing of the entire spectrum. Their Lemmas 2–3 retain a separating gap for the selected sectors. Belovs' [*Quantum Walks and Electric Networks*](https://arxiv.org/abs/1302.3143) already uses source-dependent flows and effective spectral-gap reasoning for a designed reflection walk. Neither general gap avoidance nor the averaging argument is claimed as a new principle here. The additional statement is the positive-block absolute inverse-moment inequality and its application to the uncorrected disordered Hamiltonian, whose small bulk gaps are not bounded.

## Implementation

Berry, Childs, and Kothari's [sparse Hamiltonian simulation theorem](https://arxiv.org/abs/1501.01715) supplies a sufficient charged oracle implementation. It is an imported simulation algorithm, not part of the claimed novelty. The [resource account](../science/resources.md) distinguishes total evolution time, coherent oracle calls, elementary gates, and workspace.

## Exact boundary of the comparison

An active algorithm given adjacency queries could simulate the clean graph and omit the potential. The result is therefore a finite-time robustness guarantee for the specified disordered walk. It does not introduce a new unrestricted graph-query separation, an optimal time exponent, generic all-site disorder tolerance, or an application-level crossover. These comparisons are targeted at the actual model; they are not an exhaustive priority certificate.

Structured bibliographic metadata is in [references.bib](references.bib).
