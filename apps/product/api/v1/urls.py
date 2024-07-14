from django.urls import include, path

from .views.product import (ProductCreateAPIView, ProductDestroyAPIView,
                            ProductListAPIView, ProductRetrieveAPIView,
                            ProductUpdateAPIView)

app_name = "product"

product_urls = [
    path("", ProductListAPIView.as_view(), name="list-product"),
    path("create/", ProductCreateAPIView.as_view(), name="create-product"),
    path("<uuid:pk>/", ProductRetrieveAPIView.as_view(), name="retrieve-product"),
    path("<uuid:pk>/update/", ProductUpdateAPIView.as_view(), name="update-product"),
    path("<uuid:pk>/delete/", ProductDestroyAPIView.as_view(), name="delete-product"),
]

urlpatterns = [
    path("", include(product_urls)),
]
