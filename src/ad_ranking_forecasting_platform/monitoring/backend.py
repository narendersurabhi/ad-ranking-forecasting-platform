from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


class SQLiteObservabilityBackend:
    def __init__(self, db_path: Path):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _init_db(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS metrics (
                    timestamp TEXT,
                    metric_name TEXT,
                    metric_value REAL,
                    tags TEXT
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS drift_reports (
                    timestamp TEXT,
                    feature_name TEXT,
                    psi REAL,
                    passed INTEGER
                )
                """
            )

    def write_metrics(self, metrics: pd.DataFrame) -> None:
        with sqlite3.connect(self.db_path) as conn:
            metrics.to_sql("metrics", conn, if_exists="append", index=False)

    def write_drift_report(self, report: pd.DataFrame) -> None:
        with sqlite3.connect(self.db_path) as conn:
            report.to_sql("drift_reports", conn, if_exists="append", index=False)
