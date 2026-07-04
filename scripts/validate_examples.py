from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]

VALIDATION_TARGETS = [
    (
        "Allocation Readiness Record",
        ROOT / "schemas" / "allocation-readiness-record.schema.json",
        ROOT / "examples" / "allocation-readiness-record.example.yaml",
    ),
    (
        "Allocation Blocking Rule Set",
        ROOT / "schemas" / "allocation-blocking-rule-set.schema.json",
        ROOT / "examples" / "allocation-blocking-rule-set.example.yaml",
    ),
    (
        "Contribution Claim Bundle",
        ROOT / "schemas" / "contribution-claim-bundle.schema.json",
        ROOT / "examples" / "contribution-claim-bundle.example.yaml",
    ),
    (
        "Review and Dispute Gate",
        ROOT / "schemas" / "review-dispute-gate.schema.json",
        ROOT / "examples" / "review-dispute-gate.example.yaml",
    ),
]

def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML object at the root.")

    return data


def format_error_path(error) -> str:
    if not error.absolute_path:
        return "<root>"

    return ".".join(str(part) for part in error.absolute_path)


def validate_target(
    label: str,
    schema_path: Path,
    example_path: Path,
) -> bool:
    print(f"[validate] {label}")
    print(f"  schema : {schema_path.relative_to(ROOT)}")
    print(f"  example: {example_path.relative_to(ROOT)}")

    schema = load_json(schema_path)
    example = load_yaml(example_path)

    validator = Draft202012Validator(
        schema,
        format_checker=FormatChecker(),
    )

    errors = sorted(
        validator.iter_errors(example),
        key=lambda error: list(error.absolute_path),
    )

    if errors:
        for error in errors:
            path = format_error_path(error)
            print(f"Error: {path}: {error.message}")

        return False

    print(f"[ok] {example_path.name} is valid")
    return True


def main() -> int:
    all_valid = True

    for label, schema_path, example_path in VALIDATION_TARGETS:
        try:
            is_valid = validate_target(
                label,
                schema_path,
                example_path,
            )
        except Exception as exc:
            print(f"Error: {exc}")
            is_valid = False

        all_valid = all_valid and is_valid

    if all_valid:
        print("[success] All examples are valid.")
        return 0

    print("[failed] Validation errors detected.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
