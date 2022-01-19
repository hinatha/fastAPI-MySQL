from typing import Optional

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")


class TaskCreate(TaskBase):
    pass

'''
orm_mode = True
TaskCreateResponse implicitly receive an ORM and convert it to a Response schema.
FYI:
https://zenn.dev/sh0nk/books/537bb028709ab9/viewer/b92ab0
'''
class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True


class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ")

    class Config:
        orm_mode = True
