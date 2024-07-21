from rest_framework import serializers

from apps.product.models import Product
from apps.product.repositories.product import ProductRepository


class AlternativeProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("uuid", "brand", "logo")
        ref_name = "AlternativeProductList"


class ListProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "uuid",
            "brand",
            "logo",
            "status",
            "category",
            "description",
            "url",
        )
        ref_name = "ListProduct"


class RetrieveProductSerializer(serializers.ModelSerializer):
    alternative_products = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "uuid",
            "brand",
            "logo",
            "status",
            "category",
            "description",
            "url",
            "alternative_products",
        )
        ref_name = "RetrieveProduct"

    def get_alternative_products(self, obj):
        product_repository = ProductRepository()
        alternative_products = product_repository.get_alternative(category=obj.category)

        return AlternativeProductListSerializer(alternative_products, many=True).data


class CreateProductSerializer(serializers.ModelSerializer):
    description_en = serializers.CharField(required=False, allow_blank=True)
    description_ru = serializers.CharField(required=False, allow_blank=True)
    description_kg = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Product
        fields = (
            "brand",
            "logo",
            "status",
            "category",
            "description",
            "description_en",
            "description_ru",
            "description_kg",
            "url",
        )
        ref_name = "CreateProduct"


class UpdateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "brand",
            "logo",
            "status",
            "category",
            "description",
            "url",
        )
        ref_name = "UpdateProduct"


class CountProductSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = ("count",)
