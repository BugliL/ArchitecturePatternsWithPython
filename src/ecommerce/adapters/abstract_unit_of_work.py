import abc
from typing_extensions import Self


class AbstractUnitOfWork(abc.ABC):
    def __enter__(self) -> Self:
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback) -> None:
        if exception_type:
            self.rollback()

        self.commit()

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError
