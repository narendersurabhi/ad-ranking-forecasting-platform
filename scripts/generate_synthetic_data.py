from ad_ranking_forecasting_platform.data.synthetic import SyntheticConfig, generate_all
from ad_ranking_forecasting_platform.paths import DATA_RAW


def main():
    DATA_RAW.mkdir(parents=True, exist_ok=True)
    ds = generate_all(SyntheticConfig())
    for name, df in ds.items():
        df.to_csv(DATA_RAW / f"{name}.csv", index=False)
    print("generated raw data")


if __name__ == "__main__":
    main()
