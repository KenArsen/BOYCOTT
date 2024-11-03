from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin

from .models import Category, Product
from django import forms


class ProductAdminForm(forms.ModelForm):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    rating = forms.ChoiceField(choices=RATING_CHOICES, label=_("Rating"))

    class Meta:
        model = Product
        fields = "__all__"


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (_("Category"), {"fields": ("name",)}),
        (_("Timestamps"), {"fields": ("created_at", "updated_at")}),
    )

    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    form = ProductAdminForm
    list_display = ("brand", "status", "category", "created_at", "updated_at")
    list_filter = ("status", "category", "created_at", "updated_at")
    search_fields = ("brand", "category__name", "description")
    readonly_fields = ("created_at", "updated_at")
    filter_horizontal = ("alternatives",)

    fieldsets = (
        (
            _("Product"),
            {"fields": ("category", "brand", "logo", "status", "description", "url", 'rating')},
        ),
        (_("Alternatives"), {"fields": ("alternatives",)}),
        (_("Timestamps"), {"fields": ("created_at", "updated_at")}),
    )

    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }
