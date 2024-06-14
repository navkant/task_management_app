from dependency_injector.wiring import Provide
from task_app.task.data.task_abstract_repo import TaskAbstractRepo
from task_app.task.domain.domain_models import TaskDomainModel
from task_app.task.presentation.types import TaskCreateRequest


class CreateTaskUseCase:
    def __init__(self, task_repo: TaskAbstractRepo = Provide["task_container.task_repo"]):
        self.task_repo = task_repo

    def execute(self, task: TaskCreateRequest) -> TaskDomainModel:
        return self.task_repo.create_task(
            task=TaskDomainModel(
                title=task.title,
                description=task.description,
                status=task.status,
            )
        )
