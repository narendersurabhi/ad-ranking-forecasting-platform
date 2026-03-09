import pandas as pd


def validate_non_empty(df: pd.DataFrame, name: str) -> None:
    if df.empty:
        raise ValueError(f"{name} cannot be empty")
