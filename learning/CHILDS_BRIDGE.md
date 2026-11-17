# From Childs' quantum-walk notes to sublattice disorder

The familiar starting point is a hidden maze: the entrance label is known, the exit label is unknown, and a query reveals only the neighbors of a named vertex. A clean quantum walk can cross some exponentially large mazes because its motion compresses into a small space of uniform layer states. This project asks what survives when microscopic onsite disorder destroys that compression.

The answer needs two ingredients. A zero-energy state retains its entrance-to-exit contribution. A local spectral estimate then proves that this contribution becomes visible within a finite, polynomial time. Keeping the zero state unchanged is the starting point, not the whole transport proof.

## The selected educational anchor

The single educational anchor is Andrew M. Childs, [*Lecture Notes on Quantum Algorithms*, 17 April 2025](https://www.cs.umd.edu/~amchilds/qa/qa.pdf).

| Source location | Use in this project |
|---|---|
| §1.6, *Quantum complexity* | Separate oracle calls from the size of an explicit circuit. |
| §17.1, *Continuous-time quantum walk* | Interpret a Hamiltonian as a rule for moving amplitudes on a graph. |
| §§17.4–17.5, black-box traversal and its quantum algorithm | Understand the hidden entrance-to-exit task and the clean layer reduction. |
| §17.6, *Classical and quantum mixing* | Understand why sampling an evolution time gives a useful probability distribution. |
| §17.7, *Classical lower bound* | Understand why the comparator includes all classical exploration algorithms. |
| §27.4 and Chapters 28–29 | Connect sparse evolution to charged quantum-circuit implementation. |

These sections supply the entry route. The block-matrix moment theorem and the disordered graph proof are developed in this repository. Research attribution and imported theorem dependencies are recorded separately in [Related work](../references/RELATED_WORK.md).

## 1. What the clean compression means

A vertex basis state $`|x\rangle`$ represents a position in the graph. A quantum state assigns a complex amplitude to each position. Evolving for time $`t`$ applies $`e^{-itH}`$; measuring the vertex register returns a label, with probability equal to its squared amplitude.

For a layer $`L`$, its normalized uniform state is

```math
|L\rangle=\frac{1}{\sqrt{|L|}}\sum_{x\in L}|x\rangle.
```

The clean graph is wired so that every vertex in one layer has the same number of neighbors in the next, and conversely. Adjacency therefore maps a uniform layer state to a combination of uniform layer states. Starting at a singleton entrance keeps the clean walk inside their span. This is an exact invariant subspace, not an approximation or a claim that the machine knows the hidden layers.

The project uses a different exact graph from the notes' original glued trees. Its [degree-six construction](../science/graph_family.md) has $`N=20\,4^n-16`$ physical vertices and only $`4n+3`$ layers. The clean quotient remains useful for calculating certain vectors, even though it will cease to describe the disordered motion.

## 2. Why microscopic disorder breaks that calculation

Split the vertices into two bipartition classes, $`\mathsf E`$ and $`\mathsf O`$. Every edge connects opposite classes; both endpoints belong to $`\mathsf E`$. With that basis order,

```math
A_G=\begin{pmatrix}0&B\\B^\dagger&0\end{pmatrix},
\qquad
H=\begin{pmatrix}0&B\\B^\dagger&V\end{pmatrix}.
```

The diagonal entry of $`V`$ at an odd vertex is its onsite energy. The theorem assumes $`v\leq V_{xx}\leq W`$ for known $`0<v\leq W`$, while every even onsite energy is exactly zero.

If two vertices in the same odd layer receive different values, multiplying that layer's uniform state by $`V`$ produces unequal amplitudes. Those amplitudes contain a component outside the uniform-layer space. The actual walk can enter the exponentially large complementary space. We must therefore analyze the full $`H`$; continuing to evolve only the small quotient would solve a different problem.

The restriction to one sublattice matters. This theorem does not cover arbitrary all-site disorder, arbitrary hopping errors, or an indefinite odd block.

## 3. What the protected zero state does—and does not—prove

A zero state has the form $`(z,0)`$ with $`B^\dagger z=0`$. Direct multiplication gives

```math
H\begin{pmatrix}z\\0\end{pmatrix}
=\begin{pmatrix}0\\B^\dagger z\end{pmatrix}=0.
```

It has no amplitude on the disordered sublattice, so changing $`V`$ leaves this vector unchanged. Strict positivity also ensures that these are all the zero states. Write $`P_0`$ for their orthogonal projector.

In the spectral expansion of the transition amplitude, the zero contribution $`\langle b|P_0|a\rangle`$ stays constant in time. The other contributions rotate with their nonzero energies. At time zero they must cancel the zero contribution, because distinct endpoints have zero initial transition amplitude. If some rotating contributions are extremely slow, that cancellation might persist for a long time.

Thus a protected zero state establishes a persistent spectral contribution. A useful algorithm additionally needs a bound on how long the other contributions can hide it. Partial-chiral zero-state protection is inherited physics; the additional [moment bound](../science/inverse_moment.md) addresses this finite-time issue.

## 4. Replace a worst-case gap by the spectral weight seen at the endpoints

For an endpoint $`a`$, define

```math
M_a=\langle a|\,|H|^+\,|a\rangle
=\sum_{\lambda\ne0}\frac{|\langle\lambda|a\rangle|^2}{|\lambda|}.
```

Here $`|H|`$ replaces every energy by its absolute value, and the pseudoinverse $`+`$ replaces a nonzero value by its reciprocal while assigning zero to the kernel. The sum uses an orthonormal eigenbasis; the corresponding projector formulation also handles degeneracy.

A small nonzero energy receives a large reciprocal weight. Its importance is nevertheless multiplied by how strongly the endpoint overlaps that mode. A very slow bulk mode can be harmless for this task if the endpoints barely see it. This is different from proving that no slow modes exist.

To state the project theorem, remove the endpoint's zero component and call the remaining first-block vector $`s_a`$. It lies in $`\mathrm{ran}B`$. The full-space estimate is

```math
M_a\leq W\|B^+s_a\|^2+\frac{2\|s_a\|^2}{v}.
```

The quantity $`\|B^+s_a\|^2`$ is source specific. It is not the operator norm $`\|B^+\|^2`$, which would inspect the worst direction in the entire graph.

The proof connects three facts: the constrained minimum of $`y^\dagger Vy`$ over $`By=s_a`$ determines the signed inverse expectation of $`H`$; $`B^+s_a`$ is a feasible choice that bounds this minimum from above; and all positive eigenvalues of $`H`$ are at least $`v`$. Combining them bounds the absolute inverse expectation, including negative eigenvalues arbitrarily close to zero. The complete argument is in [the matrix theorem](../science/inverse_moment.md).

For both endpoints, the clean graph's layer structure constructs short feasible flow vectors and proves that the source-specific pseudoinverse norms grow only linearly in the number of layers. This use of the clean quotient remains valid: it calculates properties of the unchanged $`B`$, rather than pretending that $`V`$ preserves the disordered dynamics.

## 5. Turn the moment bound into a measured success probability

Choose $`t`$ uniformly from $`[0,T]`$. Each nonzero spectral phase obeys

```math
\left|\frac1T\int_0^T e^{-it\lambda}\,dt\right|
\leq\frac{2}{T|\lambda|}.
```

Keeping the endpoint weights and applying Cauchy–Schwarz gives

```math
\left|\mathbb E_t\langle b|e^{-itH}|a\rangle
-\langle b|P_0|a\rangle\right|
\leq\frac{2\sqrt{M_aM_b}}{T}.
```

This controls the **average amplitude**. The experiment measures probabilities. The connection is $`\mathbb E|A_t|^2\geq|\mathbb E A_t|^2`$: squaring the magnitude of the mean provides a lower bound on the mean measured success probability. No intermediate measurement of an eigenmode or hidden layer is needed.

For the exact graph family, the zero-projector endpoint element has magnitude $`1/Z`$, with $`Z=2+3(k-1)/5`$ and $`k=2n+1`$. Both moments are bounded by $`\overline M=5Wk/24+2/v`$. Taking $`T=4Z\overline M`$ leaves at least half the zero contribution in the average amplitude, giving success at least $`1/(4Z^2)`$ per run. At fixed $`v,W`$, the horizon and required number of runs are each $`O(n^2)`$. Failed runs are charged. See [Traversal](../science/traversal.md) for the exact statement.

## 6. A complete three-site example

Take the line with entrance $`a`$, middle site $`o`$, and exit $`b`$. Set both hopping amplitudes to one and the middle onsite energy to $`\nu>0`$. In position order $`(a,o,b)`$,

```math
H=\begin{pmatrix}0&1&0\\1&\nu&1\\0&1&0\end{pmatrix}.
```

In block order $`(a,b\mid o)`$, this is $`B=(1,1)^T`$ and $`V=(\nu)`$. The normalized zero state and its endpoint contribution are

```math
|z\rangle=\frac{|a\rangle-|b\rangle}{\sqrt2},
\qquad
\langle b|P_0|a\rangle=-\frac12.
```

Changing the middle energy does not change this state. The other two energies are $`(\nu\pm\sqrt{\nu^2+8})/2`$, obtained by restricting $`H`$ to the span of $`(|a\rangle+|b\rangle)/\sqrt2`$ and $`|o\rangle`$.

The entrance with its zero component removed is $`s_a=(|a\rangle+|b\rangle)/2`$. Solving $`By=s_a`$ gives $`y=1/2`$, so $`\|B^+s_a\|^2=1/4`$ and $`\|s_a\|^2=1/2`$. The same holds for the exit. The theorem therefore gives

```math
M_a,M_b\leq\frac\nu4+\frac1\nu.
```

For $`\nu=1`$, use the conservative bound $`M_a,M_b\leq5/4`$ and choose $`T=10`$. The possible nonzero-spectrum remainder in the average amplitude is at most $`1/4`$. Since the zero contribution has magnitude $`1/2`$, the average transition probability is at least $`1/16`$.

A complete run prepares $`a`$, samples a duration in $`[0,10]`$, evolves under the displayed matrix, measures the position, and checks whether it is $`b`$. Eighteen independent runs give failure probability at most $`e^{-18/16}<1/3`$. These deliberately loose bounds illustrate the proof chain. This three-site system has no hidden-graph hardness or asymptotic speedup; the large graph supplies that separate ingredient.

## 7. Translate the access model before interpreting the advantage

| Notation or idea in the anchor | Notation or role here |
|---|---|
| A vertex name represented by bits | An $`\ell=O(n)`$-bit random label; the entrance name is supplied. |
| A local port selects a neighbor | A charged reversible neighbor-list query; ports reveal no layer direction. |
| Uniform column states | Uniform states of this family's hidden layers; used analytically, not supplied as input. |
| The walk Hamiltonian | The prescribed $`H=A_G+\mathrm{diag}(0,V)`$. |
| Spectral control of time averaging | The endpoint moments $`M_a,M_b`$, rather than a minimum full-spectrum gap. |
| A classical lower bound | A bound against arbitrary adaptive classical queries, not just random walking. |

The graph-size parameter in the notes is not a formula to transplant into this construction. Use this repository's exact layer and degree definitions. Also distinguish the potential matrix $`V`$ here from the conventional use of $`V`$ for a graph's vertex set.

The [classical lower bound](../science/classical_lower.md) imports the research-level hidden-graph transcript method of Balasubramanian–Li–Harrow and specializes it to this family. Random labels and ports hide the graph's direction; iid odd-site values can be supplied lazily and do not reveal it. That proof is not replaced by saying that a random walker gets lost. The uniform quantum robustness statement and the iid classical hard distribution have different quantifiers.

For gate-model implementation, neighbor, onsite-value and exit-membership calls are charged. The seven-sparse Hamiltonian can be simulated with finite precision; the [resource account](../science/resources.md) also charges random-time discretization, basis-state preparation, failed runs, reset and output. The ideal $`O(n^4)`$ integrated evolution-time upper bound must not be confused with an optimal gate count or a physical crossover.

An active algorithm with adjacency access could simulate the clean graph and omit the potential. The project's added result is that the **uncorrected prescribed disordered walk** remains efficient. It does not claim a new unrestricted oracle separation or robustness to every kind of noise.

For an ordered route through the whole project, continue with the [30-milestone common map](MILESTONES.md): 12 background targets followed by 18 narrative targets. Each target points to this same anchor and the canonical science. You can also return to the [scientific reading route](../README.md#read-the-science) or go directly to the [full local-moment proof](../science/inverse_moment.md).
