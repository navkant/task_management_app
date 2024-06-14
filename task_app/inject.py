from dependency_injector import containers, providers

from task_app.task.inject import TaskContainer


class TaskAppContainer(containers.DeclarativeContainer):
    task_container = providers.Container(TaskContainer)
