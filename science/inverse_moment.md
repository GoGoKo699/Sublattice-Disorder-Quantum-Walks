# A local spectral bound without a global gap

A preserved zero mode need not be useful at a finite time. Other eigenvalues can lie very close to zero and prevent a short averaging window from isolating it. The estimate below controls those eigenvalues through their overlap with the entrance and exit, rather than through the smallest gap of the entire system.

## Matrix setting

Let $B:\mathbb C^q\to\mathbb C^p$ be any finite matrix. It may be rectangular or rank deficient. Let $V$ be Hermitian and satisfy

$$
0\lt vI\preceq V\preceq WI,
\qquad
H=\begin{pmatrix}0&B\\B^\dagger&V\end{pmatrix}.
$$

The superscript $+$ denotes the Moore–Penrose pseudoinverse. For a Hermitian matrix, $|H|$ is obtained by replacing each eigenvalue with its absolute value. In particular, $|H|^+$ assigns weight $1/|\lambda|$ to each nonzero eigenspace and zero to the kernel.

## Theorem: kernel, energy, and local inverse moment

The kernel is

$$
\ker H=(\ker B^\dagger)\oplus\{0\}.
$$

For $s\in\mathrm{ran}B$ and $u=(s,0)$, define

$$
\mathcal E_s=\min_{Bz=s}z^\dagger Vz,
\qquad
M_s=u^\dagger |H|^+u.
$$

Then

$$
u^\dagger H^+u=-\mathcal E_s,
\qquad
M_s\leq\mathcal E_s+\frac{2\lVert s\rVert^2}{v}
\leq W\lVert B^+s\rVert^2+\frac{2\lVert s\rVert^2}{v}.
$$

No lower bound on the smallest nonzero singular value of $B$, or on the full spectral gap of $H$, is assumed.

### Proof of the kernel statement

If $H(x,y)=0$, then $By=0$ and $B^\dagger x+Vy=0$. Taking the inner product of the second equation with $y$ gives

$$
0=y^\dagger B^\dagger x+y^\dagger Vy=y^\dagger Vy.
$$

Strict positivity implies $y=0$, after which $B^\dagger x=0$. The converse is immediate.

### Proof of the variational identity

Because $s\in\mathrm{ran}B$, $u$ is orthogonal to $\ker H$ and $H H^+u=u$. Write $H^+u=(x,y)$. Its equations are

$$
By=s,
\qquad
B^\dagger x+Vy=0.
$$

For every $z\in\ker B$, the second equation gives $z^\dagger Vy=0$. Thus $y$ is the unique minimizer of the strictly convex quadratic form $y^\dagger Vy$ on the affine space $By=s$. Indeed, every other solution is $y+z$ with $z\in\ker B$, and

$$
(y+z)^\dagger V(y+z)=y^\dagger Vy+z^\dagger Vz.
$$

Consequently

$$
u^\dagger H^+u=s^\dagger x
=y^\dagger B^\dagger x
=-y^\dagger Vy=-\mathcal E_s.
$$

The feasible choice $z=B^+s$ gives $\mathcal E_s\leq W\lVert B^+s\rVert^2$. This argument includes arbitrary kernels of $B$; no inverse of $B$ has been presumed.

### Proof of the absolute inverse bound

First, every positive eigenvalue of $H$ is at least $v$. For an eigenpair with $\lambda>0$, write its vector as $(x,y)$. The vector $y$ is nonzero, and the eigenvalue equations imply

$$
\lambda^2\lVert y\rVert^2
=\lVert By\rVert^2+\lambda y^\dagger Vy
\geq\lambda v\lVert y\rVert^2.
$$

Hence $\lambda\geq v$. This statement allows negative eigenvalues arbitrarily close to zero.

Let $P_s$ be the expectation of the positive part of $H^+$ in $u$, and $N_s$ the expectation of the absolute negative part. Then

$$
P_s-N_s=-\mathcal E_s,
\qquad
M_s=P_s+N_s=\mathcal E_s+2P_s.
$$

The positive-spectrum bound gives $P_s\leq\lVert u\rVert^2/v=\lVert s\rVert^2/v$, proving the theorem.

## Consequence for endpoint states

Let $P_0$ project onto $\ker H$. For vectors $a,b$ supported on the first block, put

$$
s_a=(I-P_{\ker B^\dagger})a,
\qquad
s_b=(I-P_{\ker B^\dagger})b.
$$

The vectors $s_a,s_b$ belong to $\mathrm{ran}B$. Since $|H|^+$ vanishes on the kernel, the theorem bounds

$$
M_a=\langle a|\,|H|^+\,|a\rangle,
\qquad
M_b=\langle b|\,|H|^+\,|b\rangle
$$

by their corresponding source-specific $B^+$ norms. A large system can therefore contain very slow modes while these two local quantities stay small.

## Lemma: a uniform time average

For $T>0$, let

$$
\overline A_T=\frac1T\int_0^T
\langle b|e^{-itH}|a\rangle\,dt,
\qquad
\eta=|\langle b|P_0|a\rangle|.
$$

Then

$$
\left|\overline A_T-\langle b|P_0|a\rangle\right|
\leq\frac{2\sqrt{M_aM_b}}{T}.
$$

In particular, for a uniformly sampled time $t\in[0,T]$,

$$
\mathbb E_t\left[|\langle b|e^{-itH}|a\rangle|^2\right]
\geq\left(\eta-\frac{2\sqrt{M_aM_b}}T\right)_+^2.
$$

Here $(x)_+=\max\{x,0\}$.

### Proof

For a nonzero eigenvalue $\lambda$,

$$
\left|\frac1T\int_0^T e^{-it\lambda}\,dt\right|
\leq\frac{2}{T|\lambda|}.
$$

Expand $H$ in an orthonormal eigenbasis. The nonzero contribution to the averaged endpoint amplitude is bounded by

$$
\frac2T\sum_{\lambda\ne0}
\frac{|\langle b|\lambda\rangle|\,|\langle\lambda|a\rangle|}{|\lambda|}
\leq\frac2T
\sqrt{\sum_{\lambda\ne0}\frac{|\langle\lambda|a\rangle|^2}{|\lambda|}}
\sqrt{\sum_{\lambda\ne0}\frac{|\langle\lambda|b\rangle|^2}{|\lambda|}}.
$$

This is the claimed bound. Finally, $\mathbb E|A_t|^2\geq|\mathbb E A_t|^2$ gives the probability statement. Degenerate eigenspaces cause no change to the argument.

## Relation to established methods

The unchanged opposite-sublattice zero mode is the partial-chiral mechanism established by Poli et al.; source-weighted flow analysis and spectral averaging also have prior uses in quantum walks. The additional statement proved here is the positive-block absolute inverse-moment bound and its consequence for the prescribed microscopic-disorder dynamics. Exact model comparisons and sources are in [Related work](../references/RELATED_WORK.md).

## Why the restrictions matter

The zero projector is protected because the second block is strictly positive. Positivity also isolates the positive spectrum, which converts the signed variational identity into an absolute inverse-moment bound. The proof supplies no analogous uniform claim for indefinite $V$, for $v=0$, or after adding an arbitrary first-block onsite term.

The next step is to show that the [specific graph endpoints](graph_family.md) have small source-specific pseudoinverse norms. That calculation uses the clean adjacency structure; it does not require $V$ to preserve that structure.
