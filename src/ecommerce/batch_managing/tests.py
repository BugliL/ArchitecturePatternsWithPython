from django.test import TestCase

from .repositories import batch_repository
import domain
from . import models


class TestBatch(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product = domain.Product(sku="Pencil")
        cls.batch = domain.Batch(reference="batch-001", product=cls.product, qty=20)

    def test_when_batch_added_to_repository_it_should_be_saved(self):
        repository = batch_repository
        repository.add(self.batch)

        batch = models.Batch.objects.get(reference=self.batch.reference)
        self.assertIsNotNone(batch)
        self.assertEqual(batch.reference, self.batch.reference)
        self.assertEqual(batch.product.sku, self.batch.product.sku)
        self.assertEqual(batch.available_qty, self.batch.available_qty)
