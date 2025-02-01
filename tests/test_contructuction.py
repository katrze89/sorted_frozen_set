from collections.abc import Iterable

from main.sorted_frozen_set import SortedFrozenSet


def test_construct_no_arguments() -> None:
    s = SortedFrozenSet()
    assert isinstance(s._items, Iterable)


def test_construct_empty() -> None:
    SortedFrozenSet([])


def test_construct_from_non_empty_list() -> None:
    SortedFrozenSet([7, 8, 3, 1])


def test_construct_from_iterator() -> None:
    items = [7, 8, 3, 1]
    iterator = iter(items)
    SortedFrozenSet(iterator)
