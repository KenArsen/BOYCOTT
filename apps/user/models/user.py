from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy

from apps.common import models as core_models
from apps.common.models import CoreModel


class UserManager(core_models.CoreManager, BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must give an email address")

        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(PermissionsMixin, CoreModel, AbstractBaseUser):
    email = models.EmailField(
        verbose_name=gettext_lazy("email address"),
        unique=True,
    )
    first_name = models.CharField(
        verbose_name=gettext_lazy("first name"),
        max_length=150,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name=gettext_lazy("last name"),
        max_length=150,
        blank=True,
    )
    is_staff = models.BooleanField(
        gettext_lazy("staff status"),
        default=False,
        help_text=gettext_lazy(
            "Designates whether the user can log into this admin site."
        ),
    )
    is_active = models.BooleanField(
        gettext_lazy("active"),
        default=True,
        help_text=gettext_lazy(
            "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(
        gettext_lazy("date joined"),
        default=timezone.now,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ("first_name", "last_name")
        verbose_name = gettext_lazy("User")
        verbose_name_plural = gettext_lazy("Users")

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name} <{self.email}>"
        return None
