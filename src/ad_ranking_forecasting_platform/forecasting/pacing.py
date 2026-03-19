from __future__ import annotations

import pandas as pd


def simulate_budget_burndown(campaigns: pd.DataFrame, days: int = 7) -> pd.DataFrame:
    """Simulate daily spend and remaining budget trajectories."""
    rows: list[dict] = []

    for _, campaign in campaigns.iterrows():
        remaining = float(campaign["remaining_budget"])
        daily_cap = float(campaign["daily_cap"])
        total_budget = float(campaign["budget"])
        pacing_status = campaign.get("pacing_status", "on_track")

        burn_multiplier = {
            "under_paced": 0.75,
            "on_track": 1.0,
            "over_paced": 1.2,
        }.get(pacing_status, 1.0)

        for day in range(1, days + 1):
            planned_daily = min(daily_cap * burn_multiplier, remaining)
            spend = max(planned_daily, 0.0)
            remaining = max(remaining - spend, 0.0)
            rows.append(
                {
                    "campaign_id": campaign["campaign_id"],
                    "day": day,
                    "daily_spend": round(spend, 2),
                    "remaining_budget": round(remaining, 2),
                    "burn_rate": round(spend / max(total_budget, 1.0), 6),
                    "burn_pct_total": round((total_budget - remaining) / max(total_budget, 1.0), 6),
                    "is_budget_exhausted": int(remaining <= 0.0),
                }
            )
    return pd.DataFrame(rows)


def summarize_burndown(simulation: pd.DataFrame) -> pd.DataFrame:
    """Aggregate campaign-level pacing summary from simulated burndown."""
    latest = simulation.sort_values(["campaign_id", "day"]).groupby("campaign_id", as_index=False).tail(1)
    totals = simulation.groupby("campaign_id", as_index=False).agg(total_spend=("daily_spend", "sum"))
    summary = latest.merge(totals, on="campaign_id", how="left")
    return summary[
        [
            "campaign_id",
            "total_spend",
            "remaining_budget",
            "burn_pct_total",
            "is_budget_exhausted",
        ]
    ].sort_values("burn_pct_total", ascending=False)
