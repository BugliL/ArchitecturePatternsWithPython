from .exceptions import OutOfStockError


class Batch:
    def __init__(self, reference, product, qty):
        self.reference = reference
        self.product = product
        self.available_qty = qty

    def allocate(self, order_line):
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
