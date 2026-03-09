from ad_ranking_forecasting_platform.data.synthetic import SyntheticConfig, generate_all
from ad_ranking_forecasting_platform.targeting.rules import apply_targeting


def test_targeting_region_device():
    ds = generate_all(SyntheticConfig(n_campaigns=30, n_impressions=200, n_users=50, n_creatives=80))
    out = apply_targeting(ds["campaigns"], {"region": "US", "device_type": "ctv"})
    assert not out.empty
