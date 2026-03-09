from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta

import numpy as np
import pandas as pd


@dataclass
class SyntheticConfig:
    seed: int = 7
    n_users: int = 7000
    n_campaigns: int = 600
    n_creatives: int = 3000
    n_impressions: int = 100000


def _rng(seed: int) -> np.random.Generator:
    return np.random.default_rng(seed)


def generate_all(cfg: SyntheticConfig) -> dict[str, pd.DataFrame]:
    rng = _rng(cfg.seed)
    users = pd.DataFrame(
        {
            "user_id": [f"u_{i}" for i in range(cfg.n_users)],
            "age_bucket": rng.choice(["18_24", "25_34", "35_49", "50_plus"], cfg.n_users),
            "region": rng.choice(["US", "CA", "UK"], cfg.n_users, p=[0.75, 0.15, 0.10]),
            "device_type": rng.choice(["ctv", "mobile", "web"], cfg.n_users, p=[0.5, 0.3, 0.2]),
            "subscription_tier": rng.choice(["ad_supported", "premium"], cfg.n_users, p=[0.8, 0.2]),
            "content_preferences": rng.choice(["sports", "kids", "news", "entertainment"], cfg.n_users),
            "prior_engagement_rate": rng.uniform(0.05, 0.8, cfg.n_users).round(3),
        }
    )
    campaigns = pd.DataFrame(
        {
            "campaign_id": [f"camp_{i}" for i in range(cfg.n_campaigns)],
            "advertiser_vertical": rng.choice(["retail", "finance", "gaming", "auto"], cfg.n_campaigns),
            "objective": rng.choice(["clicks", "conversions", "awareness"], cfg.n_campaigns),
            "budget": rng.integers(5000, 250000, cfg.n_campaigns),
            "daily_cap": rng.integers(500, 15000, cfg.n_campaigns),
            "bid": rng.uniform(0.5, 12.0, cfg.n_campaigns).round(2),
            "allowed_regions": rng.choice(["US", "CA", "UK", "US|CA"], cfg.n_campaigns),
            "allowed_devices": rng.choice(["ctv", "mobile", "web", "ctv|mobile"], cfg.n_campaigns),
            "frequency_cap": rng.integers(2, 8, cfg.n_campaigns),
            "pacing_status": rng.choice(["under_paced", "on_track", "over_paced"], cfg.n_campaigns),
        }
    )
    campaigns["remaining_budget"] = campaigns["budget"] * rng.uniform(0.1, 1.0, cfg.n_campaigns)
    campaigns["start_date"] = "2026-01-01"
    campaigns["end_date"] = "2026-12-31"
    creatives = pd.DataFrame(
        {
            "creative_id": [f"cr_{i}" for i in range(cfg.n_creatives)],
            "campaign_id": rng.choice(campaigns["campaign_id"], cfg.n_creatives),
            "format": rng.choice(["video", "banner"], cfg.n_creatives, p=[0.9, 0.1]),
            "duration": rng.choice([6, 15, 30], cfg.n_creatives),
            "category": rng.choice(["sports", "entertainment", "general"], cfg.n_creatives),
            "quality_score": rng.uniform(0.3, 1.0, cfg.n_creatives).round(3),
        }
    )
    content = pd.DataFrame(
        {
            "content_id": [f"content_{i}" for i in range(2500)],
            "genre": rng.choice(["sports", "drama", "news", "kids", "comedy"], 2500),
            "content_type": rng.choice(["movie", "series", "live"], 2500),
            "duration_bucket": rng.choice(["short", "medium", "long"], 2500),
            "audience_segment": rng.choice(["family", "young_adults", "broad"], 2500),
            "is_live": rng.choice([0, 1], 2500, p=[0.8, 0.2]),
            "is_sports": rng.choice([0, 1], 2500, p=[0.7, 0.3]),
        }
    )
    start = datetime(2026, 3, 1)
    ts = [start + timedelta(minutes=int(x)) for x in rng.integers(0, 60 * 24 * 30, cfg.n_impressions)]
    impressions = pd.DataFrame(
        {
            "request_id": [f"req_{i}" for i in range(cfg.n_impressions)],
            "timestamp": ts,
            "user_id": rng.choice(users["user_id"], cfg.n_impressions),
            "content_id": rng.choice(content["content_id"], cfg.n_impressions),
            "placement_id": rng.choice(["pre_roll", "mid_roll", "pause"], cfg.n_impressions),
            "device_type": rng.choice(["ctv", "mobile", "web"], cfg.n_impressions),
            "region": rng.choice(["US", "CA", "UK"], cfg.n_impressions, p=[0.75, 0.15, 0.10]),
            "session_id": [f"s_{i//3}" for i in range(cfg.n_impressions)],
        }
    )
    impressions["hour"] = pd.to_datetime(impressions["timestamp"]).dt.hour
    impressions["time_of_day"] = np.where(impressions["hour"].between(18, 23), "evening", "day")
    events = impressions[["request_id", "user_id", "content_id", "placement_id", "device_type", "region"]].copy()
    p_click = 0.02 + 0.015 * (events["device_type"] == "mobile") + 0.01 * (events["placement_id"] == "pre_roll")
    events["click"] = rng.binomial(1, np.clip(p_click, 0.01, 0.15))
    events["conversion"] = rng.binomial(1, np.where(events["click"] == 1, 0.08, 0.002))
    events["impression"] = 1
    events["completion"] = rng.binomial(1, 0.6, cfg.n_impressions)
    events["skip"] = rng.binomial(1, 0.2, cfg.n_impressions)
    return {
        "users": users,
        "campaigns": campaigns,
        "creatives": creatives,
        "content": content,
        "impressions": impressions,
        "events": events,
    }
