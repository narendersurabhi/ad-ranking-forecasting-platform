import pandas as pd

from ad_ranking_forecasting_platform.paths import DATA_RAW


def load_raw_table(name: str) -> pd.DataFrame:
    return pd.read_csv(DATA_RAW / f"{name}.csv")
