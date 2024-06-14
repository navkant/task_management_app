from enum import Enum
from pydantic import BaseModel
from typing import List


class TaskDomainModel(BaseModel):
    id: int
    title: str
    description: str
    status: str  # use validator here?

    class Config:
        orm_mode = True
        from_attributes = True


class TaskListDomainModel(BaseModel):
    items: List[TaskDomainModel]

    class Config:
        orm_mode = True
        from_attributes = True


class StatusChoices(Enum):
    TODO = 'TO DO'
    INPROGRESS = 'IN PROGRESS'
    DONE = 'Done'
