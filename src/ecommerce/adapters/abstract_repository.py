import abc

from .domain_model import DomainModel


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, batch: DomainModel):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> DomainModel:
        raise NotImplementedError
