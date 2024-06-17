from django.urls import include, path

from task_app.task.presentation import views


urlpatterns = [
    path(r"", views.ListAllTasksView.as_view(), name="list_all_tasks"),
    path(r"<int:task_id>/", views.GetTaskByIdView.as_view(), name="get_task_by_id"),
    path(r"create/", views.CreateTaskView.as_view(), name="create_task"),
    path(r"update/", views.UpdateTaskView.as_view(), name="update_task"),
    path(r"<int:task_id>/delete/", views.DeleteTaskView.as_view(), name="delete_task"),
    path(r"<str:status>/", views.ListTasksByStatusView.as_view(), name="list_task_by_status"),
]
