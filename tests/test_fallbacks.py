from ad_ranking_forecasting_platform.inference.fallback import cold_start_campaigns


def test_cold_start():
    assert cold_start_campaigns()[0]["campaign_id"] == "house_1"
