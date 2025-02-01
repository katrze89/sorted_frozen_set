from collections.abc import Iterable, Iterator

from main.dtypes import SupportsRichComparison


class SortedFrozenSet:
    def __init__(self, items: Iterable[SupportsRichComparison] | None = None):
        self._items: list[SupportsRichComparison] = (
            sorted(set(items)) if items is not None else []
        )

    def __contains__(self, item: SupportsRichComparison) -> bool:
        return item in self._items

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[SupportsRichComparison]:
        return iter(self._items)
