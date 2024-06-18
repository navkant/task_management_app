from rest_framework.views import APIView
from rest_framework import response, status
from rest_framework.permissions import IsAuthenticated
from dependency_injector.wiring import Provide

from task_app.task.domain.use_cases.list_all_tasks_use_case import ListAllTasksUseCase
from task_app.task.domain.use_cases.get_task_by_id_use_case import GetTaskByIdUseCase
from task_app.task.domain.use_cases.create_task_use_case import CreateTaskUseCase
from task_app.task.domain.use_cases.update_task_use_case import UpdateTaskUseCase
from task_app.task.domain.use_cases.delete_task_use_case import DeleteTaskUseCase
from task_app.task.domain.use_cases.list_task_by_status_use_case import ListTasksByStatusUseCase
from task_app.task.domain.domain_models import TaskDomainModel
from task_app.task.presentation.types import TaskListResponse, TaskResponse, TaskCreateRequest, TaskUpdateRequest


class ListAllTasksView(APIView):
    permission_classes = [IsAuthenticated]

    def get(
        self,
        request,
        list_all_tasks: ListAllTasksUseCase = Provide["task_container.list_all_tasks_use_case"]
    ):
        tasks = list_all_tasks.execute(user_id=request.user.id)
        return response.Response(
            TaskListResponse.from_orm(tasks).dict(), status=status.HTTP_200_OK
        )


class GetTaskByIdView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, task_id, get_task_by_id: "GetTaskByIdUseCase" = Provide["task_container.get_task_by_id_use_case"]):
        task = get_task_by_id.execute(task_id=task_id, user_id=request.user.id)
        return response.Response(
            TaskResponse.from_orm(task).dict(), status=status.HTTP_200_OK
        )


class CreateTaskView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, create_task_use_case: CreateTaskUseCase = Provide["task_container.create_task_use_case"]):
        task_create_request = TaskCreateRequest.parse_obj(request.data)

        task_response = create_task_use_case.execute(
            task=TaskDomainModel(
                title=task_create_request.title,
                description=task_create_request.description,
                status=task_create_request.status,
            ),
            user_id=request.user.id
        )

        return response.Response(
            TaskResponse.from_orm(task_response).dict(), status=status.HTTP_200_OK
        )


class UpdateTaskView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, update_task_use_case: UpdateTaskUseCase = Provide["task_container.update_task_use_case"]):
        task_update_request = TaskUpdateRequest.parse_obj(request.data)

        update_task = update_task_use_case.execute(
            task=task_update_request,
            user_id=request.user.id
        )

        return response.Response(
            TaskResponse.from_orm(update_task).dict(), status=status.HTTP_200_OK
        )


class DeleteTaskView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, task_id: int, delete_task_use_case: DeleteTaskUseCase = Provide["task_container.delete_task_use_case"]):
        deleted_task = delete_task_use_case.execute(task_id=task_id, user_id=request.user.id)
        return response.Response(
            TaskResponse.from_orm(deleted_task).dict(), status=status.HTTP_200_OK
        )


class ListTasksByStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(
        self,
        request,
        task_status: str,
        list_tasks_by_status: ListTasksByStatusUseCase = Provide["task_container.list_tasks_by_status_use_case"]
    ):
        tasks = list_tasks_by_status.execute(user_id=request.user.id, status=task_status)
        return response.Response(TaskListResponse.from_orm(tasks).dict(), status=status.HTTP_200_OK)
