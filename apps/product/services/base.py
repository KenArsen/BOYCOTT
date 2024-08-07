import abc

from apps.product.models import Category, Product


# Category
class ICreateCategoryService(abc.ABC):
    @abc.abstractmethod
    def create_category(self, data) -> Category: ...


class IUpdateCategoryService(abc.ABC):
    @abc.abstractmethod
    def update_category(self, category: Category, data) -> Category: ...


class IDeleteCategoryService(abc.ABC):
    @abc.abstractmethod
    def delete_category(self, category: Category) -> None: ...


# Product
class ICreateProductService(abc.ABC):
    @abc.abstractmethod
    def create_product(self, data) -> Product: ...


class IUpdateProductService(abc.ABC):
    @abc.abstractmethod
    def update_product(self, product: Product, data) -> Product: ...


class IDeleteProductService(abc.ABC):
    @abc.abstractmethod
    def delete_product(self, product: Product) -> None: ...
