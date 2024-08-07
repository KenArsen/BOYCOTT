import os
from pathlib import Path

from django.conf.locale import LANG_INFO
from django.utils.translation import gettext_lazy as _
from environs import Env

env = Env()
env_file = os.getenv("ENV_FILE", ".env")
env.read_env(env_file)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env.str("BOYCOTT_SECRET_KEY")

DEBUG = env.bool("BOYCOTT_DEBUG", default=False)

ALLOWED_HOSTS = env.list("BOYCOTT_ALLOWED_HOSTS", default=["*"])

FIRST_PARTY_APPS = [
    "jazzmin",
    "modeltranslation",
]

SECOND_PARTY_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

THIRD_PARTY_APPS = [
    "corsheaders",
    "django_filters",
    "rest_framework",
    "drf_spectacular",
    "drf_spectacular_sidecar",
]

LOCAL_APPS = [
    "apps.user.apps.UserConfig",
    "apps.product.apps.ProductConfig",
]

INSTALLED_APPS = [
    *FIRST_PARTY_APPS,
    *SECOND_PARTY_APPS,
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

AUTH_USER_MODEL = "user.User"
ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("BOYCOTT_DATABASE_NAME"),
        "USER": env.str("BOYCOTT_DATABASE_USER"),
        "PASSWORD": env.str("BOYCOTT_DATABASE_PASSWORD"),
        "HOST": env.str("BOYCOTT_DATABASE_HOST"),
        "PORT": env.int("BOYCOTT_DATABASE_PORT"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication"
    ],
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    # "PAGE_SIZE": 20,
}

SIMPLE_JWT = {
    "USER_ID_FIELD": "uuid",
    "USER_ID_CLAIM": "user_uuid",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Boycott API",
    "DESCRIPTION": "Boycott",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
}

JAZZMIN_SETTINGS = {
    "site_title": "Boycott Admin",
    "site_header": "Boycott",
    "site_brand": "Boycott",
    "site_logo_classes": "img-circle",
    "welcome_sign": "Welcome to the Boycott Admin!",
    "search_model": ["user.User", "product.Product"],
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "user.User"},
        {"model": "product.Product"},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["user", "product"],
    "icons": {
        "user": "fas fa-users-cog",
        "user.User": "fas fa-user",
        "user.Group": "fas fa-users",
        "sites.Site": "fas fa-globe",
        "product.Product": "fas fa-box",
        "product.Category": "fas fa-tags",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": False,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    "language_chooser": True,
}

# Internationalization settings
LANGUAGE_CODE = "ru-ru"
LANGUAGES = [
    ("en", _("English")),
    ("ru", _("Russian")),
    ("kg", _("Kyrgyz")),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = "en"
MODELTRANSLATION_LANGUAGES = ("en", "ru", "kg")

LANG_INFO.update(
    {
        "kg": {
            "bidi": False,
            "code": "kg",
            "name": "Kyrgyz",
            "name_local": "Кыргызча",
        },
    }
)

TIME_ZONE = env.str("BOYCOTT_TIME_ZONE", default="UTC")

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files settings
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media files settings
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Locale paths
LOCALE_PATHS = [BASE_DIR / "locale/"]

# Security settings
USE_X_FORWARDED_HOST = True
APPEND_SLASH = False
SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "BOYCOTT_SECURE_CONTENT_TYPE_NOSNIFF", default=True
)
SECURE_HSTS_SECONDS = env.int("BOYCOTT_SECURE_HSTS_SECONDS", default=31536000)  # 1 year
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_HTTPONLY = env.bool("BOYCOTT_SESSION_COOKIE_HTTPONLY", default=True)
SESSION_COOKIE_SECURE = env.bool("BOYCOTT_SESSION_COOKIE_SECURE", default=True)
SESSION_COOKIE_NAME = "s"
CSRF_COOKIE_SECURE = env.bool("BOYCOTT_CSRF_COOKIE_SECURE", default=True)
CSRF_COOKIE_NAME = "c"
X_FRAME_OPTIONS = env.str("BOYCOTT_X_FRAME_OPTIONS", default="SAMEORIGIN")
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_PRELOAD = True
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = env.list("BOYCOTT_CORS_ALLOWED_ORIGINS", default=[])
CSRF_TRUSTED_ORIGINS = env.list("BOYCOTT_CSRF_TRUSTED_ORIGINS", default=[])

SITE_ID = env.int("BOYCOTT_SITE_ID", default=1)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
