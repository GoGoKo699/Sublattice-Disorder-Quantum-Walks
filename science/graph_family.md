# An exact degree-six hidden graph

This family makes the two parts of the argument explicit. The clean adjacency matrix has a small invariant layer space, which permits an exact endpoint calculation. Positive potentials may then vary independently within every odd layer, destroying that invariant space while preserving the endpoint guarantee through the [local moment theorem](inverse_moment.md).

The random hierarchical graph construction and classical hiding mechanism are inherited from the framework of Balasubramanian, Li, and Harrow. The construction below is an exact bounded-degree family; it uses no approximate graph sparsification.

## Layers and degrees

Fix $n\geq1$. On the left, use even layers $E_0,\ldots,E_n$ and odd layers $O_0,\ldots,O_{n-1}$, with

$$
|E_0|=1,\qquad |O_0|=6,
\qquad |E_j|=15\,4^{j-1}\quad(1\leq j\leq n),
$$

$$
|O_j|=2|E_j|\quad(1\leq j<n).
$$

Take a disjoint reflected copy on the right, denoted $E'_j,O'_j$. Between the two peak even layers $E_n,E'_n$, insert a central odd layer $O_c$ of size

$$
|O_c|=\frac43|E_n|=20\,4^{n-1}.
$$

The entrance is the unique vertex of $E_0$ and the exit the unique vertex of $E'_0$. The layers form one line, with the right-hand layers in reverse order.

The degree rules on the growing left half are:

- The entrance has six neighbors in $O_0$.
- Each vertex of $O_0$ has one neighbor in $E_0$ and five in $E_1$.
- Each vertex of $E_j$, $1\leq j<n$, has two neighbors in the previous odd layer and four in $O_j$.
- Each vertex of $O_j$, $1\leq j<n$, has two neighbors in $E_j$ and four in $E_{j+1}$.
- Each vertex of $E_n$ has two neighbors in the previous odd layer and four in $O_c$.
- Each vertex of $O_c$ has three neighbors in $E_n$ and three in $E'_n$.

Reflect these rules on the right. For $n=1$, the previous odd layer at $E_n$ is $O_0$ and the same boundary rules apply.

Every physical vertex has degree six. All edge counts match. For example,

$$
6\cdot5=15\cdot2,
\qquad
|E_j|\cdot4=|O_j|\cdot2,
\qquad
|E_n|\cdot4=|O_c|\cdot3.
$$

All these bipartite degree constraints admit simple graphs. There are no intra-layer edges, loops, or parallel edges.

For every adjacent layer pair, independently choose a uniformly random simple biregular graph with the specified degrees. Randomize each vertex's local neighbor-port order independently, and apply the uniform injective $\ell$-bit labeling specified in the [model](model.md). Neither a port nor a label identifies a hidden layer or direction.

Both bipartition classes have size $10\,4^n-8$, so the total vertex count is

$$
N=20\,4^n-16.
$$

The graph has $2k+1$ layers, with

$$
k=2n+1.
$$

## The clean layer space

For a layer $L$, write

$$
|L\rangle=\frac1{\sqrt{|L|}}\sum_{x\in L}|x\rangle.
$$

The fixed interlayer degrees imply that adjacency maps uniform layer states into their span. More specifically, the off-diagonal block $B$ and its adjoint both preserve the corresponding odd and even uniform layer spaces. The orthogonal complements are also preserved, so these spaces reduce the clean bipartite adjacency matrix.

If each vertex in a layer has $d_+$ neighbors in the next layer and each next-layer vertex has $d_-$ neighbors back, their quotient hopping amplitude is

$$
\sqrt{d_+d_-}.
$$

The quotient's boundary hoppings are $\sqrt6,\sqrt{10}$, its growing and shrinking interior hoppings are $\sqrt8$, and its two central hoppings are $\sqrt{12}$.

Adding vertex-dependent onsite values to the odd block generally invalidates this invariant-space description of the **disordered** dynamics. We use the clean quotient only to compute a kernel projector and construct a low-energy flow; the full evolution is controlled by the matrix theorem.

## The zero projector at the endpoints

Order even layers along the line by $i=0,\ldots,k$ and odd layers by $j=0,\ldots,k-1$. The quotient off-diagonal block $B_q$ has two positive entries in column $j$: $a_j$ at row $j$ and $b_j$ at row $j+1$.

A sign change on alternating basis vectors makes these entries $a_j,-b_j$. In that gauge, the positive kernel vector is

$$
c=(1,r,\ldots,r,1)^T,
\qquad
r=\sqrt{\frac35},
\qquad
Z=\lVert c\rVert^2=2+\frac35(k-1).
$$

Indeed, the boundary equation is $\sqrt6\,c_0=\sqrt{10}\,c_1$, the interior and central columns have equal adjacent entries, and the reflected boundary restores the final entry to one. The oriented path matrix has rank $k$, so this quotient kernel is one dimensional.

The entrance and exit are singleton layer states. Since the clean layer spaces reduce $B$ and $B^\dagger$, components of $\ker B^\dagger$ orthogonal to the layer space have zero endpoint overlap. Thus their physical endpoint kernel projector is exactly the quotient one. Restoring alternating signs gives

$$
\langle b|P_{\ker B^\dagger}|a\rangle
=\frac{(-1)^k}{Z}=-\frac1Z.
$$

The [matrix theorem](inverse_moment.md) shows that the same matrix element is $\langle b|P_0(H)|a\rangle$ for every positive odd-block $V$. Extra physical kernel vectors, if present, do not alter this endpoint calculation.

## A source-specific flow bound

Let $C=\operatorname{diag}(c_i)$, and let $D$ be the oriented incidence matrix of the path: its column $j$ has entries $+1$ at row $j$ and $-1$ at row $j+1$. Set

$$
\Gamma_j=a_jc_j=b_jc_{j+1}.
$$

In the sign gauge,

$$
B_q=C^{-1}D\Gamma,
\qquad
\Gamma=\operatorname{diag}(\Gamma_j),
\qquad
\Gamma_j^2\geq\frac{24}5.
$$

The endpoint projected off the kernel is $s_a=e_0-c/Z$. To solve $B_qy=s_a$, multiply by $C$ and sum the incidence equations up to edge $j$. This gives

$$
\Gamma_jy_j
=1-\frac{\sum_{i=0}^j c_i^2}{Z}.
$$

Every cumulative flow on the right lies in $[0,1]$. Consequently

$$
\lVert y\rVert^2
\leq\frac{5k}{24}.
$$

For the exit load represented by $e_k$ in this gauge, the projected source is $s_b=e_k-c/Z$ and the cumulative flow is

$$
\Gamma_jy_j
=-\frac{\sum_{i=0}^j c_i^2}{Z},
$$

which lies in $[-1,0]$ and gives the same bound.

Lifting these quotient vectors to normalized odd layer states gives physical feasible solutions of $By=s_a$ and $By=s_b$. The Moore–Penrose solution minimizes the ordinary squared norm among all feasible solutions, so, irrespective of extra physical kernels,

$$
\lVert B^+s_a\rVert^2,
\ \lVert B^+s_b\rVert^2
\leq\frac{5k}{24}.
$$

This source-specific bound grows only linearly in the number of layers. It does not lower-bound the smallest nonzero singular value of the complete physical matrix.

## What the graph hides

All degrees and port-alphabet sizes are identical. Random labels hide the layer assignment. The exponential growth and shrinkage of layer sizes supply the classical hiding mechanism, while the zero-mode amplitude is spread across only $O(n)$ even layers in the uniform layer representation.

The bipartition label supplies no new navigation information along an explored tree: it is already determined by path parity from the entrance. Independent binary potentials on odd vertices therefore supply independent vertex marks, rather than a hidden depth or direction oracle. Adversarial graph-correlated marks are outside the classical hard distribution.

See [traversal](traversal.md) for the finite-time consequence and the separate classical comparison for the full adaptive-oracle lower bound.
