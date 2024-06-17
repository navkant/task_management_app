from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from utils.api_tests import TmaAPITestCase
from task_app.task.tests.factories import TaskFactory
from task_app.task.presentation.types import TaskResponse, TaskListResponse
from task_app.models import Task


class DeleteTaskAPITestCase(TmaAPITestCase):
    def setUp(self):
        super(DeleteTaskAPITestCase, self).setUp()
        self.set_auth_credentials(self.user)

    def test_get_task_by_id(self):
        # create two tasks
        task_1 = TaskFactory(created_by=self.user)
        task_2 = TaskFactory(created_by=self.user)
        # list all tasks for that user using api call
        response = self.client.delete(f'/tasks/{task_1.id}/delete/', content_type="application/json")
        json_response = response.json()
        # assert that response status is 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # assert that the entry is deleted from db
        task = Task.objects.filter(id=task_1.id, is_deleted=0)
        self.assertEqual(len(task), 0)