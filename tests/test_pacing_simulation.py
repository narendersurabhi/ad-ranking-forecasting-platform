import pandas as pd

from ad_ranking_forecasting_platform.forecasting.pacing import (
    simulate_budget_burndown,
    summarize_burndown,
)


def test_simulate_budget_burndown_respects_remaining_budget():
    campaigns = pd.DataFrame(
        [
            {
                "campaign_id": "camp_1",
                "budget": 1000,
                "remaining_budget": 300,
                "daily_cap": 100,
                "pacing_status": "on_track",
            }
        ]
    )

    sim = simulate_budget_burndown(campaigns, days=5)

    assert sim["remaining_budget"].iloc[-1] == 0
    assert sim["daily_spend"].sum() == 300

    summary = summarize_burndown(sim)
    assert summary["is_budget_exhausted"].iloc[0] == 1
