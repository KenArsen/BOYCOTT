from django.urls import include, path

app_name = "api"
urlpatterns = [
    path(
        "users/",
        include(
            "apps.user.api.v1.urls",
            namespace="user",
        ),
    ),
    path(
        "products/",
        include(
            "apps.product.api.v1.urls",
            namespace="product",
        ),
    ),
]
