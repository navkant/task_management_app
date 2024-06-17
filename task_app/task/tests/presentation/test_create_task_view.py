from rest_framework import status
from utils.api_tests import TmaAPITestCase
import json
from task_app.models import Task


class CreateTaskAPITestCase(TmaAPITestCase):
    def setUp(self):
        super(CreateTaskAPITestCase, self).setUp()
        self.set_auth_credentials(self.user)

    def test_create_task(self):
        # task that has to be created
        task_create_payload = {
            "title": "this is amazing task",
            "description": "this is the description",
            "status": "TO DO"
        }
        response = self.client.post(
            '/tasks/create/',
            data=json.dumps(task_create_payload),
            content_type="application/json"
        )
        json_response = response.json()
        # assert that response status is 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # assert that all attributes are matching
        self.assertEqual(json_response["title"], task_create_payload["title"])
        self.assertEqual(json_response["description"], task_create_payload["description"])
        self.assertEqual(json_response["status"], task_create_payload["status"])

        # assert that the primary key is same
        task = Task.objects.all().first()
        self.assertEqual(task.id, json_response["id"])