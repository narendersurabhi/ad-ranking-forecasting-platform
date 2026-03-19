
def pacing_adjustment(pacing_status: str) -> float:
    return {"under_paced": 0.05, "on_track": 0.0, "over_paced": -0.05}.get(pacing_status, 0.0)
