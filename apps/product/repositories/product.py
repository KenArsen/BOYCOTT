from django.db.models.query import QuerySet
from rest_framework.exceptions import NotFound

from ..models import Product
from .base import IProductRepository


class ProductRepository(IProductRepository):
    def none(self) -> QuerySet[Product]:
        return Product.objects.none()

    def list(self) -> list[Product]:
        return Product.objects.all()

    def retrieve(self, product_id: int) -> Product:
        try:
            return Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise NotFound("Product not found")

    def create(self, data) -> Product:
        return Product.objects.create(**data)

    def update(self, product: Product, data) -> Product:
        for key, value in data.items():
            setattr(product, key, value)
        product.save()
        return product

    def delete(self, product: Product) -> None:
        product.delete()
