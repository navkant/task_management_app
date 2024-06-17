from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework import HTTP_HEADER_ENCODING, exceptions
from rest_framework.authentication import BaseAuthentication

from basic_token_auth.exceptions import  AuthTokenExpired


class BearerTokenAuthentication(BaseAuthentication):
    keyword = "Bearer"
    model = None

    def get_model(self):
        if self.model is not None:
            return self.model

        from basic_token_auth.models import Token
        return Token

    def authenticate_credentials(self, key, request):
        model = self.get_model()
        try:
            token = model.objects.select_related("user").get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_("Invalid token"))

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(_("User inactive or deleted"))

        if token.expiry < timezone.now():
            raise AuthTokenExpired

        return token.user, token

    def _get_authorization_header(self, request):
        """
        Return request's 'Authorization:' header, as a bytestring.
        Hide some test client ickyness where the header can be unicode.
        """
        auth = request.META.get("HTTP_AUTHORIZATION", b"")
        if isinstance(auth, str):
            auth = auth.encode(HTTP_HEADER_ENCODING)

        return auth

    def authenticate(self, request):
        auth = self._get_authorization_header(request).split()
        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = _("Invalid token header. No Credentials Provided.")
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _("Invalid token header, Token string should not contain spaces.")

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _(
                "Invalid token header. Token string should not contain invalid characters."
            )
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token, request)