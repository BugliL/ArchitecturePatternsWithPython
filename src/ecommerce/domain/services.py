from .batch import Batch
from .order_line import OrderLine
from adapters import AbstractRepository
from typing import List
from . import exceptions

__all__ = ["allocate", "is_valid_sku"]


def is_valid_sku(sku:str, batches: List[Batch]) -> bool:
    """
    Check if sku is valid
    """
    return sku in {b.product.sku for b in batches}


# Function related to ONLY domain logic and basic types
def _allocate(line: OrderLine, batches: List[Batch]) -> str:
    """
    Allocate order line to a batch
    this is a domain function that has no dependency on the repository
    """
    batch = next(b for b in sorted(batches) if b.can_allocate(line))
    batch.allocate(line)
    return batch.reference


# Function related to an higher level of abstraction
def allocate(line: OrderLine, repo: AbstractRepository) -> str:
    """
    Allocate order line to a batch
    """

    batches = repo.list()
    if not is_valid_sku(line.sku, batches):
        raise exceptions.InvalidSku(f"Invalid sku {line.sku}")

    batchref = _allocate(line, batches)
    return batchref
