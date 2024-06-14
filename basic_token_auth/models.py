import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


def get_token_expiry():
    time_delta = timezone.timedelta(days=1)
    return timezone.now() + time_delta


class Token(models.Model):
    key = models.CharField("Key", max_length=40, primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(
        User, null=False, blank=False, related_name="token", on_delete=models.CASCADE
    )
    expiry = models.DateTimeField(null=True, blank=True, default=get_token_expiry)

    def __str__(self):
        return self.key


class RefreshToken(models.Model):
    key = models.CharField("Key", max_length=40, primary_key=True, default=uuid.uuid4)
    auth_token = models.OneToOneField(
        Token, related_name='refresh_token', on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        null=False,
        blank=False,
        related_name='refresh_token',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.key
