def cold_start_campaigns() -> list[dict]:
    return [{"campaign_id": "house_1", "creative_id": "house_cr_1", "score": 0.1, "ctr_score": 0.01, "cvr_score": 0.001, "reason_codes": ["cold_start_fallback"]}]


def sparse_forecast_baseline() -> list[dict]:
    return [{"bucket_start": "2026-03-10T18:00:00", "predicted_impressions": 1000}]
