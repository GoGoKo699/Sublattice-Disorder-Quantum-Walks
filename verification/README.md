# Finite scientific verification

Run from the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The supplied dependency pins match the checked environment: Python 3.12.14, NumPy 2.3.5 and SciPy 1.17.0. The scripts use seeded random generators and explicit small matrices. They do not enumerate an exponentially large oracle input for the algorithm.

| Check | What is reconstructed | Expected observation |
|---|---|---|
| [Physical graph](physical_graph.py) | A simple 304-vertex six-regular graph, its clean layer subspace, iid binary odd potentials, kernel, endpoint pseudoinverse vectors and spectral time average | Clean invariance residual near roundoff; disordered residual about 1.112; endpoint zero-projector magnitude about 0.22727; local moment and time-average bounds hold |
| [Inverse moment](inverse_moment_check.py) | Dense rectangular block examples with small irrelevant singular directions and nonuniform positive odd terms | The full nonzero gap shrinks to about $`6\times10^{-11}`$ while endpoint inverse moments stay bounded; signed energy and absolute-moment inequalities hold |
| [Precision](precision_resource_check.py) | A 64-vertex graph, nonbinary positive values, dyadic time sampling, rounding and restart budgets | Grid and rounded-H success exceed the conservative per-run bound; budgets hold at several depths and failure targets |

The physical and precision reference outputs are [physical_graph_expected.json](physical_graph_expected.json) and [precision_resource_check.json](precision_resource_check.json). The runner compares numerical outputs with a relative tolerance of $`5\times10^{-7}`$ and absolute tolerance of $`5\times10^{-10}`$. Each script also checks its stated mathematical identities and inequalities directly.

The tiny-gap example removes the analytically known exact kernel before numerical diagonalization. Otherwise roundoff can mix that kernel with very small nonzero modes and corrupt inverse spectral moments. No claim of interval arithmetic or formally certified numerical enclosure is made.

The general block theorem, the endpoint-flow construction and the classical query lower bound rest on the proofs under [science/](../science/model.md). These finite checks do not certify asymptotic hardness, exhaustive novelty, a compiled sparse-simulation circuit, or a physical implementation.
