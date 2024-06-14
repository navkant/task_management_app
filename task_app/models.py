from django.db import models
from django.utils.translation import gettext_lazy as _


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

    def __str__(self):
        return self.title
