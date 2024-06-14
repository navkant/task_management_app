from dependency_injector.wiring import Provide
from task_app.task.data.task_abstract_repo import TaskAbstractRepo
from task_app.task.domain.domain_models import TaskDomainModel


class GetTaskByIdUseCase:
    def __init__(self, task_repo: TaskAbstractRepo = Provide["task_container.task_repo"]):
        self.task_repo = task_repo

    def execute(self, id: int) -> TaskDomainModel:
        return self.task_repo.get_task_by_id(id=id)
