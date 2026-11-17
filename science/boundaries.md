# What the theorem's restrictions do

The traversal theorem covers a protected even block and a uniformly positive odd block. The examples below explain why its proof does not automatically cover broader perturbations. They do not claim a general localization theorem or rule out other algorithms.

## An indefinite odd block can give a large local inverse moment

The matrix lemma allows a general Hermitian odd block, although the algorithmic graph model uses a diagonal onsite potential. To test the lemma's positivity restriction, take

```math
B_\eta=\begin{pmatrix}1&0\\1&0\\0&\eta\end{pmatrix},
\qquad
V=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad \eta>0,
```

and let the source be the first even basis vector. Here $`\lVert V\rVert=1`$ and $`\lVert B_\eta^+s\rVert^2=1/4`$. The even dark vector $`(1,-1,0)/\sqrt2`$ remains an exact zero vector, with endpoint projector element $`-1/2`$ between the first two even coordinates.

In the orthogonal bright sector, the nonzero block is a four-site chain with couplings $`\sqrt2,1,\eta`$. Its two squared positive energies are the roots of

```math
x^2-(3+\eta^2)x+2\eta^2=0.
```

The smaller positive energy is asymptotic to $`\eta\sqrt{2/3}`$. Its pair of opposite-energy modes has total source weight tending to $`1/6`$, and therefore

```math
\langle s|\,|H_\eta|^+\,|s\rangle
\sim\frac1{\sqrt{24}\,\eta}.
```

Thus the source inverse moment can diverge while the dark projector and $`\lVert B_\eta^+s\rVert`$ stay fixed. An unchanged zero mode alone does not supply the local moment bound.

This is a counterexample to extending the **general-block moment estimate** without its sign restriction. Its off-diagonal $`V`$ is not a diagonal onsite potential on the degree-six graph family, so it is not presented as a failure example for every signed diagonal graph potential. The [finite check](../verification/precision_resource_check.py) verifies the displayed asymptotic coefficient.

## Perturbing the protected block removes exact zero protection

For $`B=(1,1)^\mathsf T`$ and odd potential $`V=1`$, add opposite even-site potentials:

```math
H_\delta=\begin{pmatrix}
\delta&0&1\\
0&-\delta&1\\
1&1&1
\end{pmatrix}.
```

Its determinant is $`-\delta^2`$. Every nonzero $`\delta`$ therefore removes the exact zero eigenvalue used in the proof. This illustrates the exact protected-sublattice assumption; it does not imply that every such finite perturbation prevents transport.

Norm-small implementation errors are controlled for the finite horizon by the [precision budget](resources.md). Arbitrary constant-strength even-site disorder, unrestricted signed odd-site disorder and arbitrary hopping perturbations remain outside the claimed theorem.
