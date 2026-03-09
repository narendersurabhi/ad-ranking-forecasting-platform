from pathlib import Path

from ad_ranking_forecasting_platform.registry.model_registry import LocalModelRegistry


def test_registry(tmp_path: Path):
    reg = LocalModelRegistry(tmp_path / "registry.json")
    reg.register("m", "v1", "dev", "/tmp/m", {"auc": 1.0}, {})
    assert len(reg.list_records()) == 1
