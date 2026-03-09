import joblib
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


FEATURES = ["placement_id", "region", "device_type", "hour", "day", "lag_1", "rolling_3"]


def train_forecast_model(df):
    pre = ColumnTransformer(
        [("cat", OneHotEncoder(handle_unknown="ignore"), ["placement_id", "region", "device_type"])],
        remainder="passthrough",
    )
    model = Pipeline([("pre", pre), ("reg", RandomForestRegressor(n_estimators=60, random_state=7))])
    model.fit(df[FEATURES], df["impressions"])
    return model


def save_forecast_model(model, path):
    joblib.dump(model, path)
