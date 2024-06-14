from abc import ABC, abstractmethod
from task_app.task.domain.domain_models import TaskListDomainModel, TaskDomainModel


class TaskAbstractRepo(ABC):
    @abstractmethod
    def list_all_tasks(self) -> TaskListDomainModel:
        pass

    @abstractmethod
    def get_task_by_id(self, id: int) -> TaskDomainModel:
        pass

    @abstractmethod
    def create_task(self, task: TaskDomainModel) -> TaskDomainModel:
        pass

    @abstractmethod
    def update_task(self, task: TaskDomainModel) -> TaskDomainModel:
        pass
