from django.apps import AppConfig


class TaskAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'task_app'
    inject_container = None

    def ready(self):
        from task_app import task
        from task_app.inject import TaskAppContainer

        self.inject_container = TaskAppContainer()
        self.inject_container.wire(
            packages=[
                task
            ]
        )
