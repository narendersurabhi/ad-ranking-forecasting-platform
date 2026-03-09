import pandas as pd

from ad_ranking_forecasting_platform.data.synthetic import SyntheticConfig, generate_all
from ad_ranking_forecasting_platform.retrieval.candidate_generation import generate_candidates


def test_candidate_generation():
    ds = generate_all(SyntheticConfig(n_campaigns=30, n_creatives=100, n_impressions=200, n_users=50))
    cands = generate_candidates(ds["campaigns"], ds["creatives"], {"region": "US", "device_type": "ctv"}, pd.DataFrame(columns=["campaign_id", "exposure_count"]))
    assert "creative_id" in cands.columns
