from .exceptions import OutOfStockError
from .order_line import OrderLine
from adapters.domain_model import DomainModel
from .product import Product

class Batch(DomainModel):
    def __init__(self, reference:str, product:Product, qty:int):
        if not product:
            raise ValueError("Product cannot be None")

        self.reference = reference
        self.product = product
        self.available_qty = qty

    def allocate(self, order_line: OrderLine):
        if not self.can_allocate(order_line):
            raise OutOfStockError(
                f"Cannot allocate {order_line.qty} units "
                + "for order {order_line.reference}"
            )

        self.available_qty -= order_line.qty

    def can_allocate(self, order_line):
        return (
            self.product.sku == order_line.sku and self.available_qty >= order_line.qty
        )
