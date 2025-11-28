"""Core statistical calculations used throughout the project."""

from __future__ import annotations

from collections import Counter
from typing import Iterable, List, Sequence
import math


Number = float | int


def _validate_input(values: Sequence[Number] | Iterable[Number]) -> List[float]:
    collected = [float(value) for value in values]
    if not collected:
        raise ValueError("At least one value is required to compute statistics.")
    return collected


def mean(values: Sequence[Number] | Iterable[Number]) -> float:
    """Return the arithmetic mean of the provided values.

    Raises:
        ValueError: If *values* is empty.
    """

    collected = _validate_input(values)
    return sum(collected) / len(collected)


def median(values: Sequence[Number] | Iterable[Number]) -> float:
    """Return the median of the provided values."""

    collected = sorted(_validate_input(values))
    mid = len(collected) // 2
    if len(collected) % 2:
        return collected[mid]
    return (collected[mid - 1] + collected[mid]) / 2


def mode(values: Sequence[Number] | Iterable[Number]) -> List[float]:
    """Return the mode(s) of the provided values.

    The return value is a list because there can be multiple equally common modes.
    """

    collected = _validate_input(values)
    counts = Counter(collected)
    highest = max(counts.values())
    modes = [value for value, count in counts.items() if count == highest]
    return sorted(modes)


def variance(values: Sequence[Number] | Iterable[Number], sample: bool = False) -> float:
    """Return the variance of the provided values.

    Args:
        values: A sequence of numbers.
        sample: If ``True``, compute the sample variance. Defaults to population variance.

    Raises:
        ValueError: If fewer than two values are provided for a sample variance.
    """

    collected = _validate_input(values)
    if sample and len(collected) < 2:
        raise ValueError("Sample variance requires at least two values.")

    mean_value = mean(collected)
    total = sum((value - mean_value) ** 2 for value in collected)
    divisor = len(collected) - 1 if sample else len(collected)
    return total / divisor


def stdev(values: Sequence[Number] | Iterable[Number], sample: bool = False) -> float:
    """Return the standard deviation of the provided values."""

    return math.sqrt(variance(values, sample=sample))


def summary(values: Sequence[Number] | Iterable[Number]) -> dict[str, float | list[float]]:
    """Return a statistical summary of *values*.

    The summary includes count, mean, median, mode, variance, standard deviation,
    minimum, and maximum.
    """

    collected = _validate_input(values)
    return {
        "count": len(collected),
        "mean": mean(collected),
        "median": median(collected),
        "mode": mode(collected),
        "variance": variance(collected),
        "stdev": stdev(collected),
        "minimum": min(collected),
        "maximum": max(collected),
    }
