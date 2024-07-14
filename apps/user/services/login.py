import abc

from rest_framework_simplejwt.tokens import RefreshToken

from apps.user.models import User


class ILoginService(abc.ABC):
    @abc.abstractmethod
    def login(self, request, user): ...


class LoginService(ILoginService):
    def login(self, request, user):
        token = RefreshToken.for_user(user)
        return self._construct_response_data(user, token.access_token, token)

    def _construct_response_data(
        self, user: User, token: str, refresh_token: str
    ) -> dict:
        """
        Constructs the response data dictionary for a successful login.
        """
        return {
            "token": str(token),
            "refresh": str(refresh_token),
            "firs_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        }
