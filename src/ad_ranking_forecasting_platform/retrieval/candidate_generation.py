import pandas as pd

from ad_ranking_forecasting_platform.targeting.eligibility import enforce_frequency_cap
from ad_ranking_forecasting_platform.targeting.rules import apply_targeting


def generate_candidates(
    campaigns: pd.DataFrame,
    creatives: pd.DataFrame,
    request: dict,
    exposure_counts: pd.DataFrame,
) -> pd.DataFrame:
    eligible_campaigns = apply_targeting(campaigns, request)
    eligible_campaigns = enforce_frequency_cap(eligible_campaigns, exposure_counts)
    cands = creatives.merge(eligible_campaigns, on="campaign_id", how="inner")
    return cands
