
import pandas as pd

from ad_ranking_forecasting_platform.monitoring import (
    SQLiteObservabilityBackend,
    run_drift_checks,
)
from ad_ranking_forecasting_platform.paths import ARTIFACTS, DATA_RAW


def main() -> int:
    events = pd.read_csv(DATA_RAW / "events.csv")
    midpoint = len(events) // 2
    reference = events.iloc[:midpoint]
    current = events.iloc[midpoint:]

    report = run_drift_checks(reference, current, threshold=0.2)
    report_path = ARTIFACTS / "drift_report.csv"
    report.to_csv(report_path, index=False)

    backend = SQLiteObservabilityBackend(ARTIFACTS / "observability.db")
    backend.write_drift_report(report)

    if report.empty:
        print("No numeric columns available for drift checks.")
        return 0

    failing = report[report["passed"] == 0]
    print(report.to_string(index=False))
    if not failing.empty:
        print("\nDrift checks failed for:", ", ".join(failing["feature_name"]))
        return 1

    print(f"\nDrift checks passed. Report saved to {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
