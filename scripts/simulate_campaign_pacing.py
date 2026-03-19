import pandas as pd

from ad_ranking_forecasting_platform.forecasting.pacing import (
    simulate_budget_burndown,
    summarize_burndown,
)
from ad_ranking_forecasting_platform.paths import ARTIFACTS, DATA_RAW


def main():
    campaigns = pd.read_csv(DATA_RAW / "campaigns.csv")
    simulation = simulate_budget_burndown(campaigns, days=14)
    summary = summarize_burndown(simulation)

    simulation.to_csv(ARTIFACTS / "campaign_pacing_burndown.csv", index=False)
    summary.to_csv(ARTIFACTS / "campaign_pacing_summary.csv", index=False)
    print(summary.head(10).to_string(index=False))


if __name__ == "__main__":
    main()
