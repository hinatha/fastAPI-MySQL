from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException
import api.cruds.task as task_crud
from api.db import get_db
import api.schemas.task as task_schema

router = APIRouter()
'''
Execute APIRouter()
FYI: 
https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-apirouter
'''

'''
About Depends (DI)
FYI:
https://zenn.dev/panyoriokome/scraps/f9ba03a1ebd28f
https://qiita.com/papi_tokei/items/dbcc5f054986de9cbbf6
'''
@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks(db: AsyncSession = Depends(get_db)):
    return await task_crud.get_tasks_with_done(db)

@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(
    task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)
):
    return await task_crud.create_task(db, task_body)

'''
About HTTPException
FYI:
https://fastapi.tiangolo.com/tutorial/handling-errors/
'''

@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_task(
    task_id: int, task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)
):
    task = await task_crud.get_task(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return await task_crud.update_task(db, task_body, original=task)
    
@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    task = await task_crud.get_task(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return await task_crud.delete_task(db, original=task)
