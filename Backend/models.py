from sqlalchemy import Column, ARRAY, String, Text, Enum, ForeignKey, DateTime, Date, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import func 
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    #signin fields
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)


    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    avatar_url = Column(String, nullable=True)
    roles = Column(ARRAY(String), nullable=False)

# we gonna create a class named User , it will model a table called users.
#it inherits Base , which is created using declarative_base(). this tells the SQLArchemy that User is a mapped class , it should be traeted as a table in the database
# as_uuid=True → SQLAlchemy will store it as a Python uuid.UUID object when you read it from the database.If as_uuid=False, it would return it as a string instead.

class ProjectMember(Base):
    __tablename__ = "project_members"
    __table_args__ = (UniqueConstraint("project_id", "user_id", name = "unique_project_user"),)

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable = False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable = False)
    role = Column(Enum("manager", "member", name="project_member_role"), default="member")
    joined_at = Column(DateTime(timezone=True), server_default=func.now())


class Project(Base):
    __tablename__ = "projects"

    id = Column(UUID(as_uuid=True), primary_key=True, default= uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(Text, nullable= False)
    status = Column(Enum("active", "completed", "archived", name="project_status"), default="active")
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable= False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(Text, nullable= False)   
    status  = Column (Enum("todo", "in_progress", "review", "done", name ="task_name") , default = "todo")
    priority = Column(Enum("high", "medium", "low", name= "task_priority"), default="medium")

    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=False)
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    assigned_to = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable= True)
    due_date = Column(Date, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class TaskComment(Base):
    __tablename__ = "task_comments"

    id = Column(UUID(as_uuid=True), primary_key= True, default=uuid.uuid4, nullable = False)
    content = Column(Text, nullable=False)
    task_id = Column(UUID(as_uuid=True), ForeignKey("tasks.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())