from __future__ import annotations

import pandas as pd


def _contains(pipe_list: str, val: str) -> bool:
    return val in pipe_list.split("|")


def apply_targeting(campaigns: pd.DataFrame, request: dict) -> pd.DataFrame:
    df = campaigns.copy()
    df = df[df["remaining_budget"] > 0]
    df = df[df["allowed_regions"].apply(lambda x: _contains(str(x), request["region"]))]
    df = df[df["allowed_devices"].apply(lambda x: _contains(str(x), request["device_type"]))]
    return df
