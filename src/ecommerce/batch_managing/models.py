from django.db import models

import domain

class Product(models.Model):
    sku = models.CharField(max_length=255, primary_key=True)


class Batch(models.Model):
    reference = models.CharField(max_length=255)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    available_qty = models.IntegerField()

    @staticmethod
    def update_from_domain(batch: domain.Batch):
        """Updates a Django model from a domain object."""
        batch_model, _ = Batch.objects.get_or_create(reference=batch.reference)
        batch_model.sku = batch.product.sku
        batch_model.available_qty = batch.available_qty
        
        product, _ = Product.objects.get_or_create(sku=batch.product.sku)
        batch_model.product = product
        batch_model.save()

    def to_domain(self):
        """Converts a Django model to a domain object."""
        return domain.Batch(
            reference=self.reference,
            product=domain.Product(sku=self.product.sku),
            qty=self.available_qty,
        )
