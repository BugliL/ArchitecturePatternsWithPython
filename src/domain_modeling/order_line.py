from dataclasses import dataclass


# Frozen dataclass is immutable
@dataclass(frozen=True)
class OrderLine:
    reference: str
    sku: str
    qty: int
