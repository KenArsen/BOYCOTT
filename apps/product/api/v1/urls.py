from django.urls import include, path

from .views.category import (
    CategoryListAPIView,
    CategoryRetrieveAPIView,
    CategoryCreateAPIView,
    CategoryUpdateAPIView,
    CategoryDestroyAPIView,
)

from .views.product import (
    ProductCreateAPIView,
    ProductDestroyAPIView,
    ProductListAPIView,
    ProductRetrieveAPIView,
    ProductUpdateAPIView,
    ProductCountAPIView,
)

app_name = "product"

category_urls = [
    path("", CategoryListAPIView.as_view(), name="category-list"),
    path("create/", CategoryCreateAPIView.as_view(), name="category-create"),
    path("<uuid:pk>/", CategoryRetrieveAPIView.as_view(), name="category-retrieve"),
    path("<uuid:pk>/update/", CategoryUpdateAPIView.as_view(), name="category-update"),
    path("<uuid:pk>/delete/", CategoryDestroyAPIView.as_view(), name="category-destroy"),

]

product_urls = [
    path("", ProductListAPIView.as_view(), name="list-product"),
    path("count/", ProductCountAPIView.as_view(), name="count-product"),
    path("create/", ProductCreateAPIView.as_view(), name="create-product"),
    path("<uuid:pk>/", ProductRetrieveAPIView.as_view(), name="retrieve-product"),
    path("<uuid:pk>/update/", ProductUpdateAPIView.as_view(), name="update-product"),
    path("<uuid:pk>/delete/", ProductDestroyAPIView.as_view(), name="delete-product"),
]

urlpatterns = [
    path("", include(product_urls)),
    path("categories/", include(category_urls)),
]
