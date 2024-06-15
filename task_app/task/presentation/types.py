from typing import List
from pydantic import BaseModel


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str

    class Config:
        orm_mode = True
        from_attributes = True


class TaskListResponse(BaseModel):
    items: List[TaskResponse]

    class Config:
        orm_mode = True
        from_attributes = True


class TaskCreateRequest(BaseModel):
    title: str
    description: str
    status: str


class TaskUpdateRequest(TaskCreateRequest):
    id: int

