from django.db.models.query import QuerySet
from rest_framework.exceptions import NotFound

from ..models import Product
from .base import IProductRepository


class ProductRepository(IProductRepository):
    def none(self) -> QuerySet[Product]:
        return Product.objects.none()

    def count(self) -> int:
        return Product.objects.count()

    def get_alternative(self, category) -> list[Product]:
        return Product.objects.filter(category=category, status=False)

    def list(self) -> list[Product]:
        return Product.objects.all().select_related("category").order_by("-created_at")

    def retrieve(self, product_id: int) -> Product:
        try:
            return Product.objects.select_related("category").get(pk=product_id)
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
