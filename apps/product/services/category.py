from ..models import Category
from ..repositories.category import CategoryRepository
from .base import ICreateCategoryService, IDeleteCategoryService, IUpdateCategoryService


class CreateCategoryService(ICreateCategoryService):
    def __init__(self, category_repository: CategoryRepository):
        self._category_repository = category_repository

    def create_category(self, data) -> Category:
        category = self._category_repository.create(data)
        Category.description_en = data.get('name_en', '')
        Category.description_ru = data.get('name_ru', '')
        Category.description_kg = data.get('name_kg', '')
        category.save()
        return category


class UpdateCategoryService(IUpdateCategoryService):
    def __init__(self, category_repository: CategoryRepository):
        self._category_repository = category_repository

    def update_category(self, category: Category, data) -> Category:
        return self._category_repository.update(category, data)


class DeleteCategoryService(IDeleteCategoryService):
    def __init__(self, category_repository: CategoryRepository):
        self._category_repository = category_repository

    def delete_category(self, category: Category) -> None:
        self._category_repository.delete(category)
