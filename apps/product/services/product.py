from ..models import Product
from ..repositories.product import ProductRepository
from .base import (ICreateProductService, IDeleteProductService,
                   IUpdateProductService)


class CreateProductService(ICreateProductService):
    def __init__(self, product_repository: ProductRepository):
        self._product_repository = product_repository

    def create_product(self, data) -> Product:
        return self._product_repository.create(data)


class UpdateProductService(IUpdateProductService):
    def __init__(self, product_repository: ProductRepository):
        self._product_repository = product_repository

    def update_product(self, product: Product, data) -> Product:
        return self._product_repository.update(product, data)


class DeleteProductService(IDeleteProductService):
    def __init__(self, product_repository: ProductRepository):
        self._product_repository = product_repository

    def delete_product(self, product: Product) -> None:
        self._product_repository.delete(product)
