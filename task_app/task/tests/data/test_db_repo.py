from django.test import TestCase

from task_app.task.data.task_db_repo import TaskDbRepo
from task_app.task.domain.domain_models import TaskDomainModel, TaskListDomainModel
from task_app.task.tests.factories import TaskFactory, UserFactory
from task_app.models import Task

class BookDbRepoTest(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.db_repo = TaskDbRepo()

    def test_list_all_tasks(self):
        user_1 = UserFactory()
        user_2 = UserFactory()

        task_1 = TaskFactory(created_by=user_1)
        task_2 = TaskFactory(created_by=user_1)
        task_3 = TaskFactory(created_by=user_2)

        tasks = self.db_repo.list_all_tasks(user_id=user_1)
        self.assertEqual(len(tasks.items), 2)
        self.assertEqual(
            tasks,
            TaskListDomainModel(
                items=[
                    TaskDomainModel.from_orm(task_1),
                    TaskDomainModel.from_orm(task_2),
                ]
            ),
        )

    def test_get_task_by_id(self):
        user_1 = UserFactory()

        task_1 = TaskFactory(created_by=user_1)
        task_2 = TaskFactory(created_by=user_1)

        task = self.db_repo.get_task_by_id(task_id=task_1.id, user_id=user_1.id)
        self.assertEqual(
            task,
            TaskDomainModel.from_orm(task_1)
        )

    def test_create_task(self):
        user_1 = UserFactory()

        task_create_domain_model = TaskDomainModel(
            title="this is the title",
            description="description 1",
            status="TO DO",
            )

        new_task = self.db_repo.create_task(
            task=task_create_domain_model, user_id=user_1.id
        )
        tasks = Task.objects.all()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(task_create_domain_model.title, new_task.title)
        self.assertEqual(task_create_domain_model.description, new_task.description)
        self.assertEqual(task_create_domain_model.status, new_task.status)

    def test_update_task(self):
        user_1 = UserFactory()

        task_1 = TaskFactory(created_by=user_1)
        new_description = "some new random description"

        task_update_domain_model = TaskDomainModel(
            id=task_1.id,
            title=task_1.title,
            description= new_description,
            status=task_1.status
        )

        updated_task = self.db_repo.update_task(
            task=task_update_domain_model,
            user_id=user_1.id
        )

        self.assertEqual(updated_task.description, new_description)

    def test_delete_task(self):
        user = UserFactory()

        task = TaskFactory(created_by=user)

        deleted_task = self.db_repo.delete_task(task_id=task.id, user_id=user.id)

        tasks = Task.objects.filter(is_deleted=0)
        self.assertEqual(len(tasks), 0)
