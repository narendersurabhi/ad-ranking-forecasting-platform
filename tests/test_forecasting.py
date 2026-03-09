from ad_ranking_forecasting_platform.data.synthetic import SyntheticConfig, generate_all
from ad_ranking_forecasting_platform.forecasting.dataset import build_forecast_dataset


def test_forecast_dataset():
    ds = generate_all(SyntheticConfig(n_impressions=1000, n_users=100, n_campaigns=20, n_creatives=50))
    out = build_forecast_dataset(ds["impressions"])
    assert "rolling_3" in out.columns
