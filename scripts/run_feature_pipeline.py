from ad_ranking_forecasting_platform.data.loaders import load_raw_table
from ad_ranking_forecasting_platform.paths import DATA_PROCESSED
from ad_ranking_forecasting_platform.pipelines.feature_pipeline import run_feature_pipeline


def main():
    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
    out = run_feature_pipeline(
        users=load_raw_table("users"),
        campaigns=load_raw_table("campaigns"),
        impressions=load_raw_table("impressions"),
        events=load_raw_table("events"),
    )
    for name, df in out.items():
        df.to_csv(DATA_PROCESSED / f"{name}_features.csv", index=False)
    print("feature pipeline complete")


if __name__ == "__main__":
    main()
