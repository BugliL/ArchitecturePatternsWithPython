from .abstract_unit_of_work import AbstractUnitOfWork
from .django_repository import DjangoRepository
from django.db import transaction
from typing_extensions import Self


class DjangoUnitOfWork(AbstractUnitOfWork):
    def __init__(self, repository: DjangoRepository):
        self.repository = repository
        self._transaction_context = None

    def __enter__(self) -> Self:
        self._transaction_context = transaction.atomic()
        self._transaction_context.__enter__()
        return super().__enter__()

    def __exit__(self, exception_type, exception_value, exception_traceback) -> None:
        commit_or_rollback = self.commit if exception_type is None else self.rollback

        if self._transaction_context is not None:
            commit_or_rollback()
            super().__exit__(exception_type, exception_value, exception_traceback)

        self._transaction_context = None

    def commit(self) -> None:
        for item in self.repository.list():
            self.repository.update(item)

    def rollback(self) -> None:
        pass
