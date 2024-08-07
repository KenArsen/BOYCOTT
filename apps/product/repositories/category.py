from django.db.models.query import QuerySet
from rest_framework.exceptions import NotFound

from ..models import Category
from .base import ICategoryRepository


class CategoryRepository(ICategoryRepository):
    def none(self) -> QuerySet[Category]:
        return Category.objects.none()

    def list(self) -> list[Category]:
        return (
            Category.objects.all().prefetch_related("products").order_by("-created_at")
        )

    def retrieve(self, category_id: int) -> Category:
        try:
            return Category.objects.prefetch_related("products").get(pk=category_id)
        except Category.DoesNotExist:
            raise NotFound("Category not found")

    def create(self, data) -> Category:
        return Category.objects.create(**data)

    def update(self, category: Category, data) -> Category:
        for key, value in data.items():
            setattr(Category, key, value)
        category.save()
        return category

    def delete(self, category: Category) -> None:
        category.delete()
