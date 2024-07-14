from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from apps.user.api.permissions import IsNotAuthenticated
from apps.user.api.v1.serializers.login import LoginSerializer, LogoutSerializer
from apps.user.services.login import LoginService


class LoginView(GenericAPIView):
    permission_classes = [IsNotAuthenticated]
    serializer_class = LoginSerializer

    @extend_schema(
        summary="Login",
        tags=["Accounts"],
        responses={status.HTTP_204_NO_CONTENT: OpenApiResponse()},
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")
        response_data = LoginService().login(request, user)
        return Response(response_data, status=status.HTTP_200_OK)


class LogoutView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LogoutSerializer

    @extend_schema(
        summary="Log out",
        tags=["Accounts"],
        responses={status.HTTP_204_NO_CONTENT: OpenApiResponse()},
    )
    def post(self, request):
        try:
            # Получаем токен обновления из заголовков запроса
            refresh_token = request.data.get("refresh_token")
            if refresh_token:
                token = RefreshToken(refresh_token)
                # Добавляем токен в черный список
                token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
