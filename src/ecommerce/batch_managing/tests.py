from django.test import TestCase

from . import models
from . import services
from .repositories import batch_repository, order_line_repository
from adapters import DjangoUnitOfWork
import domain


class TestBatchRepository(TestCase):
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


class TestBatchUnitOfWork(TestCase):
    def test_uow_can_retrieve_a_batch_and_allocate_to_it(self):
        batch_reference = "batch1"
        product_sku = "HIPSTER-WORKBENCH"

        services.insert_batch(reference=batch_reference, sku=product_sku, qty=100)
        with DjangoUnitOfWork([batch_repository, order_line_repository]):
            """
            Tutto quello che viene ripreso dalla repository viene messo in una lista
            Che viene utilizzata dentro il contesto del DjangoUnitOfWork
            """
            batch = batch_repository.get(reference=batch_reference)
            order_line = domain.OrderLine(reference="o1", sku=product_sku, qty=10)
            batch.allocate(order_line)

        batchref = services.get_allocated_batch_ref(reference="o1", sku=product_sku)
        assert batchref == batch_reference
