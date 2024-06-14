from rest_framework import status
from rest_framework.exceptions import APIException


class LibException(APIException):
    pass


class InvalidRefreshToken(LibException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "This is invalid refresh token"
    default_code = "LIB_AUTH_00001"


class AuthTokenExpired(LibException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Auth token has expired"
    default_code = "LIB_AUTH_00002"
