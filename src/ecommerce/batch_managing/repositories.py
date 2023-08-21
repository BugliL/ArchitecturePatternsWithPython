from adapters import DjangoRepository
from . import models

batch_repository = DjangoRepository(models.Batch)

product_repository = DjangoRepository(models.Product)
