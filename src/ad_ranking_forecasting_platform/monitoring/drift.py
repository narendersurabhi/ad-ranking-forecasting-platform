from __future__ import annotations

from datetime import datetime, timezone

import numpy as np
import pandas as pd


def population_stability_index(reference: pd.Series, current: pd.Series, bins: int = 10) -> float:
    ref = reference.dropna().astype(float)
    cur = current.dropna().astype(float)
    if ref.empty or cur.empty:
        return 0.0

    breakpoints = np.unique(np.quantile(ref, np.linspace(0, 1, bins + 1)))
    if len(breakpoints) < 3:
        return 0.0

    ref_hist, _ = np.histogram(ref, bins=breakpoints)
    cur_hist, _ = np.histogram(cur, bins=breakpoints)

    ref_pct = np.clip(ref_hist / max(ref_hist.sum(), 1), 1e-6, None)
    cur_pct = np.clip(cur_hist / max(cur_hist.sum(), 1), 1e-6, None)
    return float(np.sum((cur_pct - ref_pct) * np.log(cur_pct / ref_pct)))


def run_drift_checks(reference_df: pd.DataFrame, current_df: pd.DataFrame, threshold: float = 0.2) -> pd.DataFrame:
    rows: list[dict] = []
    ts = datetime.now(timezone.utc).isoformat()
    numeric_cols = [c for c in reference_df.columns if pd.api.types.is_numeric_dtype(reference_df[c])]

    for col in numeric_cols:
        if col not in current_df.columns:
            continue
        psi = population_stability_index(reference_df[col], current_df[col])
        rows.append(
            {
                "timestamp": ts,
                "feature_name": col,
                "psi": round(psi, 6),
                "passed": int(psi <= threshold),
            }
        )
    return pd.DataFrame(rows)
