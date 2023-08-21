from .abstract_repository import AbstractRepository


class DjangoRepository(AbstractRepository):
    def __init__(self, model_class):
        self.model_class = model_class

    def add(self, item):
        super().add(item)
        self.update(item)

    def update(self, item):
        self.model_class.update_from_domain(item)

    def get(self, identifier):
        return (
            self.model_class.objects.filter(identifier=identifier).first().to_domain()
        )

    def list(self):
        return [item.to_domain() for item in self.model_class.objects.all()]
