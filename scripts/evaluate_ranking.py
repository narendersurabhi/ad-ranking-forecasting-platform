import json

import joblib
import pandas as pd
from sklearn.metrics import log_loss, roc_auc_score

from ad_ranking_forecasting_platform.paths import ARTIFACTS, DATA_PROCESSED, DATA_RAW


def main():
    ctr = joblib.load(ARTIFACTS / "ctr_model.joblib")
    campaigns = pd.read_csv(DATA_PROCESSED / "campaigns_features.csv")
    impressions = pd.read_csv(DATA_RAW / "impressions.csv").head(5000)
    events = pd.read_csv(DATA_RAW / "events.csv").head(5000)
    df = impressions[["request_id", "placement_id", "device_type", "region"]].merge(events[["request_id", "click"]], on="request_id")
    df = df.assign(campaign_id=campaigns["campaign_id"].sample(len(df), replace=True).values)
    df = df.merge(campaigns[["campaign_id", "bid", "pacing_ratio"]], on="campaign_id", how="left")
    df["quality_score"] = 0.7
    p = ctr.predict_proba(df[["device_type", "region", "placement_id", "bid", "quality_score", "pacing_ratio"]])[:,1]
    metrics = {"auc": float(roc_auc_score(df["click"], p)), "log_loss": float(log_loss(df["click"], p))}
    (ARTIFACTS / "ranking_eval.json").write_text(json.dumps(metrics, indent=2))
    print(metrics)


if __name__ == "__main__":
    main()
