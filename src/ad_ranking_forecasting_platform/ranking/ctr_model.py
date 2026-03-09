from __future__ import annotations

import joblib
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


FEATURES = ["device_type", "region", "placement_id", "bid", "quality_score", "pacing_ratio"]


def train_ctr_model(X, y):
    pre = ColumnTransformer(
        [("cat", OneHotEncoder(handle_unknown="ignore"), ["device_type", "region", "placement_id"])],
        remainder="passthrough",
    )
    pipe = Pipeline([("pre", pre), ("model", GradientBoostingClassifier(random_state=7))])
    pipe.fit(X[FEATURES], y)
    return pipe


def save_model(model, path):
    joblib.dump(model, path)


def load_model(path):
    return joblib.load(path)
