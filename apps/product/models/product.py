from django.db import models
from django.utils.translation import gettext_lazy as gettext_lazy

from apps.common.models import CoreModel


class Category(CoreModel):
    name = models.CharField(
        max_length=255,
        verbose_name=gettext_lazy('name'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = gettext_lazy('Category')
        verbose_name_plural = gettext_lazy('Categories')


class Product(CoreModel):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name=gettext_lazy('category'),
        related_name='products',
    )
    brand = models.CharField(
        verbose_name=gettext_lazy("brand"),
        max_length=255,
    )
    logo = models.ImageField(
        verbose_name=gettext_lazy("logo"),
        upload_to="logos/",
        blank=True,
        null=True,
    )
    status = models.BooleanField(
        verbose_name=gettext_lazy("status"),
        default=False,
        help_text=gettext_lazy(
            "Designates whether this product is in boycott (True) or normal (False)."
        ),
    )
    description = models.TextField(
        verbose_name=gettext_lazy("description"),
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = gettext_lazy("Product")
        verbose_name_plural = gettext_lazy("Products")
