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
        # Вы можете также использовать select_related или prefetch_related здесь, если у вас есть связанные объекты.
        return Product.objects.filter(category=category, status=False).select_related("category")

    def list(self) -> list[Product]:
        # Здесь используется select_related для получения связанных категорий и prefetch_related для альтернатив.
        return Product.objects.select_related("category").prefetch_related("alternatives").order_by("-updated_at")

    def retrieve(self, product_id: int) -> Product:
        try:
            # Здесь также добавляется prefetch_related для альтернатив, если они нужны
            return Product.objects.select_related("category").prefetch_related("alternatives").get(pk=product_id)
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
