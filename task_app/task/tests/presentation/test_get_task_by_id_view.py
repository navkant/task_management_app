from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from utils.api_tests import TmaAPITestCase
from task_app.task.tests.factories import TaskFactory
from task_app.task.presentation.types import TaskResponse, TaskListResponse


class GetTaskByIdAPITestCase(TmaAPITestCase):
    def setUp(self):
        super(GetTaskByIdAPITestCase, self).setUp()
        self.set_auth_credentials(self.user)

    def test_get_task_by_id(self):
        # create two tasks
        task_1 = TaskFactory(created_by=self.user)
        task_2 = TaskFactory(created_by=self.user)
        # list all tasks for that user using api call
        response = self.client.get(f'/tasks/{task_1.id}/', content_type="application/json")
        json_response = response.json()
        # assert that response status is 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # assert that all task attributes are matching
        self.assertEqual(json_response["title"], task_1.title)
        self.assertEqual(json_response["description"], task_1.description)
        self.assertEqual(json_response["status"], task_1.status)
