from models import Task as TaskModel
from models import TaskComment
from models import Project as ProjectModel
from models import User as UserModel
from models import TaskComment
from schemas import TaskCreate, TaskBase, TaskCommentContent, TaskCommentRead
from uuid import UUID
from sqlalchemy.orm import Session



def get_task_by_id(db:Session, task_id: UUID):
    task = db.query(ProjectModel).filter(ProjectModel.id == task_id).first()    
    if not task:
        return None
    return task   

def get_tasks_by_projetId(db:Session, project_id: UUID):
    db_project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not db_project : 
        return None
    return db.query(TaskModel).filter(TaskModel.project_id == project_id)

def create_task(db:Session, task: TaskCreate):
    db_project = db.query(ProjectModel).filter(ProjectModel.id == task.project_id).first()
    db_creator = db.query(UserModel).filter(UserModel.id == task.created_by).first()

    if not db_project or not db_creator:
        return None
    
    task_added = TaskModel(**task.model_dump(exclude_unset=True))
    db.add(task_added)
    db.commit()
    db.refresh(task_added)
    return task_added

def update_task(db:Session, task_id: UUID, task_update: TaskBase):
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not db_task:
        return None
    update_data = task_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task 

def delete_task(db:Session, task_id: UUID):
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not db_task:
        return None
    db.delete(db_task)
    db.commit()
    return db_task


# assign task to user
def assign_task_to_user(db: Session, task_id: UUID, user_id: UUID):
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_task or not db_user:
        return None
    db_task.assigned_to = user_id
    db.commit()
    db.refresh(db_task)
    return db_task


# add comment to a task
def add_comment_to_task(db:Session, user_id: UUID, task_id:UUID, comment:TaskCommentContent):
    db_task = db.query(TaskModel).filter(TaskModel.id == comment.task_id).first()
    db_user = db.query(UserModel).filter(TaskModel.id == comment.user_id).first()
    if not db_task or not db_user:
        return None
    db_comment = TaskComment(
        user_id = user_id,
        task_id = task_id,
        **comment.model_dump())   
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

# get comments by task_id
def get_comment_by_taskId(db:Session, task_id:UUID):
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not db_task:
        return None
    return db.query(TaskComment).filter(TaskModel.task_id == task_id)   

#Update comment
def update_comment(db:Session, comment_id: UUID, content_update: TaskCommentContent):
    db_comment = db.query(TaskComment).filter(TaskComment.id == comment_id).first()
    if not db_comment:
        return None
    update_content_dict = content_update.model_dump()
    for key, value in update_content_dict.items():
        setattr(db_comment, key, value)
    db.commit()
    db.refresh(db_comment)
    return db_comment    