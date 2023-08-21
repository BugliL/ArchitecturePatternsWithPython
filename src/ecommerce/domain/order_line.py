from dataclasses import dataclass
from adapters.domain_model import DomainModel


# Frozen dataclass is immutable
@dataclass(frozen=True)
class OrderLine(DomainModel):
    reference: str
    sku: str
    qty: int
