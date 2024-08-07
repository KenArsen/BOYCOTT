from drf_spectacular.utils import extend_schema
from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from apps.product.repositories.category import CategoryRepository
from apps.product.services.category import (
    CreateCategoryService,
    DeleteCategoryService,
    UpdateCategoryService,
)

from ..serializers.category import (
    CreateCategorySerializer,
    ListCategorySerializer,
    RetrieveCategorySerializer,
    UpdateCategorySerializer,
)


@extend_schema(tags=["Categories"], summary="List Category")
class CategoryListAPIView(ListAPIView):
    queryset = CategoryRepository().none()
    serializer_class = ListCategorySerializer
    filter_backends = (SearchFilter,)
    search_fields = ("name",)

    def get_queryset(self):
        return CategoryRepository().list()


@extend_schema(tags=["Categories"], summary="Retrieve Category")
class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = CategoryRepository().none()
    serializer_class = RetrieveCategorySerializer

    def get_object(self):
        return CategoryRepository().retrieve(self.kwargs["pk"])


@extend_schema(tags=["Categories"], summary="Create Category")
class CategoryCreateAPIView(CreateAPIView):
    queryset = CategoryRepository().none()
    serializer_class = CreateCategorySerializer

    def perform_create(self, serializer):
        service = CreateCategoryService(category_repository=CategoryRepository())
        serializer.instance = service.create_category(data=serializer.validated_data)


@extend_schema(tags=["Categories"], summary="Update Category")
class CategoryUpdateAPIView(UpdateAPIView):
    queryset = CategoryRepository().none()
    serializer_class = UpdateCategorySerializer

    def get_object(self):
        return CategoryRepository().retrieve(self.kwargs["pk"])

    def perform_update(self, serializer):
        service = UpdateCategoryService(category_repository=CategoryRepository())
        serializer.instance = service.update_category(
            category=self.get_object(), data=serializer.validated_data
        )


@extend_schema(tags=["Categories"], summary="Delete Category")
class CategoryDestroyAPIView(DestroyAPIView):
    queryset = CategoryRepository().none()
    serializer_class = RetrieveCategorySerializer

    def get_object(self):
        return CategoryRepository().retrieve(self.kwargs["pk"])

    def perform_destroy(self, instance):
        service = DeleteCategoryService(category_repository=CategoryRepository())
        service.delete_category(category=instance)
