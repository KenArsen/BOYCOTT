from rest_framework import serializers

from apps.product.models import Category


class ListCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "uuid",
            "name",
            "name_en",
            "name_ru",
            "name_kg",
        )
        ref_name = "ListCategory"


class RetrieveCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "uuid",
            "name",
            "name_en",
            "name_ru",
            "name_kg",
        )
        ref_name = "RetrieveCategory"


class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "uuid",
            "name",
            "name_en",
            "name_ru",
            "name_kg",
            )
        ref_name = "CreateCategory"


class UpdateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "uuid",
            "name",
            "name_en",
            "name_ru",
            "name_kg",
        )
        ref_name = "UpdateCategory"
