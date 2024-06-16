from enum import Enum
from pydantic import BaseModel, field_validator
from typing import List, Optional
from task_app.task.exceptions import InvalidStatus


class StatusChoices(Enum):
    TODO = 'TO DO'
    INPROGRESS = 'IN PROGRESS'
    DONE = 'DONE'

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class TaskDomainModel(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    status: str

    @field_validator('status')
    def name_must_contain_space(cls, v):
        if v not in StatusChoices.list():
            raise InvalidStatus(f'Status must be one of these {StatusChoices.list()}')
        return v

    class Config:
        orm_mode = True
        from_attributes = True


class TaskListDomainModel(BaseModel):
    items: List[TaskDomainModel]

    class Config:
        orm_mode = True
        from_attributes = True
