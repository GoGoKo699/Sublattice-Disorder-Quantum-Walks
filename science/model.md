# The walk, the disorder, and the computational task

The question is whether a fast quantum walk still reaches its destination when microscopic disorder destroys the small invariant subspace used to analyze the clean graph. The answer here is positive for a specific, explicitly stated type of disorder: positive onsite terms on the sublattice where a transport zero mode vanishes.

The graph-navigation separation without this disorder is inherited. The contribution is a finite-time guarantee for the **prescribed disordered Hamiltonian**, without identifying or canceling its onsite terms and without assuming a gap in its complete spectrum.

## Input and output

For a known integer $n\geq1$, let $G_n$ be drawn from the [degree-six graph family](graph_family.md). It has

$$
N=20\,4^n-16
$$

vertices, a distinguished entrance $a$, and a distinguished exit $b$. Choose

$$
\ell=\left\lceil2\log_2N\right\rceil
$$

and give its vertices uniformly random injective labels in $\{0,1\}^{\ell}$. Thus the label space has size between $N^2$ and $2N^2$, and labels have $O(n)$ bits. The entrance label is supplied; the exit label is not. The algorithm must output the exit label with probability at least $2/3$.

The graph is bipartite, with vertex sets $\mathsf E$ and $\mathsf O$. Both endpoints lie in $\mathsf E$. The layer labels used in the mathematical construction are **not** given as an oracle or a vertex attribute.

An exit-membership query returns one exactly on the exit label. It is available to both quantum and classical algorithms. It lets repeated walk runs recognize a successful measured vertex; it does not give the unknown label in advance.

## The fixed Hamiltonian

Order the vertex basis by $\mathsf E$ and $\mathsf O$. The unweighted adjacency matrix and the disordered Hamiltonian are

$$
A_G=\begin{pmatrix}0&B\\B^\dagger&0\end{pmatrix},
\qquad
H=A_G+\begin{pmatrix}0&0\\0&V\end{pmatrix}.
$$

In the algorithmic family, $V$ is diagonal and its entries obey

$$
0<v\leq V_{xx}\leq W<\infty
\qquad(x\in\mathsf O).
$$

Here $v,W$ are known bounds. Every even-sublattice onsite term is exactly zero. Hopping amplitudes on graph edges are one, fixing the energy and time units. Since the graph has degree six,

$$
\lVert H\rVert\leq6+W.
$$

The simplest finite-bit separation distribution uses independent fair values $V_{xx}\in\{1,2\}$ on odd vertices, independently of graph wiring, port orders, and vertex labels. These potentials vary **between physical vertices within the same layer**. They generally destroy the clean graph's invariant space of uniform layer states.

The quantum upper bound is uniform over all diagonal $V$ in the stated positive interval. The classical hard distribution uses independent potentials. These are different quantifiers: an adversarial assignment correlated with the hidden graph could encode useful navigation information in its values.

## Operations used by the walk

Each run prepares the supplied entrance basis state, chooses a classical duration uniformly in a known interval $[0,T]$, evolves under the fixed $H$, and measures the vertex label. It then checks exit membership. The algorithm uses no layer measurement, disorder estimation, potential cancellation, inverse preparation, or postselection on an unobserved internal event.

This is a passive walk in the operational sense that its only graph-dependent evolution is the prescribed $e^{-itH}$. Randomizing the duration and checking the final answer do not change the Hamiltonian.

## Oracle implementation and the comparison being made

For gate-model resource accounting, give reversible neighbor-list access to the graph, a reversible onsite-value query, and the exit-membership query. A neighbor query returns the label of the requested neighbor, with local port orders randomized independently. In the binary-potential case, the onsite value has a constant-size exact encoding. These calls are charged; the graph is an implicit oracle input, not a freely loaded amplitude vector.

The resulting Hamiltonian is seven-sparse, so standard sparse Hamiltonian simulation implements this same walk with polynomial overhead. A supplied label uses $O(n)$ qubits, and preparing its basis state costs $O(n)$ elementary operations. The [traversal account](traversal.md) gives the integrated evolution-time bound; finite precision and query compilation are accounted for in the [resource account](resources.md).

An unrestricted quantum algorithm with adjacency and potential oracles could ignore or cancel the onsite terms and run a known clean-graph algorithm. We therefore claim **robustness of the fixed disordered walk**, not a new unrestricted query-complexity separation for a previously easy quantum task.

The classical baseline permits arbitrary adaptive neighbor queries, potential queries, and exit tests. It is stronger than a classical random walker. Independent odd-site values can be supplied lazily without revealing hidden depth or direction, so the [classical lower bound](classical_lower.md) retains the hidden-graph exploration obstruction.

## Scope

The load-bearing restrictions are positivity $v>0$, exact protection of the even diagonal block, the specified base graph family, and the prescribed walk. The proof does not establish robustness to arbitrary signed onsite terms, even-sublattice disorder, arbitrary hopping errors, or a physical experimental implementation. The matrix theorem permits dense positive $V$, but sparse implementability is claimed only for the diagonal algorithmic instance.

Continue with the [local inverse-moment theorem](inverse_moment.md), the [exact graph and endpoint calculation](graph_family.md), and the [finite-time traversal guarantee](traversal.md).
