import pandas as pd

from ad_ranking_forecasting_platform.paths import ARTIFACTS, DATA_PROCESSED, DATA_RAW
from ad_ranking_forecasting_platform.ranking.ctr_model import save_model, train_ctr_model


def main():
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    campaigns = pd.read_csv(DATA_PROCESSED / "campaigns_features.csv")
    impressions = pd.read_csv(DATA_RAW / "impressions.csv")
    events = pd.read_csv(DATA_RAW / "events.csv")
    train_df = impressions[["request_id", "placement_id", "device_type", "region"]].merge(events[["request_id", "click"]], on="request_id")
    train_df = train_df.assign(campaign_id=campaigns["campaign_id"].sample(len(train_df), replace=True).values)
    train_df = train_df.merge(campaigns[["campaign_id", "bid", "pacing_ratio"]], on="campaign_id", how="left")
    train_df["quality_score"] = 0.7
    model = train_ctr_model(train_df, train_df["click"])
    save_model(model, ARTIFACTS / "ctr_model.joblib")


if __name__ == "__main__":
    main()
