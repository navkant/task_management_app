from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Task(models.Model):
    class StatusChoices(models.TextChoices):
        TODO = 'TO DO', _('TO DO')
        INPROGRESS = 'IN PROGRESS', _('IN PROGRESS')
        DONE = 'DONE', _('DONE')

    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=40,
        choices=StatusChoices.choices,
        default=StatusChoices.TODO,
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        blank=False,
        null=False,
        related_name='created_tasks',
        on_delete=models.DO_NOTHING,
    )
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
