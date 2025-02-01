from collections.abc import Iterable, Hashable


class SortedFrozenSet:
    def __init__(self, items: Iterable[Hashable] | None = None):
        self._items: list[Hashable] = list(items) if items is not None else list()

    def __contains__(self, item: Hashable) -> bool:
        return item in self._items

    def __len__(self) -> int:
        return len(self._items)
