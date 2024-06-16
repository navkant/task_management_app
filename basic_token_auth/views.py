import uuid

from django.utils import timezone
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

from basic_token_auth.exceptions import InvalidRefreshToken
from basic_token_auth.models import RefreshToken, Token


class GetAuthToken(APIView):
    serializer_class = AuthTokenSerializer

    def get_serializer_context(self):
        return {"request": self.request, "format": self.format_kwarg, "view": self}

    def get_serializer(self, *args, **kwargs):
        kwargs["context"] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        refresh_token, created = RefreshToken.objects.get_or_create(user=user, auth_token=token)

        return Response({"token": token.key, "refresh_token": refresh_token.key})


class RefreshAuthToken(APIView):
    def post(self, request):
        refresh_token_key = request.META.GET("HTTP_X_REFRESH_TOKEN")

        try:
            refresh_token_qs = RefreshToken.objects.select_related("user").filter(key=refresh_token_key)
        except RefreshToken.DoesNotExist as exc:
            raise InvalidRefreshToken

        refresh_token = refresh_token_qs[0]
        auth_token_qs = Token.objects.filter(user_id=refresh_token.user.id)
        new_auth_token = str(uuid.uuid4())
        new_expiry = timezone.now() + timezone.timedelta(days=1)
        from django.db import transaction

        with transaction.atomic():
            auth_token_qs.update(key=new_auth_token, expiry=new_expiry)
            refresh_token_qs.update(auth_token=new_auth_token)

        return Response(
            {
                "token": new_auth_token,
            }
        )


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
