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

    def test_list_tasks_by_status(self):
        # create 3 tasks
        task_1 = TaskFactory(created_by=self.user, status="DONE")
        task_2 = TaskFactory(created_by=self.user, status="TO DO")
        task_3 = TaskFactory(created_by=self.user, status="IN PROGRESS")

        # list all tasks with status as DONE
        response = self.client.get('/tasks/DONE/')
        json_response = response.json()
        # assert that response status is 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # assert that only one tasks is returned in response
        self.assertEqual(len(json_response["items"]), 1)
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
                    )
                ]
            ).dict()
        )
