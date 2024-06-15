from dependency_injector.wiring import Provide
from task_app.task.data.task_abstract_repo import TaskAbstractRepo
from task_app.task.domain.domain_models import TaskDomainModel
from task_app.task.presentation.types import TaskUpdateRequest


class DeleteTaskUseCase:
    def __init__(self, task_repo: TaskAbstractRepo = Provide["task_container.task_repo"]):
        self.task_repo = task_repo

    def execute(self, task_id: int, user_id: int) -> TaskDomainModel:
        return self.task_repo.delete_task(task_id=task_id, user_id=user_id)
