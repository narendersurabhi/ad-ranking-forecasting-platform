import pandas as pd

from ad_ranking_forecasting_platform.ranking.calibration import (
    expected_calibration_error,
    maximum_calibration_error,
    reliability_table,
)


def test_reliability_table_has_expected_columns():
    y_true = pd.Series([0, 1, 0, 1, 0, 1, 0, 0, 1, 1])
    y_prob = pd.Series([0.05, 0.8, 0.1, 0.7, 0.3, 0.9, 0.2, 0.4, 0.6, 0.95])

    report = reliability_table(y_true, y_prob, n_bins=5)

    assert {"sample_count", "avg_pred", "avg_actual", "calibration_gap"}.issubset(report.columns)
    assert expected_calibration_error(report) >= 0
    assert maximum_calibration_error(report) >= 0
