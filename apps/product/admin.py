from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin

from .models import Product


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ("brand", "status", "created_at", "updated_at")
    list_filter = ("status", "created_at", "updated_at")
    search_fields = ("brand", "description")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (_("Product"), {"fields": ("brand", "logo", "status", "description")}),
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
