from ad_ranking_forecasting_platform.data.synthetic import SyntheticConfig, generate_all


def test_generate_shapes():
    ds = generate_all(SyntheticConfig(n_impressions=1000, n_users=200, n_campaigns=50, n_creatives=150))
    assert len(ds["impressions"]) == 1000
    assert {"users", "campaigns", "creatives", "content", "impressions", "events"}.issubset(ds.keys())
