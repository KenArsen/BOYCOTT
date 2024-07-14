from rest_framework import serializers

from apps.product.models import Product


class ListProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "uuid",
            "brand",
            "logo",
            "status",
            "description",
        )
        ref_name = "ListProduct"


class RetrieveProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "uuid",
            "brand",
            "logo",
            "status",
            "description",
            "created_at",
            "updated_at",
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
            "status",
            "description",
            "description_en",
            "description_ru",
            "description_kg",
        )
        ref_name = "CreateProduct"


class UpdateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "brand",
            "logo",
            "status",
            "description",
        )
        ref_name = "UpdateProduct"
