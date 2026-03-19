import pandas as pd

from ad_ranking_forecasting_platform.monitoring import run_drift_checks


def test_run_drift_checks_flags_large_shift():
    reference = pd.DataFrame({"x": [0.1] * 100, "y": [0, 1] * 50})
    current = pd.DataFrame({"x": [0.9] * 100, "y": [0, 1] * 50})

    report = run_drift_checks(reference, current, threshold=0.05)

    assert "x" in set(report["feature_name"])
    assert (report["passed"] == 0).any()
