from django.urls import include, path

from task_app.task.presentation import urls as task_urls

urlpatterns = [
    path(r"", include(task_urls)),
]
