from rest_framework import status
from rest_framework.exceptions import APIException


class TMAException(APIException):
    pass


class InvalidRefreshToken(TMAException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "This is invalid refresh token"
    default_code = "TMA_AUTH_00001"


class AuthTokenExpired(TMAException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Auth token has expired"
    default_code = "TMA_AUTH_00002"
