from typing import cast
from unittest import mock

from dependency_injector.wiring import Provide
from django.apps import apps
from django.test import SimpleTestCase

from task_app.apps import TaskAppConfig
from task_app.task.data.task_abstract_repo import TaskAbstractRepo
from task_app.task.domain.use_cases.list_task_by_status_use_case import ListTasksByStatusUseCase
from task_app.task.tests.factories import TaskDomainModel, TaskListDomainModel, TaskListDomainModeFactory


tasks_app = cast(TaskAppConfig, apps.get_app_config("task_app"))


class ListTasksByStatusUseCaseTest(SimpleTestCase):
    def setUp(self) -> None:
        super(ListTasksByStatusUseCaseTest, self).setUp()
        self.mocked_task_repo = mock.Mock(TaskAbstractRepo)
        tasks_app.inject_container.task_container.task_repo.override(
            self.mocked_task_repo
        )

    def test_execute(
        self,
        list_tasks_by_status_use_case: ListTasksByStatusUseCase = Provide[
            "task_container.list_tasks_by_status_use_case"
        ],
    ):
        task_list = TaskListDomainModeFactory()
        user_id = 11
        task_status = "TO DO"
        self.mocked_task_repo.list_tasks_by_status.return_value = task_list
        result = list_tasks_by_status_use_case.execute(user_id=user_id, status=task_status)
        self.mocked_task_repo.list_tasks_by_status.assert_called_with(user_id=user_id, status=task_status)
        self.assertEqual(len(result.items), 3)
        self.assertEqual(task_list, result)
