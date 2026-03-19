from __future__ import annotations

import pandas as pd


def reliability_table(y_true, y_prob, n_bins: int = 10) -> pd.DataFrame:
    """Build a reliability table for binary probability predictions."""
    frame = pd.DataFrame({"y_true": y_true, "y_prob": y_prob}).dropna()
    frame["bin"] = pd.qcut(frame["y_prob"], q=n_bins, duplicates="drop")

    grouped = (
        frame.groupby("bin", observed=True)
        .agg(
            sample_count=("y_true", "size"),
            avg_pred=("y_prob", "mean"),
            avg_actual=("y_true", "mean"),
        )
        .reset_index()
    )
    grouped["calibration_gap"] = grouped["avg_pred"] - grouped["avg_actual"]
    grouped["bin_lower"] = grouped["bin"].apply(lambda interval: float(interval.left))
    grouped["bin_upper"] = grouped["bin"].apply(lambda interval: float(interval.right))
    return grouped.drop(columns=["bin"])


def expected_calibration_error(reliability: pd.DataFrame) -> float:
    total = reliability["sample_count"].sum()
    if total == 0:
        return 0.0
    weights = reliability["sample_count"] / total
    return float((weights * reliability["calibration_gap"].abs()).sum())


def maximum_calibration_error(reliability: pd.DataFrame) -> float:
    if reliability.empty:
        return 0.0
    return float(reliability["calibration_gap"].abs().max())
