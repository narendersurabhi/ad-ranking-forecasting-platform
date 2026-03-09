import pandas as pd

from ad_ranking_forecasting_platform.features.campaign_features import build_campaign_features
from ad_ranking_forecasting_platform.features.impression_features import build_impression_features
from ad_ranking_forecasting_platform.features.user_features import build_user_history


def run_feature_pipeline(users: pd.DataFrame, campaigns: pd.DataFrame, impressions: pd.DataFrame, events: pd.DataFrame):
    return {
        "users": build_user_history(users, events),
        "campaigns": build_campaign_features(campaigns),
        "impressions": build_impression_features(impressions),
    }
