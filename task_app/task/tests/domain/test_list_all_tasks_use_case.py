from typing import cast
from unittest import mock

from dependency_injector.wiring import Provide
from django.apps import apps
from django.test import SimpleTestCase

from task_app.apps import TaskAppConfig
from task_app.task.data.task_abstract_repo import TaskAbstractRepo
from task_app.task.domain.use_cases.list_all_tasks_use_case import ListAllTasksUseCase
from task_app.task.tests.factories import TaskDomainModel, TaskListDomainModel, TaskListDomainModeFactory


tasks_app = cast(TaskAppConfig, apps.get_app_config("task_app"))


class ListAllTasksUseCaseTest(SimpleTestCase):
    def setUp(self) -> None:
        super(ListAllTasksUseCaseTest, self).setUp()
        self.mocked_task_repo = mock.Mock(TaskAbstractRepo)
        tasks_app.inject_container.task_container.task_repo.override(
            self.mocked_task_repo
        )

    def test_execute(
        self,
        list_all_tasks_use_case: ListAllTasksUseCase = Provide[
            "task_container.list_all_tasks_use_case"
        ],
    ):
        task_list = TaskListDomainModeFactory()
        user_id = 11
        self.mocked_task_repo.list_all_tasks.return_value = task_list
        result = list_all_tasks_use_case.execute(user_id=user_id)
        self.mocked_task_repo.list_all_tasks.assert_called_with(user_id=user_id)
        self.assertEqual(len(result.items), 3)
        self.assertEqual(task_list, result)
