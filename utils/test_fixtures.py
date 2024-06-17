from django.contrib.auth.models import User
from basic_token_auth.models import Token, RefreshToken


def user_auth_setup_fixture(user: User):
    user.set_password('Test1234')
    token, created = Token.objects.get_or_create(user=user)
    refresh_token, created = RefreshToken.objects.get_or_create(user=user, auth_token=token)

    return {"token": token.key, "refresh_token": refresh_token.key}
