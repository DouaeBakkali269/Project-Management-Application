from fastapi import APIRouter, HTTPException, Depends
import crud.crud_tasks as crud
from models import Task as TaskModel
from schemas import TaskBase, TaskCreate, TaskRead, TaskCommentContent, TaskCommentRead
from sqlalchemy.orm import Session
from dependencies import get_db, get_current_user, require_roles
from typing import List
from uuid import UUID

router = APIRouter(prefix = "/api/v1/tasks", tags=["tasks"])

@router.post("/", response_model= TaskRead, dependencies=[Depends(get_current_user), Depends(require_roles(["admin", "manager"]))])
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    task = crud.create_task(db, task)
    if not task:
        raise HTTPException(status_code=404, detail="user or project unfound")
    return task 

@router.get("/{project_id}", response_model= List[TaskRead] , dependencies=[Depends(get_current_user)])
def get_tasks_by_project_id(project_id: UUID, db: Session = Depends(get_db)):
    tasks = crud.get_comment_by_taskId(db, project_id)
    if not tasks:
        raise HTTPException(status_code=404, detail="Project does not exist")
    return tasks

@router.get("/{task_id}", response_model=TaskRead , dependencies=[Depends(get_current_user)] )
def get_task_by_id(task_id: UUID, db:Session = Depends(get_db)):
    task = crud.get_task_by_id(db, task_id)    
    if not task:
        raise HTTPException(status_code=404, detail="task does not exist")
    return task

@router.put("/{task_id}", response_model = TaskRead, dependencies=[Depends(get_current_user), Depends(require_roles(["admin", "manager"]))])
def update_task(task_id:  UUID, task_update: TaskBase, db: Session = Depends(get_db)):
    updated_task = crud.update_task(db, task_id, task_update)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task does not exist")
    return updated_task

@router.delete("/{task_id}", response_model = TaskRead, dependencies=[Depends(get_current_user), Depends(require_roles(["admin", "manager"]))])
def delete_task(task_id: UUID, db: Session = Depends(get_db)):
    task_to_delete = crud.delete_task(db, task_id)
    if not task_to_delete:
        raise HTTPException(status_code=404, detail = "Task does not exist")
    return task_to_delete

@router.put("/{task_id}/assign/{user_id}", response_model= TaskRead, dependencies=[Depends(get_current_user), Depends(require_roles(["admin", "manager"]))])
def assign_task_to_user(task_id: UUID, user_id: UUID, db: Session = Depends(get_db)):
    assigned_task = crud.assign_task_to_user(db, task_id, user_id)
    if not assigned_task:
        raise HTTPException(status_code=404, detail="Task or User does not exist.")
    return assigned_task

@router.post("/{task_id}/comments", response_model=TaskCommentRead , dependencies=[Depends(get_current_user)])
def create_task_comment(
    task_id: UUID,
    comment: TaskCommentContent,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    comment_obj = crud.add_comment_to_task(db, task_id, current_user.id, comment)
    if not comment_obj:
        raise HTTPException(status_code=404, detail="task or user does not exist.")
    return comment_obj

@router.get("/{task_id}/comments", response_model= List[TaskCommentRead] , dependencies=[Depends(get_current_user)])
def get_comments_by_task(task_id: UUID, db:Session = Depends(get_db)):
    comments = crud.get_comment_by_taskId(db. task_id)
    if not comments:
        raise HTTPException(status_code=404, detail="task does not exist")
    return comments

@router.put("/comments/{comment_id}", response_model= TaskCommentRead , dependencies=[Depends(get_current_user)])
def update_comment(comment_id: UUID, content_update: TaskCommentContent, db : Session = Depends(get_db)):
    updated_comment = crud.update_comment(db, comment_id, content_update)
    if not updated_comment:
        raise HTTPException(status_code=404, detail="comment does not exist")
    return updated_comment
