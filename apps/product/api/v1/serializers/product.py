from rest_framework import serializers

from apps.product.models import Product


class AlternativeProductSerializer(serializers.ModelSerializer):
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
            "rating",
            "status",
            "category",
            "description",
            "description_en",
            "description_ru",
            "description_kg",
            "url",
            "url_en",
            "url_ru",
            "url_kg",
        )
        ref_name = "ListProduct"


class RetrieveProductSerializer(serializers.ModelSerializer):
    alternatives = AlternativeProductSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            "uuid",
            "brand",
            "logo",
            "rating",
            "status",
            "category",
            "description",
            "description_en",
            "description_ru",
            "description_kg",
            "url",
            "url_en",
            "url_ru",
            "url_kg",
            "alternatives",
        )
        ref_name = "RetrieveProduct"


class CreateProductSerializer(serializers.ModelSerializer):
    description_en = serializers.CharField(required=False, allow_blank=True)
    description_ru = serializers.CharField(required=False, allow_blank=True)
    description_kg = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Product
        fields = (
            "brand",
            "logo",
            "rating",
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
            "rating",
            "status",
            "category",
            "description",
            "description_en",
            "description_ru",
            "description_kg",
            "url",
            "url_en",
            "url_ru",
            "url_kg",
        )
        ref_name = "UpdateProduct"


class CountProductSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = ("count",)
