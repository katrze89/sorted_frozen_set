import pytest

from main.sorted_frozen_set import SortedFrozenSet


@pytest.fixture
def sorted_frozen_set():
    return SortedFrozenSet([6, 7, 3, 9])


def test_positive_contained(sorted_frozen_set: SortedFrozenSet) -> None:
    assert 3 in sorted_frozen_set


def test_negative_contained(sorted_frozen_set: SortedFrozenSet) -> None:
    assert not (15 in sorted_frozen_set)  # noqa: E713


def test_positive_not_contained(sorted_frozen_set: SortedFrozenSet) -> None:
    assert 15 not in sorted_frozen_set


def test_negative_not_contained(sorted_frozen_set: SortedFrozenSet) -> None:
    assert not (3 not in sorted_frozen_set)
