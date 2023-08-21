from dataclasses import dataclass
from adapters.domain_model import DomainModel


@dataclass(frozen=True)
class Product(DomainModel):
    sku: str
