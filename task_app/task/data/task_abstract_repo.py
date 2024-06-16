from abc import ABC, abstractmethod
from task_app.task.domain.domain_models import TaskListDomainModel, TaskDomainModel


class TaskAbstractRepo(ABC):
    @abstractmethod
    def list_all_tasks(self, user_id: int) -> TaskListDomainModel:
        pass

    @abstractmethod
    def get_task_by_id(self, task_id: int, user_id: int) -> TaskDomainModel:
        pass

    @abstractmethod
    def create_task(self, task: TaskDomainModel, user_id: int) -> TaskDomainModel:
        pass

    @abstractmethod
    def update_task(self, task: TaskDomainModel, user_id: int) -> TaskDomainModel:
        pass

    @abstractmethod
    def delete_task(self, task_id: int, user_id: int) -> TaskDomainModel:
        pass

    @abstractmethod
    def filter_task_by_status(self, user_id: int, status: str) -> TaskListDomainModel:
        pass
