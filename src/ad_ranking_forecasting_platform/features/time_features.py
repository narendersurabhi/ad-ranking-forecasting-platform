import pandas as pd

def add_time_flags(df: pd.DataFrame, ts_col: str = "timestamp") -> pd.DataFrame:
    out = df.copy()
    dt = pd.to_datetime(out[ts_col])
    out["hour"] = dt.dt.hour
    out["day_of_week"] = dt.dt.dayofweek
    out["is_prime_time"] = out["hour"].between(18, 23).astype(int)
    return out
