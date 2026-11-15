# Finite-time navigation with microscopic disorder

The walk succeeds because its endpoint zero-mode amplitude remains visible within a polynomial averaging time. The proof controls all the other physical modes through their endpoint overlaps, even after the onsite disorder destroys the clean invariant layer space.

## Theorem

Take a graph from the [exact family](graph_family.md), and let its odd-site diagonal potential obey $v\leq V_{xx}\leq W$ for fixed known $0<v\leq W$. Put

$$
k=2n+1,
\qquad
Z=2+\frac35(k-1),
\qquad
\overline M=\frac{5Wk}{24}+\frac2v,
\qquad
T=4Z\overline M.
$$

A run starting at the entrance, evolving under the prescribed $H$ for a uniformly sampled time $t\in[0,T]$, and measuring the vertex reaches the exit with probability at least

$$
p_* = \frac1{4Z^2}.
$$

The guarantee holds for every allowed microscopic potential assignment and every wiring satisfying the exact graph-family degree constraints. For fixed $v,W$, $T=O(n^2)$ and $p_*^{-1}=O(n^2)$.

### Proof

The graph calculation gives

$$
|\langle b|P_0(H)|a\rangle|=\frac1Z,
\qquad
\lVert B^+s_a\rVert^2,
\ \lVert B^+s_b\rVert^2
\leq\frac{5k}{24}.
$$

The projected endpoint sources have norm at most one. The [local inverse-moment theorem](inverse_moment.md) therefore bounds both endpoint moments by $\overline M$. Its time-average estimate gives

$$
\left|\mathbb E_t\langle b|e^{-itH}|a\rangle
-\langle b|P_0(H)|a\rangle\right|
\leq\frac{2\overline M}{T}
=\frac1{2Z}.
$$

The averaged amplitude has magnitude at least $1/(2Z)$. Applying $\mathbb E|A_t|^2\geq|\mathbb E A_t|^2$ gives the stated success probability. This proof makes no assumption about a global spectral gap.

## A bounded-error algorithm

The input supplies $n,v,W$ and the entrance label. It does not supply the hidden layers, the exit label, or the microscopic potential realization.

1. Prepare the entrance basis state.
2. Sample $t$ uniformly from $[0,T]$ and evolve under the fixed $H$ for that duration.
3. Measure the vertex label and query exit membership.
4. Return a positively identified exit, or start a fresh run.

After

$$
R=\left\lceil4Z^2\log\frac1\delta\right\rceil
$$

runs, the probability of having no successful output is at most

$$
(1-p_*)^R\leq e^{-Rp_*}\leq\delta.
$$

Taking $\delta=1/3$ gives the usual bounded-error navigation task. The worst-case integrated evolution time is bounded by

$$
RT=O\!\left(n^4\log\frac1\delta\right)
$$

for fixed $v,W$. Repetition charges failed runs and their durations. The exit-membership flag is supplied to the classical comparator as well.

## What changes when the quotient is lost

With no microscopic potential, the walk remains in the span of uniform layer states. If different vertices in an odd layer receive different onsite values, applying $V$ to its uniform state produces nonuniform components. The disordered walk can therefore enter the full physical Hilbert space, whose dimension is exponential in $n$.

The result does not assert that these additional modes have a polynomial gap. Instead, their total inverse-energy weight at the endpoints is bounded. Strict positivity of the odd block first isolates the positive spectrum; a minimum-energy identity then controls the negative spectrum's weighted endpoint contribution. That local estimate is enough for finite-time averaging.

Thus an unchanged dark zero mode is one ingredient, not the complete transport argument. The additional assertion is that the prescribed walk can access its endpoint contribution within polynomial time after the original dynamical reduction has failed.

## Implementation and interpretation

The continuous-time theorem fixes the actual Hamiltonian throughout a run. It uses no sign reversal, active refocusing, learning of $V$, or cancellation of its onsite terms.

For a logical oracle implementation, simulate this same seven-sparse $H$ with charged reversible neighbor and potential queries. The binary instance $V_{xx}\in\{1,2\}$ has exact constant-bit onsite data. Standard finite-bit sampling and sufficiently accurate simulation preserve a constant fraction of the inverse-polynomial per-run success probability; the explicit budgets and overhead are proved in the [resource account](resources.md). The displayed $O(n^4)$ bound is the integrated ideal evolution-time bound, before those precision and compilation factors.

This result extends the robustness of a known quantum navigation mechanism. It does not claim that the disorder creates a harder unrestricted quantum task: an active algorithm with the same logical oracles could remove or ignore it. The comparison of interest is that this **fixed disordered walk** remains polynomial while arbitrary classical exploration of the hidden graph remains exponential under the specified independent-potential distribution.

No statement here covers generic all-site disorder, indefinite odd-site potentials, arbitrary hopping perturbations, or a practical crossover on a physical processor.
