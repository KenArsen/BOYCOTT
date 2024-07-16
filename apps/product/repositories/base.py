import abc

from django.db.models.query import QuerySet

from apps.product.models import Product, Category


class ICategoryRepository(abc.ABC):
    @abc.abstractmethod
    def none(self) -> QuerySet[Category]: ...

    @abc.abstractmethod
    def list(self) -> list[Category]: ...

    @abc.abstractmethod
    def retrieve(self, category_id: int) -> Category: ...

    @abc.abstractmethod
    def create(self, data) -> Category: ...

    @abc.abstractmethod
    def update(self, category: Category, data) -> Category: ...

    @abc.abstractmethod
    def delete(self, category: Category) -> None: ...


class IProductRepository(abc.ABC):
    @abc.abstractmethod
    def none(self) -> QuerySet[Product]: ...

    @abc.abstractmethod
    def count(self) -> int: ...

    @abc.abstractmethod
    def get_alternative(self, category: Category) -> list[Product]: ...

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
