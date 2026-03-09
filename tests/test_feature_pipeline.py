from ad_ranking_forecasting_platform.data.synthetic import SyntheticConfig, generate_all
from ad_ranking_forecasting_platform.pipelines.feature_pipeline import run_feature_pipeline


def test_feature_pipeline_outputs():
    ds = generate_all(SyntheticConfig(n_impressions=1000, n_users=200, n_campaigns=50, n_creatives=150))
    out = run_feature_pipeline(ds["users"], ds["campaigns"], ds["impressions"], ds["events"])
    assert "pacing_ratio" in out["campaigns"].columns
