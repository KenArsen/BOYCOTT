from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from apps.user.api.v1.views.login import LoginView, LogoutView
from apps.user.api.v1.views.password import (ChangePasswordAPIView,
                                             ConfirmResetPasswordAPIView,
                                             ResetPasswordAPIView)
from apps.user.api.v1.views.profile import UserProfileAPIView
from apps.user.api.v1.views.registration import RegistrationAPIView

app_name = "user"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", UserProfileAPIView.as_view(), name="user-profile"),
    path("password/", ChangePasswordAPIView.as_view(), name="change-password"),
    path(
        "password/confirm/",
        ConfirmResetPasswordAPIView.as_view(),
        name="confirm-reset-password",
    ),
    path("password/reset/", ResetPasswordAPIView.as_view(), name="reset-password"),
    path("registration/", RegistrationAPIView.as_view(), name="registration"),
]
