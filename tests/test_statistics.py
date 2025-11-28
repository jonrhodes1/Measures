from measures import mean, median, mode, variance, stdev, summary
import pytest


def test_mean_and_median():
    values = [1, 2, 3, 4]
    assert mean(values) == 2.5
    assert median(values) == 2.5


def test_mode_with_multiple_modes():
    assert mode([1, 2, 2, 3, 3]) == [2.0, 3.0]


def test_variance_and_stdev_population_and_sample():
    values = [2, 4, 4, 4, 5, 5, 7, 9]
    assert variance(values) == pytest.approx(4.0)
    assert variance(values, sample=True) == pytest.approx(4.5714, rel=1e-3)
    assert stdev(values) == pytest.approx(2.0)
    assert stdev(values, sample=True) == pytest.approx(2.1381, rel=1e-3)


def test_summary_contains_expected_keys():
    values = [1, 2, 2, 3]
    stats = summary(values)
    assert stats["count"] == 4
    assert stats["mean"] == 2.0
    assert stats["median"] == 2.0
    assert stats["mode"] == [2.0]
    assert stats["minimum"] == 1.0
    assert stats["maximum"] == 3.0


def test_validation_errors():
    with pytest.raises(ValueError):
        mean([])
    with pytest.raises(ValueError):
        variance([1], sample=True)
