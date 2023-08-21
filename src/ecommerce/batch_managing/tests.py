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
    @classmethod
    def setUpTestData(cls):
        services.insert_batch(reference="batch1", sku="HIPSTER-WORKBENCH", qty=100)

    def test_uow_can_retrieve_a_batch_and_allocate_to_it(self):
        with DjangoUnitOfWork(batch_repository) as uow:
            batch = uow.repository.get(reference="batch1")
            order_line = domain.OrderLine(reference="o1", sku="HIPSTER-WORKBENCH", qty=10)
            batch.allocate(order_line)
            
            # TODO: spostare questo
            # order_line_repository.update(order_line)
            

        for batch in models.Batch.objects.all():
            print(batch.reference, batch.available_qty, batch.order_line)

        batchref = services.get_allocated_batch_ref(
            reference="o1", sku="HIPSTER-WORKBENCH"
        )
        assert batchref == "batch1"
