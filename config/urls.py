from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
]

urlpatterns += [
    path("api/v1/", include("apps.api.v1.urls", namespace="api")),
]

swagger_urlpatterns = [
    path(f"api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        f"api/v1/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="v1-schema-swagger-ui",
    ),
    path(
        f"api/v1/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="v1-schema-redoc",
    ),
]

urlpatterns += swagger_urlpatterns

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
