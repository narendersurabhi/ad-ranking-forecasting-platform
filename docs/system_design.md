# System design

## Retrieval vs ranking
Retrieval narrows campaigns to eligible candidates using hard constraints. Ranking orders only the eligible set using predicted value and business-adjusted score.

## Why business rules coexist with ML
ML scores optimize engagement probability. Rules enforce delivery obligations such as budget caps, pacing, and policy constraints.

## Pacing and budget constraints
Campaigns can be under-paced or over-paced. Reranking nudges under-paced campaigns and protects remaining budget.

## Batch vs real-time
Batch jobs generate synthetic data, features, models, and forecasts. Real-time API loads artifacts and returns low latency scores.

## Forecasting role
Forecasting predicts supply by placement and context buckets for next 24h and 7d planning windows.

## Scale and latency tradeoffs
Retrieval uses deterministic filters to reduce model scoring volume. Ranking then applies lightweight gradient boosting models for fast API responses.
