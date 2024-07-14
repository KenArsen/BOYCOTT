import abc

from apps.product.models import Product


class ICreateProductService(abc.ABC):
    @abc.abstractmethod
    def create_product(self, data) -> Product: ...


class IUpdateProductService(abc.ABC):
    @abc.abstractmethod
    def update_product(self, product: Product, data) -> Product: ...


class IDeleteProductService(abc.ABC):
    @abc.abstractmethod
    def delete_product(self, product: Product) -> None: ...
