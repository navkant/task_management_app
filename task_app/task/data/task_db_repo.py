from task_app.task.data.task_abstract_repo import TaskAbstractRepo
from task_app.task.domain.domain_models import TaskDomainModel, TaskListDomainModel
from task_app.models import Task
from task_app.task.exceptions import TaskDoesNotExists


class TaskDbRepo(TaskAbstractRepo):
    def list_all_tasks(self, user_id: int) -> TaskListDomainModel:
        tasks = Task.objects.filter(created_by=user_id, is_deleted=False)
        return TaskListDomainModel(items=list(map(TaskDomainModel.from_orm, tasks)))

    def get_task_by_id(self, task_id: int, user_id: int) -> TaskDomainModel:
        try:
            task = Task.objects.get(id=task_id, created_by=user_id, is_deleted=False)
        except Task.DoesNotExist as exc:
            raise TaskDoesNotExists(f"No Task found with id: {task_id} user_id: {user_id}")

        return TaskDomainModel.from_orm(task)

    def create_task(self, task: TaskDomainModel, user_id: int) -> TaskDomainModel:
        new_task = Task.objects.create(
            title=task.title,
            description=task.description,
            status=task.status,
            created_by_id=user_id,
        )

        return TaskDomainModel.from_orm(new_task)

    def update_task(self, task: TaskDomainModel, user_id: int) -> TaskDomainModel:
        Task.objects.filter(id=task.id, created_by=user_id).update(
            title=task.title,
            description=task.description,
            status=task.status,
        )

        update_task = Task.objects.get(id=task.id)

        return TaskDomainModel.from_orm(update_task)

    def delete_task(self, task_id: int, user_id: int) -> TaskDomainModel:
        Task.objects.filter(id=task_id, created_by=user_id).update(is_deleted=True)
        try:
            deleted_task = Task.objects.get(id=task_id, created_by=user_id)
        except Task.DoesNotExist as exc:
            raise TaskDoesNotExists(f"No Task found with id: {task_id} user_id: {user_id}")

        return TaskDomainModel.from_orm(deleted_task)
