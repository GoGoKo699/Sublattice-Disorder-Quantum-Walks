# Finite precision and complete resource accounting

The [continuous-time traversal theorem](traversal.md) becomes a finite algorithm with a finite random-time grid, logarithmic value precision, and charged sparse Hamiltonian simulation. At fixed disorder bounds, the total ideal evolution time is $`O(k^4)`$, the oracle count is $`\widetilde O(k^4)`$, and a sufficient known-gate bound is $`\widetilde O(k^5)`$. These are upper bounds; optimality is not claimed.

## Parameters and time grid

Use the notation of the [graph family](graph_family.md):

```math
k=2n+1,\qquad N=20\,4^n-16,\qquad
Z=\frac{3k+7}{5},\qquad
\overline M=\frac{5Wk}{24}+\frac2v.
```

Here $`0\lt v\leq W`$ are known bounds on the odd-site diagonal. Use supplied rational bounds, or conservative rational bounds, when computing the finite algorithm's parameters. Set $`\Lambda=6+W`$, so $`\lVert H\rVert\leq\Lambda`$. Choose

```math
T_0=2^{\lceil\log_2(4Z\overline M)\rceil},
\qquad
q=\max\!\left\{0,\left\lceil\log_2(4\Lambda T_0Z)\right\rceil\right\},
\qquad M=2^q.
```

Thus $`4Z\overline M\leq T_0\lt 8Z\overline M`$. Sample $`j`$ uniformly from $`\{0,\ldots,M-1\}`$ using $`q`$ fair classical bits and set

```math
t_j=\frac{jT_0}{M}.
```

The durations are dyadic rationals with $`O(\log k)`$ bits for fixed $`v,W`$.

Let $`f(t)=\langle b|e^{-itH}|a\rangle`$. Since $`|f'(t)|\leq\Lambda`$, comparing each left grid point with its integration cell gives

```math
\left|\frac1M\sum_{j=0}^{M-1}f(t_j)
-\frac1{T_0}\int_0^{T_0}f(t)\,dt\right|
\leq\frac{\Lambda T_0}{2M}\leq\frac1{8Z}.
```

The continuous-time mean amplitude has magnitude at least $`1/(2Z)`$. The grid mean therefore has magnitude at least $`3/(8Z)`$, and Jensen's inequality gives

```math
\frac1M\sum_j |f(t_j)|^2\geq\frac9{64Z^2}.
```

This replaces continuum time sampling without assuming a global spectral gap.

## Potential values and simulation accuracy

Adjacency entries remain exactly zero or one, and the protected even diagonal remains exactly zero. For a prescribed real-valued odd diagonal, let a finite-bit approximation satisfy

```math
\max_x|\widehat V_{xx}-V_{xx}|\leq\zeta,
\qquad
\zeta\leq\min\!\left\{\frac v2,\frac1{64Z^2T_0}\right\}.
```

This diagonal error has operator norm at most $`\zeta`$. Duhamel's identity implies

```math
\lVert e^{-it\widehat H}-e^{-itH}\rVert\leq t\zeta.
```

For a normalized pure input, the probability of any measured event changes by at most this operator-norm difference. At every sampled time the rounding error therefore changes the exit probability by at most $`1/(64Z^2)`$.

Require the implemented simulation channel to have diamond-norm error at most

```math
\varepsilon_{\rm sim}=\frac1{64Z^2}
```

from the rounded-Hamiltonian channel. Its exit-probability error is at most the same quantity. This channel convention is deliberately conservative and needs no phase alignment between runs. The implemented mean success probability obeys

```math
p_{\rm impl}\geq\frac9{64Z^2}-\frac1{64Z^2}-\frac1{64Z^2}
=\frac7{64Z^2}\geq p_{\rm safe}:=\frac1{16Z^2}.
```

A sufficient number of fractional value bits is

```math
b_{\rm frac}=\left\lceil\log_2\max\!\left\{\frac2v,64Z^2T_0\right\}\right\rceil,
```

when the absolute rounding error is at most $`2^{-b_{\rm frac}}`$. Include magnitude bits for $`W`$. At fixed $`v,W`$, this requires $`O(\log k)`$ bits because $`Z^2T_0=O(k^4)`$. The independent binary-potential ensemble uses values $`0,1,2`$, which have an exact two-bit encoding and no rounding error.

For a native fixed Hamiltonian, no value query is needed: the theorem directly covers its actual allowed positive odd-site values. Simulating one prescribed real-valued Hamiltonian is a separate implementation question; the budget above is sufficient for it.

If a native implementation has deterministic duration error at most $`1/(128\Lambda Z^2)`$, the bound $`|\frac{d}{dt}|f(t)|^2|\leq2\Lambda`$ gives one further probability loss of at most $`1/(64Z^2)`$. The remaining success bound still exceeds $`p_{\rm safe}`$. This is a timing-error implication, not an experimental control claim.

## Restarts, reset and output

For requested failure probability $`0\lt \delta\leq1/3`$, use

```math
R=\left\lceil16Z^2\ln\frac1\delta\right\rceil.
```

Each run prepares the entrance basis state, samples a fresh $`j`$, simulates for $`t_j`$, measures the label, and checks the exit predicate. Return the first positively identified exit. A correctly reset run succeeds with probability at least $`p_{\rm safe}`$ even conditional on earlier failures, so

```math
\Pr[\text{all runs fail}]\leq(1-p_{\rm safe})^R
\leq e^{-Rp_{\rm safe}}\leq\delta.
```

The per-run simulation precision need not be divided by $`R`$: it bounds the actual per-run success probability rather than approximating the joint state of all runs. All failed runs are nevertheless charged. The exit predicate is exact in this model and is supplied to the classical comparator as well.

For an $`\ell`$-bit label, basis preparation, label measurement and reset each cost $`O(\ell)`$ elementary operations per run. Sampling uses $`q`$ classical random bits per run. The successful classical output is one $`\ell`$-bit label, with no tomography or exponentially long output.

## Sparse queries, known gates and workspace

The [input model](model.md) supplies reversible neighbor-list queries, onsite-value queries, and the exit predicate. These are named input oracles and every call is counted. Use an out-of-place XOR convention for the classical functions. Controlled evaluation can then be built by computing into scratch, conditionally copying the answer, and uncomputing, with a constant number of calls; inverse XOR evaluation is the same query.

The Hamiltonian has at most seven nonzero entries per row: six unit adjacency entries and its diagonal. A zero diagonal on an even vertex may occupy the seventh sparse slot. The reverse-port map needed by an in-place sparse-location convention can be obtained by scanning the six neighbors, adding only constant query overhead. Invalid labels may be assigned zero Hamiltonian rows; the valid-vertex space is invariant.

For definiteness, the sparse-simulation theorem of [Berry, Childs and Kothari](https://arxiv.org/pdf/1501.01715) gives, with

```math
\tau=7\max(1,W+\zeta)T_0,
```

a sufficient per-run query bound

```math
Q_{\rm run}=O\!\left(\tau\frac{\log(\tau/\varepsilon_{\rm sim})}
{\log\log(\tau/\varepsilon_{\rm sim})}\right)
```

and an additional two-qubit gate bound

```math
O\!\left(\tau\big[\ell+\log^{5/2}(\tau/\varepsilon_{\rm sim})\big]
\frac{\log(\tau/\varepsilon_{\rm sim})}
{\log\log(\tau/\varepsilon_{\rm sim})}\right).
```

Logarithms can be regularized by positive constants for small arguments. [Qubitization](https://quantum-journal.org/papers/q-2019-07-12-163/) provides another sufficient simulation route with improved logarithmic factors. Both are inherited simulation methods; no new simulator is claimed.

The label length is

```math
\ell=\lceil2\log_2N\rceil=O(k).
```

Counting a second address register, finite value/arithmetic registers and simulation ancillas gives $`O(\ell+\mathrm{polylog}k)=O(k)`$ quantum workspace at fixed $`v,W`$. The inverse and controlled operations used inside a gate-model simulator act on the reversible input-query circuits. The passive physical protocol itself uses no reversal of $`H`$.

For fixed $`v,W`$, the resulting sufficient bounds are:

| Resource | Bound |
|---|---|
| Maximum native evolution per run | $`O(k^2)`$ |
| Summed native evolution | $`O(k^4\log(1/\delta))`$ |
| Sparse neighbor/value calls | $`\widetilde O(k^4\log(1/\delta))`$ |
| Exit-predicate calls | $`O(k^2\log(1/\delta))`$ |
| Known two-qubit gates outside input oracles | $`\widetilde O(k^5\log(1/\delta))`$ |
| Quantum workspace | $`O(k)`$ |
| Potential fractional bits | $`O(\log k)`$ sufficient; binary values exact |
| Fresh classical random bits | $`O(k^2\log k\log(1/\delta))`$ |
| Successful classical output | $`O(k)`$ bits |

The tildes suppress logarithms in $`k`$ and fixed model constants. Address operations contribute a factor $`k`$, so all gate overhead is not merely polylogarithmic in $`k`$; it is polylogarithmic in the physical size $`N`$. Compiling the known single-qubit rotations into a fixed universal gate set adds logarithmic precision overhead, which is included in the suppressed factors. Parameter calculation and simulation-coefficient compilation require polynomial classical work; no exponential table of vertices or times is prepared.

This is an implicit oracle input. No efficient construction of an arbitrary hidden neighbor oracle from a classical adjacency table is asserted, and no QRAM loading cost is omitted. If a concrete data architecture implements those input oracles, its additional cost must be included. The alternative native-Hamiltonian model supplies the fixed dynamics physically. A native network representing all $`N`$ vertices contains $`N`$ modes or sites; the logical $`O(k)`$-qubit simulation bound is not a bound on that network’s component count or construction cost. No physical-hardware crossover is inferred from the oracle complexity.

## References and checks

The explicit sparse-oracle and two-qubit-gate formulas above use Theorem 1 and the oracle definitions in Berry, Childs and Kothari, *Hamiltonian simulation with nearly optimal dependence on all parameters*, [arXiv:1501.01715v3](https://arxiv.org/pdf/1501.01715). Low and Chuang's *Hamiltonian Simulation by Qubitization*, [Quantum 3, 163 (2019)](https://quantum-journal.org/papers/q-2019-07-12-163/), is the optional alternative.

The [precision check](../verification/precision_resource_check.py) evaluates the time-grid and value-rounding budgets on a generated 64-vertex simple degree-six graph with nonbinary positive microscopic disorder. Its [saved output](../verification/precision_resource_check.json) also checks the parameter formulas at several depths and failure targets. It evaluates spectral formulas directly; it is not execution of a compiled sparse-simulation circuit or a physical benchmark. See also the [boundary examples](boundaries.md).
