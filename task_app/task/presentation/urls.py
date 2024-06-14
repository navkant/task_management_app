from django.urls import include, path

from task_app.task.presentation import views


urlpatterns = [
    path(r"", views.ListAllTasksView.as_view(), name="list_all_tasks"),
    path(r"<int:task_id>/", views.GetTaskById.as_view(), name="get_task_by_id"),
    path(r"create/", views.CreateTask.as_view(), name="create_task"),
    path(r"update/", views.UpdateTask.as_view(), name="update_task"),
]
