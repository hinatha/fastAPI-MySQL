from sqlalchemy.ext.asyncio import AsyncSession

import api.models.task as task_model
import api.schemas.task as task_schema

from typing import List, Tuple, Optional

from sqlalchemy import select
from sqlalchemy.engine import Result


'''
class AsyncSession(eversibleProxy):
    async def execute(
        self, statement, params: Any | None = ..., execution_options=..., bind_arguments: Any | None = ..., **kw
    ): ...

class FromClause(Selectable):
    def outerjoin(self, right: FromClause, onclause: Optional[ClauseElement] = ..., full: bool = ...) -> Join: ...

About annotation (->)
FYI: 
https://techacademy.jp/magazine/46675
'''
async def get_tasks_with_done(db: AsyncSession) -> List[Tuple[int, str, bool]]:
    result: Result = await (
        db.execute(
            select(
                task_model.Task.id,
                task_model.Task.title,
                task_model.Done.id.isnot(None).label("done"),
            ).outerjoin(task_model.Done)
        )
    )
    return result.all()

'''
class AsyncSession(ReversibleProxy):
    def add(self, instance, _warn: bool = ...) -> None: ...
    async def commit(self): ...
    async def refresh(self, instance, attribute_names: Any | None = ..., with_for_update: Any | None = ...): ...

About **kwargs
FYI:
https://note.nkmk.me/python-args-kwargs-usage/
About arguments and parameters
https://qiita.com/raviqqe/items/ee2bcb6bef86502f8cc6
'''
async def create_task(
    db: AsyncSession, task_create: task_schema.TaskCreate
) -> task_model.Task:
    task = task_model.Task(**task_create.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task

'''
def Optional(self, parameters):
    """Optional type.

    Optional[X] is equivalent to Union[X, None].
    """
    arg = _type_check(parameters, f"{self} requires a single type.")
    return Union[arg, type(None)]

About Optional and Union
FYI:
https://docs.python.org/ja/3/library/typing.html#special-forms
'''
async def get_task(db: AsyncSession, task_id: int) -> Optional[task_model.Task]:
    result: Result = await db.execute(
        select(task_model.Task).filter(task_model.Task.id == task_id)
    )
    task: Optional[Tuple[task_model.Task]] = result.first()
    return task[0] if task is not None else None  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す

async def update_task(
    db: AsyncSession, task_create: task_schema.TaskCreate, original: task_model.Task
) -> task_model.Task:
    original.title = task_create.title
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original

'''
class AsyncSession(ReversibleProxy):
    async def delete(self, instance): ...
'''
async def delete_task(db: AsyncSession, original: task_model.Task) -> None:
    await db.delete(original)
    await db.commit()