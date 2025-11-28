"""Command-line interface for the Measures toolkit."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable, List

from .statistics import summary


def _parse_tokens(raw_values: Iterable[str]) -> List[float]:
    values: List[float] = []
    for token in raw_values:
        cleaned = token.replace(",", " ")
        for part in cleaned.split():
            if not part:
                continue
            try:
                values.append(float(part))
            except ValueError as exc:  # pragma: no cover - helpful error path
                raise argparse.ArgumentTypeError(f"Invalid number: {part}") from exc
    return values


def _load_file_values(path: Path) -> List[float]:
    if not path.exists():
        raise argparse.ArgumentTypeError(f"File not found: {path}")
    content = path.read_text(encoding="utf-8")
    return _parse_tokens([content])


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compute summary statistics for numbers.")
    parser.add_argument(
        "numbers",
        nargs="*",
        help="Numbers to summarize. You can separate values with spaces or commas.",
    )
    parser.add_argument(
        "-f",
        "--file",
        type=Path,
        help="Optional path to a file containing numbers.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Render the summary as JSON instead of human-readable text.",
    )
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    values = _parse_tokens(args.numbers)
    if args.file:
        values.extend(_load_file_values(args.file))

    if not values:
        parser.error("Provide numbers as arguments or via --file.")

    stats = summary(values)
    if args.json:
        print(json.dumps(stats, indent=2))
    else:
        print("Summary statistics:")
        print(f"  Count:   {stats['count']}")
        print(f"  Mean:    {stats['mean']:.3f}")
        print(f"  Median:  {stats['median']:.3f}")
        print(f"  Mode:    {', '.join(str(value) for value in stats['mode'])}")
        print(f"  Variance:{stats['variance']:.3f}")
        print(f"  Stdev:   {stats['stdev']:.3f}")
        print(f"  Min:     {stats['minimum']}")
        print(f"  Max:     {stats['maximum']}")

    return 0


if __name__ == "__main__":  # pragma: no cover - entrypoint
    raise SystemExit(main())
