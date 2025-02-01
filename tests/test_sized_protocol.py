from main.sorted_frozen_set import SortedFrozenSet


def test_empty_with_default() -> None:
    s = SortedFrozenSet()
    assert len(s) == 0


def test_empty() -> None:
    s = SortedFrozenSet([])
    assert len(s) == 0


def test_one() -> None:
    s = SortedFrozenSet([22])
    assert len(s) == 1


def test_ten() -> None:
    s = SortedFrozenSet(range(10))
    assert len(s) == 10


def test_with_duplicates() -> None:
    s = SortedFrozenSet([5, 5, 5])
    assert len(s) == 1


def test_with_duplicates_multiple() -> None:
    s = SortedFrozenSet([5, 5, 5, 6, 7, 5, 6])
    assert len(s) == 3
