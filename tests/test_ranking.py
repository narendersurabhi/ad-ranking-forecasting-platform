
from ad_ranking_forecasting_platform.config import ScoringWeights
from ad_ranking_forecasting_platform.data.synthetic import SyntheticConfig, generate_all
from ad_ranking_forecasting_platform.features.campaign_features import build_campaign_features
from ad_ranking_forecasting_platform.ranking.ctr_model import train_ctr_model
from ad_ranking_forecasting_platform.ranking.scorer import score_candidates


def test_ranking_scores():
    ds = generate_all(SyntheticConfig(n_campaigns=20, n_creatives=80, n_impressions=500, n_users=100))
    campaigns = build_campaign_features(ds["campaigns"])
    train = ds["impressions"][["placement_id", "device_type", "region"]].copy()
    train["bid"] = 1.0
    train["quality_score"] = 0.8
    train["pacing_ratio"] = 0.5
    model = train_ctr_model(train, ds["events"]["click"])
    cands = ds["creatives"].merge(campaigns, on="campaign_id").head(10)
    cands = cands.assign(device_type="ctv", region="US", placement_id="pre_roll")
    out = score_candidates(cands, model, model, ScoringWeights())
    assert "final_score" in out.columns
