from rest_framework import status

from task_app.task.tests.factories import TaskFactory
from utils.api_tests import TmaAPITestCase
import json
from task_app.models import Task


class UpdateTaskAPITestCase(TmaAPITestCase):
    def setUp(self):
        super(UpdateTaskAPITestCase, self).setUp()
        self.set_auth_credentials(self.user)

    def test_update_task(self):
        # create few tasks first
        task_1 = TaskFactory(created_by=self.user)
        task_2 = TaskFactory(created_by=self.user)
        # task that has to be updated
        task_update_payload = {
            "id": task_2.id,
            "title": "this is amazing updated task",
            "description": "this is the updated description",
            "status": "DONE"
        }
        response = self.client.post(
            '/tasks/update/',
            data=json.dumps(task_update_payload),
            content_type="application/json"
        )
        json_response = response.json()
        # assert that response status is 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # assert that all attributes are matching
        self.assertEqual(json_response["title"], task_update_payload["title"])
        self.assertEqual(json_response["description"], task_update_payload["description"])
        self.assertEqual(json_response["status"], task_update_payload["status"])
