from .abstract_repository import AbstractRepository
from django.db import models


class DjangoRepository(AbstractRepository):
    def __init__(self, model: models.Model):
        self.model_class = model
        self.update_list = []

    def add(self, item):
        self.update(item)

    def update_all(self):
        for item in self.update_list:
            self.update(item)

    def update(self, item):
        self.model_class.update_from_domain(item)

    def get(self, **kwargs):
        result = self.model_class.objects.filter(**kwargs).first().to_domain()
        self.update_list.append(result)
        return result

    def list(self):
        return [item.to_domain() for item in self.model_class.objects.all()]
