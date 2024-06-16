from rest_framework import status
from rest_framework.exceptions import APIException


class TaskDoesNotExists(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "No Task exists with given id"
    default_code = "TMA_TASK_00001"


class InvalidStatus(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default = "Status Type is Invalid"
    default_detail = "TMA_TASK_00002"
