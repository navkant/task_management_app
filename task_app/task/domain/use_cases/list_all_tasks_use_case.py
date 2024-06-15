from dependency_injector.wiring import Provide
from task_app.task.data.task_abstract_repo import TaskAbstractRepo
from task_app.task.domain.domain_models import TaskListDomainModel


class ListAllTasksUseCase:
    def __init__(self, task_repo: TaskAbstractRepo = Provide["task_container.task_repo"]):
        self.task_repo = task_repo

    def execute(self, user_id: int) -> TaskListDomainModel:
        return self.task_repo.list_all_tasks(user_id=user_id)
    