from rest_framework.views import APIView
from rest_framework import response, status
from dependency_injector.wiring import Provide

from task_app.task.domain.use_cases.list_all_tasks_use_case import ListAllTasksUseCase
from task_app.task.domain.use_cases.get_task_by_id import GetTaskByIdUseCase
from task_app.task.domain.use_cases.create_task_use_case import CreateTaskUseCase
from task_app.task.domain.use_cases.update_task_use_case import UpdateTaskUseCase
from task_app.task.presentation.types import TaskListResponse, TaskResponse, TaskCreateRequest, TaskUpdateRequest


class ListAllTasksView(APIView):

    def get(
        self,
        request,
        list_all_tasks: ListAllTasksUseCase = Provide["task_container.list_all_tasks_use_case"]
    ):
        tasks = list_all_tasks.execute()
        print(tasks)
        return response.Response(
            TaskListResponse.from_orm(tasks).dict(), status=status.HTTP_200_OK
        )


class GetTaskById(APIView):
    def get(self, request, task_id, get_task_by_id: "GetTaskByIdUseCase" = Provide["task_container.get_task_by_id_use_case"]):
        task = get_task_by_id.execute(id=task_id)
        return response.Response(
            TaskResponse.from_orm(task).dict(), status=status.HTTP_200_OK
        )


class CreateTask(APIView):
    def post(self, request, create_task_use_case: CreateTaskUseCase = Provide["task_container.create_task_use_case"]):
        task_create_request = TaskCreateRequest.parse_obj(request.data)

        task_response = create_task_use_case.execute(task=task_create_request)

        return response.Response(
            TaskResponse.from_orm(task_response).dict(), status=status.HTTP_200_OK
        )


class UpdateTask(APIView):
    def post(self, request, update_task_use_case: UpdateTaskUseCase = Provide["task_container.update_task_use_case"]):
        task_update_request = TaskUpdateRequest.parse_obj(request.data)

        update_task = update_task_use_case.execute(
            task=task_update_request
        )

        return response.Response(
            TaskResponse.from_orm(update_task).dict(), status=status.HTTP_200_OK
        )
