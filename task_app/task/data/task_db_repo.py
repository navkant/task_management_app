from task_app.task.data.task_abstract_repo import TaskAbstractRepo
from task_app.task.domain.domain_models import TaskDomainModel, TaskListDomainModel
from task_app.models import Task


class TaskDbRepo(TaskAbstractRepo):
    def list_all_tasks(self) -> TaskListDomainModel:
        tasks = Task.objects.all()
        return TaskListDomainModel(items=list(map(TaskDomainModel.from_orm, tasks)))

    def get_task_by_id(self, id: int) -> TaskDomainModel:
        task = Task.objects.get(id=id)
        return TaskDomainModel.from_orm(task)

    def create_task(self, task: TaskDomainModel) -> TaskDomainModel:
        new_task = Task.objects.create(
            title=task.title,
            description=task.description,
            status=task.status,
        )

        return TaskDomainModel.from_orm(new_task)

    def update_task(self, task: TaskDomainModel) -> TaskDomainModel:
        Task.objects.filter(id=task.id).update(
            title=task.title,
            description=task.description,
            status=task.status,
        )

        update_task = Task.objects.get(id=task.id)

        return TaskDomainModel.from_orm(update_task)
