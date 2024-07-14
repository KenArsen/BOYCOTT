import abc

from django.db.models.query import QuerySet

from apps.product.models import Product


class IProductRepository(abc.ABC):
    @abc.abstractmethod
    def none(self) -> QuerySet[Product]: ...

    @abc.abstractmethod
    def list(self) -> list[Product]: ...

    @abc.abstractmethod
    def retrieve(self, product_id: int) -> Product: ...

    @abc.abstractmethod
    def create(self, data) -> Product: ...

    @abc.abstractmethod
    def update(self, product: Product, data) -> Product: ...

    @abc.abstractmethod
    def delete(self, product: Product) -> None: ...
