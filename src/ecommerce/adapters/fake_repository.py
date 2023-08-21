from .abstract_repository import AbstractRepository


class FakeRepository(AbstractRepository):
    def __init__(self, items):
        self._items = set(items)

    def add(self, item):
        self._items.add(item)

    def get(self, reference):
        return next((item for item in self._items if item.reference == reference), None)

    def list(self):
        return list(self._items)
