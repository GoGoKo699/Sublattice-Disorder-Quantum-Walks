"""Run the finite scientific diagnostics and compare saved reference outputs."""
from __future__ import annotations

import json
import math
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent


def compare(actual, expected, where="root"):
    if isinstance(expected, dict):
        assert isinstance(actual, dict) and actual.keys() == expected.keys(), where
        for key in expected:
            compare(actual[key], expected[key], f"{where}.{key}")
    elif isinstance(expected, list):
        assert isinstance(actual, list) and len(actual) == len(expected), where
        for i, (a, e) in enumerate(zip(actual, expected)):
            compare(a, e, f"{where}[{i}]")
    elif isinstance(expected, (int, float)) and not isinstance(expected, bool):
        assert math.isclose(actual, expected, rel_tol=5e-7, abs_tol=5e-10), (
            where, actual, expected
        )
    else:
        assert actual == expected, (where, actual, expected)


def run(filename):
    result = subprocess.run(
        [sys.executable, str(HERE / filename)],
        cwd=HERE.parent, check=True, capture_output=True, text=True,
    )
    return json.loads(result.stdout)


def main():
    physical = run("physical_graph.py")
    compare(physical, json.loads((HERE / "physical_graph_expected.json").read_text()))
    inverse = run("inverse_moment_check.py")
    assert inverse["passed"] is True
    precision = run("precision_resource_check.py")
    compare(precision, json.loads((HERE / "precision_resource_check.json").read_text()))
    print(json.dumps({
        "passed": True,
        "physical_vertices": physical["N"],
        "physical_layer_invariance_residual_after_disorder": physical["disordered_equitable_residual"],
        "inverse_moment_cases": len(inverse["records"]),
        "scope": "Finite floating-point model, inverse-moment and precision checks; general proofs, classical asymptotics and novelty are assessed in the written account.",
    }, indent=2))


if __name__ == "__main__":
    main()
