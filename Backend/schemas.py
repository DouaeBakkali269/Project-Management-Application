from pydantic import BaseModel, EmailStr
from typing import List, Optional
from uuid import UUID
from datetime import datetime, date
from enum import Enum

# define enum for creating users / registration
class UserRole(str, Enum):
    team_member = "team member"
    project_manager = "project manager"


#base schema for users (good also for update)
class UserBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    gender: Optional[str] = None
    avatar_url : Optional[str] = None
    roles: Optional[List[str]] = None

# Schema for creating users
class UserCreate(UserBase):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    roles: List[UserRole]

# Schema for reading users
class UserRead(UserBase):
    id: UUID
    email: EmailStr

    class Config:
        orm_mode = True #tells Pydantic that it can read data directly from ORM models (SQLAlchemy objects)

# Authentication schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: Optional[str] = None
    roles: Optional[List[str]] = None

#It extends BaseModel so it gets all the features of Pydantic models:
# Automatic data validation (checks types, required fields, etc.)
#Easy conversion to and from dictionaries and JSON
#Helpful error messages if data is wrong or missing

# Project model schemas
class ProjectBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = "active"

class ProjectCreate(ProjectBase):
    name: str
    created_by: UUID

class ProjectRead(ProjectBase):
    id: UUID
    created_by: UUID
    created_at: datetime
    updated_at: Optional[datetime] = None

    class config:
        orm_mode = True

# ProjectTember schema
class ProjectMemberCreate(BaseModel):
    project_id: UUID
    user_id: UUID
    role: str = "member"

class ProjectMemberRead(BaseModel):
    id: UUID
    project_id: UUID
    user_id: UUID
    role: str = "member"
    joined_at: datetime

    class config:
        orm_mode = True        

# Task schemas
class TaskBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = "todo"
    priority: Optional[str] = "medium"
    assigned_to: Optional[UUID] = None
    due_date: Optional[date] = None

class TaskCreate(TaskBase):
    title: str
    project_id: UUID
    created_by: UUID

class TaskRead(BaseModel):
    id: UUID
    project_id: UUID
    created_by: UUID    
    created_at: datetime
    updated_at: Optional[datetime] = None

    class config:
        orm_mode = True   

# Task Coment schema
class TaskCommentContent(BaseModel):
    content: str


class TaskCommentRead(BaseModel):
    id: UUID
    content: str
    task_id: UUID
    user_id: UUID    
    created_at: datetime
    updated_at: Optional[datetime] = None
