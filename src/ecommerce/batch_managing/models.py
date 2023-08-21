from django.db import models

import domain


class OrderLine(models.Model):
    reference = models.CharField(max_length=255, primary_key=True)
    sku = models.CharField(max_length=255)
    qty = models.IntegerField()

    @staticmethod
    def update_from_domain(order_line: domain.OrderLine):
        """Updates a Django model from a domain object."""

        # Here is used a try/except block to avoid problems with
        # additional fields that should not be null.
        try:
            order_line_model = OrderLine.objects.get(reference=order_line.reference)
        except OrderLine.DoesNotExist:
            order_line_model = OrderLine(reference=order_line.reference)

        order_line_model.sku = order_line.sku
        order_line_model.qty = order_line.qty
        order_line_model.save()


class Product(models.Model):
    sku = models.CharField(max_length=255, primary_key=True)


class Batch(models.Model):
    available_qty = models.IntegerField()
    reference = models.CharField(max_length=255, primary_key=True)
    order_line = models.ForeignKey("OrderLine", on_delete=models.CASCADE, null=True)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    @staticmethod
    def update_from_domain(batch: domain.Batch):
        """Updates a Django model from a domain object."""

        # Here is used a try/except block to avoid problems with
        # additional fields that should not be null.
        try:
            batch_model = Batch.objects.get(reference=batch.reference)
        except Batch.DoesNotExist:
            batch_model = Batch(reference=batch.reference)

        batch_model.sku = batch.product.sku
        batch_model.available_qty = batch.available_qty

        product, _ = Product.objects.get_or_create(sku=batch.product.sku)
        batch_model.product = product

        if batch.order_line:
            o = batch.order_line
            order_line, _ = OrderLine.objects.get_or_create(
                reference=o.reference, sku=o.sku, qty=o.qty
            )
            batch_model.order_line = order_line

        batch_model.save()

    def to_domain(self):
        """Converts a Django model to a domain object."""
        return domain.Batch(
            reference=self.reference,
            product=domain.Product(sku=self.product.sku),
            qty=self.available_qty,
            order_line=domain.OrderLine(
                reference=self.order_line.reference,
                sku=self.order_line.sku,
                qty=self.order_line.qty,
            ) if self.order_line else None,
        )
