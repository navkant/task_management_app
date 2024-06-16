import factory
from factory import fuzzy

from task_app.task.domain.domain_models import TaskDomainModel, TaskListDomainModel, StatusChoices
from task_app.models import Task
from django.contrib.auth.models import User


class TaskFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("name")
    description = factory.Faker("pystr")
    status = fuzzy.FuzzyChoice(StatusChoices.list())

    class Meta:
        model = Task


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("email")
    username = factory.Faker("user_name")
    password = factory.Faker("password")

    class Meta:
        model = User


class TaskDomainModelFactory(factory.Factory):
    title = factory.Faker("name")
    description = factory.Faker("pystr")
    status = fuzzy.FuzzyChoice(StatusChoices.list())

    class Meta:
        model = TaskDomainModel


class TaskListDomainModeFactory(factory.Factory):
    items = factory.List([factory.SubFactory(TaskDomainModelFactory) for _ in range(3)])

    class Meta:
        model = TaskListDomainModel
