from typing import cast
from unittest import mock

from dependency_injector.wiring import Provide
from django.apps import apps
from django.test import SimpleTestCase

from task_app.apps import TaskAppConfig
from task_app.task.data.task_abstract_repo import TaskAbstractRepo
from task_app.task.domain.use_cases.delete_task_use_case import DeleteTaskUseCase
from task_app.task.tests.factories import TaskListDomainModeFactory, TaskDomainModelFactory
from task_app.task.presentation.types import TaskCreateRequest


tasks_app = cast(TaskAppConfig, apps.get_app_config("task_app"))


class DeleteTaskUseCaseTest(SimpleTestCase):
    def setUp(self) -> None:
        super(DeleteTaskUseCaseTest, self).setUp()
        self.mocked_task_repo = mock.Mock(TaskAbstractRepo)
        tasks_app.inject_container.task_container.task_repo.override(
            self.mocked_task_repo
        )

    def test_execute(
        self,
        delete_task_use_case: DeleteTaskUseCase = Provide[
            "task_container.delete_task_use_case"
        ],
    ):
        task = TaskDomainModelFactory()
        user_id = 11
        self.mocked_task_repo.delete_task.return_value = task
        result = delete_task_use_case.execute(
            task_id=task.id, user_id=user_id
        )
        self.mocked_task_repo.delete_task.assert_called_with(
            task_id=task.id,
            user_id=user_id
        )
        self.assertEqual(result, task)
