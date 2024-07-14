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
    class Meta:
        model = Product
        fields = (
            "brand",
            "logo",
            "status",
            "description",
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
