# Classical queries cannot navigate the hidden graph efficiently

The classical comparator may use arbitrary adaptive computation and storage. It is not restricted to a random walk. This account proves a distributional exponential query lower bound for the exact simple graph ensemble in the [graph construction](graph_family.md), including the independent onsite-value oracle and exit test in the [model](model.md).

The hidden-graph transcript method is inherited from [Balasubramanian, Li, and Harrow (BLH)](https://arxiv.org/html/2307.15062v2), especially Definitions 2.2 and 2.5, Theorem 5.4, Corollary 5.5, and Example 6.1/Lemma 6.2. We supply the details needed for this deterministic size profile, the uniform **simple** biregular ensemble, and the additional independent site marks.

## The lower-bound statement

Write the physical layers as $`S_0,\ldots,S_L`$, where

```math
L=4n+2,
\qquad
N=20\,4^n-16.
```

The entrance and exit are the singleton layers $`S_0`$ and $`S_L`$. Every interlayer graph is sampled independently and uniformly from the simple biregular graphs with the prescribed directional degrees. Local port orders are uniform and independent. Vertex labels form a uniform random injection into a universe of size $`M\geq N^2`$.

The algorithm receives the entrance label, $`n`$, and the family description. It receives no map from labels to layers and no graph-dependent advice. It may query neighbors, independent fair values in $`\{1,2\}`$ on odd vertices and zero on even vertices, and exit membership. All calls are counted. Arbitrary new-label queries and an arbitrary final output label are allowed.

**Theorem.** There are absolute constants $`C`$ and $`n_0`$ such that, for $`n\geq n_0`$, every classical algorithm making at most

```math
Q\leq 2^{n/128}
```

calls returns the exit label with probability at most

```math
C\,2^{-n/5},
```

averaged over the graph, labels, ports, independent marks, and its own randomness. Thus bounded-error traversal requires $`\exp(\Omega(n))`$ classical queries on this distribution.

This is an oracle distributional statement. It does not assert hardness for an algorithm supplied with the particular instance's exit as advice. The [quantum robustness bound](traversal.md) is uniform over permitted positive onsite assignments; the classical hard distribution uses graph-independent iid values. Arbitrary graph-correlated values could encode a route and are outside this lower bound.

## The volume profile

Let $`s_i=|S_i|`$ and $`d(i)=\min(i,L-i)`$. The exact sizes in the [construction](graph_family.md) obey

```math
2^{d(i)}\leq s_i\leq4\,2^{d(i)}.
```

If $`e_i`$ denotes the number of edges between layers $`i`$ and $`i+1`$, every cut in the growing interior, beyond the fixed boundary gadget, satisfies

```math
e_i=4s_i\geq4\,2^i.
```

Both bipartition classes have $`10\,4^n-8`$ vertices. Every physical vertex has degree six. Within a layer, every vertex has the same left and right degrees, so the graph is balanced in BLH's sense. No physical degree or port count reveals position. Independent random port ordering is essential: ports labeled by their left/right direction would supply a different input model.

## The correct nonbacktracking state space

Let $`l_i`$ and $`r_i`$ be the left and right degrees of a vertex in layer $`i`$, with $`l_i+r_i=6`$. At the entrance $`l_0=0,r_0=6`$, with the reflected convention at the exit.

The layer alone is not a Markov state for a nonbacktracking walk. The ordered pair of previous and current layers is. For example,

```math
\begin{aligned}
P((i-1,i),(i,i+1))&=\frac{r_i}{5},\\
P((i-1,i),(i,i-1))&=\frac{l_i-1}{5}.
\end{aligned}
```

The analogous formulas hold after entering from the right. These probabilities are exact for every fixed balanced graph and every physical incoming edge: precisely five outgoing ports remain after excluding the parent edge.

The stationary law on these oriented layer edges is

```math
\pi(i,i+1)=\pi(i+1,i)=\frac{e_i}{6N}.
```

For example, the incoming stationary mass at $`(i,i+1)`$ is

```math
\frac{e_{i-1}r_i+e_i(r_i-1)}{30N}
=\frac{s_i r_i(l_i+r_i-1)}{30N}
=\frac{e_i}{6N}.
```

The endpoint cases follow directly, and $`\sum_i2e_i=6N`$ normalizes the law. Periodicity is irrelevant.

Start at the layer orientation $`(a,a+1)`$. Its point mass is elementwise at most $`\pi/\pi(a,a+1)`$, and a stochastic transition preserves this domination. For every time $`t`$ and every set $`R`$ of layers,

```math
\Pr(i_t\in R)
\leq\frac{6\sum_{j\in R}s_j}{e_a}.
```

No uniform physical starting vertex is assumed. An adaptively selected physical cut crossing still has the same initial oriented layer state. The bound applies to an unconditioned nonbacktracking path; the adaptive transcript reduction below explains where that path occurs.

## Exposing a uniform simple biregular graph

Consider one interlayer simple $`(r,s)`$-biregular graph, with $`m`$ edges and degrees at most $`D=6`$. Give its vertices labeled stubs and condition on $`h`$ exposed stub pairs $`F`$. Every simple graph has the same product of local factorials many stub realizations. Thus this representation samples the required uniform simple graph and independent port orders, and its remaining completion is uniform conditional on $`F`$.

Fix an unrevealed stub $`\alpha`$ at vertex $`u`$ and a set $`A`$ of vertices on the opposite side. In a completion where $`\alpha`$ is paired to a stub at $`v\in A`$, choose a second unexposed edge $`(u',v')`$ and switch

```math
(u,v),(u',v')\longmapsto(u,v'),(u',v).
```

Exclude edges in $`F`$, forbidden endpoint coincidences, edges creating a parallel pair, and choices with $`v'\in A`$. At least

```math
m-h-2D^2-D|A|-2D
```

choices remain. Each resulting completion with $`\alpha`$ paired outside $`A`$ has at most $`D|A|`$ reverse switchings, one for each possible opposite-side stub in $`A`$. The switch preserves every exposed pair, every degree, and simplicity. Double-counting these switches gives, whenever the denominator is positive,

```math
\Pr(\alpha\text{ reaches }A\mid F,\text{ simple})
\leq
\frac{D|A|}{m-h-2D^2-D|A|-2D}.
```

Consequently, if the relevant layer sizes are at least $`S`$, at most $`Q`$ edges and $`Q+1`$ vertices have been exposed, and $`S`$ exceeds a fixed multiple of $`Q`$, then

```math
\Pr(\text{a fresh port reaches a seen vertex}
\mid\text{partial history})
\leq C_0\frac{Q}{S}
```

for an absolute constant $`C_0`$. The bound is uniform over admissible partial histories and survives averaging over unobserved directional port assignments.

This is a local counting argument in the simple ensemble. It does not divide by the probability that an entire configuration-model graph is simple, which could lose an exponential factor across the many interlayer blocks. For analysis, exposing both endpoint ports of an edge is harmless; the reverse port can also be found with at most six ordinary neighbor queries.

## Two cuts separate informative cycles from the hidden middle

For sufficiently large $`n`$, set

```math
b=\lfloor n/4\rfloor,
\qquad
a=\lfloor n/2\rfloor.
```

Call $`i\leq a`$ the entrance-side prefix. Define the small endpoint region

```math
R_b=\{i:d(i)\leq b\}.
```

Its total volume satisfies

```math
\sum_{i\in R_b}s_i\leq16\,2^b.
```

Every layer outside $`R_b`$ has size at least $`2^b`$. Any path leaving the entrance-side prefix first crosses $`a\to a+1`$, whose cut has $`e_a\geq4\,2^a`$ edges. The stationary comparison and a union bound therefore give

```math
\Pr\!\left(
\text{a nonbacktracking path from }(a,a+1)
\text{ reaches }R_b\text{ within }Q\text{ steps}
\right)
\leq24(Q+1)2^{b-a}.
```

The bound includes returns toward the entrance and visits to the exit-side endpoint region. It assumes no monotonic motion. A return to a large prefix layer $`b\lt i\leq a`$ is permitted.

## An unconditioned reference transcript

The entrance region can contain short cycles. Replacing the entire exploration by one tree would therefore be incorrect. Instead, exclude successful guesses of fresh valid labels as bounded below, and consider the graph exposed by ordinary neighbor queries.

Let $`G_{\rm init}`$ be the exposed subgraph reachable from the entrance by a queried path contained in the entrance-side prefix. Keep genuine cycles inside $`R_b`$. Record a coupling failure on **every fresh edge joining already seen vertices with at least one endpoint outside $`R_b`$**, including a cycle wholly inside the large part of $`G_{\rm init}`$. A query from a known layer-$`b+1`$ vertex to a known layer-$`b`$ vertex is included: the latter pool still has size at least $`2^b`$. Thus a direction of querying an edge cannot evade this rule.

Before failure, exposed vertices outside $`G_{\rm init}`$ form tree tendrils with single attachments to it. Each root edge crosses $`a\to a+1`$; an edge between two prefix vertices would instead extend $`G_{\rm init}`$. A tendril may later visit large prefix layers. Returning there is not a failure unless it creates an exposed second attachment. A visit by a tendril to $`R_b`$ is a separate coupling failure.

Define a reference experiment in which each post-cut tendril is an infinite abstract six-regular rooted tree. A requested child receives a fresh unused fake label, an independent mark of the parity fixed by its tree depth, and a fresh local port permutation with its parent port specified. These visible variables are sampled without consulting hidden layer directions. Every new tree vertex has five unused child ports, and its exit flag is zero.

The reference is **not censored by physical survival**. If a latent path reaches a small physical layer, continue returning fresh tree answers and record a coupling failure. If a physical endpoint is reused in the large region, continue with a fresh abstract clone and a fresh permutation. Genuine small-region wiring may remain part of the entrance-side process. After any recorded failure, complete the reference by the same erased-layer rule, without reweighting its previous choices by the failed identification.

Attach hidden layer states to each new post-cut tree by starting its root at orientation $`(a,a+1)`$. Independently at every abstract vertex, place the prescribed residual left/right multiset into its five child positions in a uniform random order. Generate this direction permutation **before** testing any physical matching partner for freshness.

The algorithm sees fake labels, marks and port names, not these directions. Its choice of which child to expand can depend arbitrarily on its own random bits, the visible tree, and genuine small-region exploration. Those data reveal no hidden direction in a post-cut tree. Conditional on its visible reference transcript, a selected root-to-query port path is fixed independently of that tree's hidden permutations. Its **unconditioned reference** layer marginal is exactly the oriented-layer nonbacktracking chain above.

This assertion is not made about the actual process conditioned on avoiding previous collisions. Survival can bias latent directions because layer pools have different sizes. The stationary inequality is applied only to the uncensored reference law.

## Coupling the reference to physical queries

Generate the actual graph by deferred exposure of uniform simple interlayer completions. Whenever a physical vertex is first reached, use the reference's fresh local port permutation there. Its port order is independent of the unlabelled graph; after fixing its one incoming edge, its remaining direction positions have the uniform residual law. A newly reached physical vertex has a uniform unused label under the independent injection, regardless of any bias in its physical identity.

At a queried port, its already drawn direction specifies the interlayer block. Sample its physical matching partner from the uniform simple completion of the revealed pairs. Reusing a seen vertex outside the permitted small-region cycles causes the global collision failure above, charged by the switching bound. A post-cut latent path reaching $`R_b`$ causes the boundary failure. Before either event, every requested large vertex uses a distinct physical permutation and its actual answer agrees with the reference answer.

Exposing another large-region branch cannot reveal a hidden direction without sharing an already used physical vertex or reaching the small region. The former event is charged globally; the latter is charged for post-cut tendrils. Genuine small-region cycles can change which post-cut root is selected, but each new tree has fresh independent permutations and begins at the same layer orientation. This covers adaptive root selection and selective expansion of branches. Pool depletion may change the probability that coupling fails; it is not used to reweight the reference chain.

There are at most $`Q`$ root-to-new-query paths, each of length at most $`Q`$. Along one path, at most $`Q+1`$ vertices have previously been exposed. Before its boundary failure, any new identification that spoils its large-region tree transcript uses an interlayer pool of size at least $`2^b`$. The switching estimate and a path union bound cost at most $`C_1Q^2 2^{-b}`$. Union over at most $`Q`$ paths, also including the global collisions inside the large part of $`G_{\rm init}`$, gives the conservative bound

```math
\Pr(\text{large-region collision or second attachment})
\leq C_1Q^3 2^{-b}.
```

A tighter global count can save one factor of $`Q`$ but is unnecessary. Apply the stationary hitting estimate in the unconditioned reference and union over the same at-most-$`Q`$ selected paths:

```math
\Pr(\text{a tendril reaches }R_b\text{ before real/reference failure})
\leq24Q(Q+1)2^{b-a}.
```

Actual boundary encounters before a collision are included among the reference encounters. No stationary estimate is applied after conditioning reference paths on successful coupling.

These estimates are the concrete averaged easy/hard transcript bound. They permit actual entrance-region cycles and do not require a uniform estimate after conditioning on an arbitrary completely specified easy subgraph. Outside their failure events, $`G_{\rm init}`$ contains no exit, every tendril remains away from the exit-side small region, and no exit label has been returned.

## Independent potentials and exit membership

For every discovered vertex, bipartite parity is determined by its path from the entrance. Repeated paths agree. A simulator answers its first odd-potential query by sampling a fair value in $`\{1,2\}`$ and caching it, and returns zero on even vertices. This is the exact iid distribution under adaptive queries and revisits. The potential oracle supplies private randomness, rather than depth or direction information.

An exit-membership oracle is zero until the exit is encountered or guessed. Coupling it to an identically zero flag changes no earlier decision. Supplying membership to both comparators therefore recognizes a found label without directing the algorithm toward an unseen one.

These statements rely on identical independent mark distributions at all odd vertices. Layer-dependent or graph-correlated values require another analysis.

## Guessing a valid unseen label

After at most $`Q`$ exposed or ruled-out labels, any chosen bitstring not previously returned as a valid vertex has conditional probability at most

```math
\frac{N}{M-2Q}
```

of naming a fresh valid vertex. This follows from the uniform unused portion of the injective encoding. It applies to neighbor, potential and flag calls. Including the final output guess and taking $`Q\ll N`$ gives

```math
\Pr(\text{any successful off-exploration guess})
\leq\frac{2(Q+1)N}{M}.
```

An explicit list of valid labels or graph-dependent labels would constitute stronger access and is not supplied.

## Completing the estimate

Combining collisions, reference boundary visits and label guesses yields

```math
p_{\rm cl}(n,Q)
\leq C_1Q^3 2^{-b}
+24Q(Q+1)2^{b-a}
+\frac{2(Q+1)N}{M}.
```

For $`Q\leq2^{n/128}`$, $`b=\lfloor n/4\rfloor`$ and $`a=\lfloor n/2\rfloor`$, the first exponent is at most $`-29n/128+O(1)`$ and the second at most $`-30n/128+O(1)`$. Since $`N=\Theta(2^{2n})`$ and $`M\geq N^2`$, the guessing term is smaller still. Increasing an absolute constant and choosing $`n\geq n_0`$ gives

```math
p_{\rm cl}(n,Q)\leq C\,2^{-n/5},
```

proving the theorem. The argument uses neither a graph-sparsification conjecture nor a global simplicity-conditioning factor. Its scope is the precise oracle ensemble above; the [fixed-walk traversal theorem](traversal.md) states the separate quantum consequence.
