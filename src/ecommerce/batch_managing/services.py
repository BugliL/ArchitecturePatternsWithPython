from . import models


def insert_batch(reference: str, sku: str, qty: int) -> None:
    product, _ = models.Product.objects.get_or_create(sku=sku)
    models.Batch.objects.create(reference=reference, product=product, available_qty=qty)


def get_allocated_batch_ref(reference: str, sku: str) -> str:
    return models.Batch.objects.get(
        order_line__reference=reference, order_line__sku=sku
    ).reference
