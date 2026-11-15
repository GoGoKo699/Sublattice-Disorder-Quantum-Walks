# What survives when the clean symmetry is lost

The argument has three distinct steps. Keeping them separate explains both the result and its restrictions.

## Clean motion can be compressed

The graph has exponentially many physical vertices. Exact interlayer degrees make the uniform superposition on each layer evolve within the span of those layer states. The clean walk therefore admits a short-chain calculation. Its endpoint zero-mode amplitude and a source-specific flow can be computed without listing the full graph. This graph framework and the noiseless algorithmic advantage are prior work, as explained in [Related work](../references/RELATED_WORK.md).

## Microscopic disorder invalidates the dynamical compression

If the onsite potential is constant across a layer, its uniform state stays uniform. Different potentials at different vertices in an odd layer instead create nonuniform components. The actual disordered walk can enter an exponentially large complement of the clean layer space. Reusing the clean chain's dynamics after this perturbation would be incorrect.

The dark state remains because its odd-vertex amplitudes vanish. This partial-chiral protection is also established prior physics. Its survival establishes an endpoint contribution in an infinite time average, but does not by itself say how long that contribution takes to become visible. Near-zero bulk modes could otherwise cancel it throughout the available window.

## A local inverse moment controls the waiting time

The [matrix theorem](inverse_moment.md) bounds the inverse-energy weight of those modes at the entrance and exit. Strict positivity on the odd block keeps every positive eigenvalue above a known floor. A constrained-energy identity then bounds the absolute negative inverse contribution through a flow determined only by the clean off-diagonal block.

The resulting time-average bound has no minimum global gap. The [endpoint flow](graph_family.md) has energy only linear in depth, so a quadratic time window suffices, and quadratically many runs give bounded-error navigation. The number of physical vertices may be exponential; the quantities entering this endpoint estimate remain polynomial.

## Which comparisons follow

The uniform quantum upper bound holds for all allowed positive odd-site assignments, including ones that destroy the invariant layer space. To compare with classical exploration, choose graph-independent iid binary assignments. These marks can be generated lazily from private randomness once path parity is known. A graph-correlated adversary could encode a route in potential values, so that stronger universal classical quantifier is not asserted.

This is a robustness statement about uncorrected fixed-Hamiltonian dynamics. Coherent adjacency queries would also allow an active algorithm to simulate the clean graph. Neither the underlying task's first quantum advantage nor a new unrestricted separation is claimed.

The positivity floor, protected even block, exact hopping structure and hidden-label oracle matter. The [precision account](resources.md) permits controlled implementation errors at explicitly shrinking budgets; it does not turn arbitrary constant all-site errors into the promised disorder model. These restrictions delimit the scientific result rather than an unexamined implementation detail.
