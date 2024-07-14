import django_filters

from apps.product.models import Product


class ProductFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(lookup_expr="icontains")
    status = django_filters.BooleanFilter()

    class Meta:
        model = Product
        fields = ["brand", "status"]
