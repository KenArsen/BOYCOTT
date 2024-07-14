from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from apps.product.api.filters import ProductFilter
from apps.product.repositories.product import ProductRepository
from apps.product.services.product import (CreateProductService,
                                           DeleteProductService,
                                           UpdateProductService)

from ..serializers.product import (CreateProductSerializer,
                                   ListProductSerializer,
                                   RetrieveProductSerializer,
                                   UpdateProductSerializer)


@extend_schema(tags=["Products"], summary="List product")
class ProductListAPIView(ListAPIView):
    queryset = ProductRepository().none()
    serializer_class = ListProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get_queryset(self):
        return ProductRepository().list()


@extend_schema(tags=["Products"], summary="Retrieve product")
class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = ProductRepository().none()
    serializer_class = RetrieveProductSerializer

    def get_object(self):
        return ProductRepository().retrieve(self.kwargs["pk"])


@extend_schema(tags=["Products"], summary="Create product")
class ProductCreateAPIView(CreateAPIView):
    queryset = ProductRepository().none()
    serializer_class = CreateProductSerializer

    def perform_create(self, serializer):
        service = CreateProductService(product_repository=ProductRepository())
        serializer.instance = service.create_product(data=serializer.validated_data)


@extend_schema(tags=["Products"], summary="Update product")
class ProductUpdateAPIView(UpdateAPIView):
    queryset = ProductRepository().none()
    serializer_class = UpdateProductSerializer

    def get_object(self):
        return ProductRepository().retrieve(self.kwargs["pk"])

    def perform_update(self, serializer):
        service = UpdateProductService(product_repository=ProductRepository())
        serializer.instance = service.update_product(
            product=self.get_object(), data=serializer.validated_data
        )


@extend_schema(tags=["Products"], summary="Delete product")
class ProductDestroyAPIView(DestroyAPIView):
    queryset = ProductRepository().none()
    serializer_class = RetrieveProductSerializer

    def get_object(self):
        return ProductRepository().retrieve(self.kwargs["pk"])

    def perform_destroy(self, instance):
        service = DeleteProductService(product_repository=ProductRepository())
        service.delete_product(product=instance)
