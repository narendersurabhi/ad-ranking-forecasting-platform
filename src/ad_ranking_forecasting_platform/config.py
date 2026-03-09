from dataclasses import dataclass


@dataclass
class ScoringWeights:
    alpha: float = 0.6
    beta: float = 0.2
    gamma: float = 0.1
    delta: float = 0.1


@dataclass
class AppConfig:
    top_k_default: int = 3
    scoring: ScoringWeights = ScoringWeights()
