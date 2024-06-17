from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from utils.api_tests import TmaAPITestCase
from task_app.task.tests.factories import TaskFactory
from task_app.task.presentation.types import TaskResponse, TaskListResponse


class TaskAPITestCase(TmaAPITestCase):
    def setUp(self):
        super(TaskAPITestCase, self).setUp()
        self.set_auth_credentials(self.user)

    def test_list_all_tasks(self):
        # create two tasks
        task_1 = TaskFactory(created_by=self.user)
        task_2 = TaskFactory(created_by=self.user)
        # list all tasks for that user using api call
        response = self.client.get('/tasks/')
        json_response = response.json()
        # assert that response status is 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # assert that two tasks are returned in response
        self.assertEqual(len(json_response["items"]), 2)
        # assert that all atrributes are matching
        self.assertEqual(
            json_response,
            TaskListResponse(
                items=[
                    TaskResponse(
                        id=task_1.id,
                        title=task_1.title,
                        description=task_1.description,
                        status=task_1.status
                    ),
                    TaskResponse(
                        id=task_2.id,
                        title=task_2.title,
                        description=task_2.description,
                        status=task_2.status
                    )
                ]
            ).dict()
        )
