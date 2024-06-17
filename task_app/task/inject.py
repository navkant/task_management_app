from dependency_injector import containers, providers

from task_app.task.data.task_abstract_repo import TaskAbstractRepo
from task_app.task.data.task_db_repo import TaskDbRepo
from task_app.task.domain.use_cases.list_all_tasks_use_case import ListAllTasksUseCase
from task_app.task.domain.use_cases.get_task_by_id import GetTaskByIdUseCase
from task_app.task.domain.use_cases.create_task_use_case import CreateTaskUseCase
from task_app.task.domain.use_cases.update_task_use_case import UpdateTaskUseCase
from task_app.task.domain.use_cases.delete_task_use_case import DeleteTaskUseCase
from task_app.task.domain.use_cases.list_task_by_status import ListTasksByStatusUseCase


class TaskContainer(containers.DeclarativeContainer):
    task_repo = providers.Dependency(
        instance_of=TaskAbstractRepo,
        default=TaskDbRepo(),
    )
    list_all_tasks_use_case = providers.Factory(ListAllTasksUseCase)
    get_task_by_id_use_case = providers.Factory(GetTaskByIdUseCase)
    create_task_use_case = providers.Factory(CreateTaskUseCase)
    update_task_use_case = providers.Factory(UpdateTaskUseCase)
    delete_task_use_case = providers.Factory(DeleteTaskUseCase)
    list_task_by_status = providers.Factory(ListTasksByStatusUseCase)
