from .product import Product
from .batch import Batch
from .order_line import OrderLine
from .exceptions import OutOfStockError
import pytest


def test_when_x_unit_allocated_then_available_quantity_is_decreased_by_x():
    product = Product(sku="Pencil")
    batch = Batch(reference="batch-001", product=product, qty=20)
    order_line = OrderLine(reference="order-001", sku=product.sku, qty=11)
    batch.allocate(order_line)

    assert batch.available_qty == 9


def test_when_more_unit_allocated_than_available_then_raises_out_of_stock_exception():
    product = Product(sku="Pen")
    batch = Batch(reference="batch-002", product=product, qty=20)
    order_line = OrderLine(reference="order-002", sku=product.sku, qty=21)

    with pytest.raises(OutOfStockError):
        batch.allocate(order_line)


def test_when_product_sku_does_not_match_order_line_sku_than_return_false():
    pencil = Product(sku="Pencil")
    pen = Product(sku="Pen")
    batch = Batch(reference="batch-003", product=pencil, qty=20)
    order_line = OrderLine(reference="order-003", sku=pen.sku, qty=11)

    assert batch.can_allocate(order_line) is False
