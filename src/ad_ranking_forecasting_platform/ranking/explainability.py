def reason_codes(row: dict) -> list[str]:
    reasons = []
    if row.get("campaign_historical_ctr", 0) > 0.03:
        reasons.append("high_historical_ctr")
    if row.get("bid", 0) > 8:
        reasons.append("strong_bid")
    if row.get("pacing_status") == "under_paced":
        reasons.append("under_paced_campaign")
    if row.get("is_live", 0) == 1:
        reasons.append("live_event_match")
    if not reasons:
        reasons.append("content_affinity")
    return reasons
