from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from utils.test_fixtures import user_auth_setup_fixture


class TmaAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test', first_name='test', last_name='test',
                                             email='test@gmail.com')

    def set_auth_credentials(self, user: User):
        self.creds = user_auth_setup_fixture(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.creds["token"]))
