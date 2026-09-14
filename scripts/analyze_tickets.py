import csv
from collections import Counter
from pathlib import Path

RESULTS_FILE = Path(__file__).resolve().parents[1] / "results" / "triage-results.csv"


def normalize(value: str) -> str:
    return (value or "").strip()


def main() -> None:
    with RESULTS_FILE.open(encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))

    classifications = Counter(normalize(row["classification"]) for row in rows)
    severities = Counter(normalize(row["severity"]) for row in rows if normalize(row["severity"]) != "None")
    priorities = Counter(normalize(row["priority"]) for row in rows)
    statuses = Counter(normalize(row["status"]) for row in rows)

    escalated = [row for row in rows if normalize(row["escalation"]) not in {"SUPPORT", "PRODUCT"}]
    confirmed_defects = [row for row in rows if normalize(row["classification"]) == "Product defect"]
    high_critical = [
        row for row in confirmed_defects
        if normalize(row["severity"]) in {"High", "Critical"}
    ]

    print("Customer Support QA Lab — Pilot Summary")
    print("=" * 43)
    print(f"Tickets reviewed: {len(rows)}")
    print(f"Confirmed defects: {len(confirmed_defects)}")
    print(f"Engineering/incident escalations: {len(escalated)}")
    print(f"High/Critical defects: {len(high_critical)}")

    print("\nClassification")
    for key, value in classifications.most_common():
        print(f"- {key}: {value}")

    print("\nSeverity")
    for level in ["Critical", "High", "Medium", "Low"]:
        if severities[level]:
            print(f"- {level}: {severities[level]}")

    print("\nPriority")
    for level in ["P0", "P1", "P2", "P3"]:
        if priorities[level]:
            print(f"- {level}: {priorities[level]}")

    print("\nStatus")
    for key, value in statuses.most_common():
        print(f"- {key}: {value}")


if __name__ == "__main__":
    main()
