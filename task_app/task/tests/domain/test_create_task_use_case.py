from typing import cast
from unittest import mock

from dependency_injector.wiring import Provide
from django.apps import apps
from django.test import SimpleTestCase

from task_app.apps import TaskAppConfig
from task_app.task.data.task_abstract_repo import TaskAbstractRepo
from task_app.task.domain.use_cases.create_task_use_case import CreateTaskUseCase
from task_app.task.tests.factories import TaskListDomainModeFactory, TaskDomainModelFactory
from task_app.task.presentation.types import TaskCreateRequest


tasks_app = cast(TaskAppConfig, apps.get_app_config("task_app"))


class CreateTaskUseCaseTest(SimpleTestCase):
    def setUp(self) -> None:
        super(CreateTaskUseCaseTest, self).setUp()
        self.mocked_task_repo = mock.Mock(TaskAbstractRepo)
        tasks_app.inject_container.task_container.task_repo.override(
            self.mocked_task_repo
        )

    def test_execute(
        self,
        create_task_use_case: CreateTaskUseCase = Provide[
            "task_container.create_task_use_case"
        ],
    ):
        task = TaskDomainModelFactory()
        user_id = 11
        self.mocked_task_repo.create_task.return_value = task
        result = create_task_use_case.execute(
            task=TaskCreateRequest(
                title=task.title,
                description=task.description,
                status=task.status,
            ),
            user_id=user_id,
        )
        self.mocked_task_repo.create_task.assert_called_with(
            task=task,
            user_id=user_id
        )
        self.assertEqual(result, task)
