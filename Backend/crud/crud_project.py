from sqlalchemy.orm import Session
from schemas import ProjectBase, ProjectCreate, ProjectMemberCreate, ProjectMemberRead
from models import Project as ProjectModel 
from models import ProjectMember, User
from uuid import UUID


def get_all_project(db: Session):
    return db.query(ProjectModel)

def get_project_by_id(db:Session, project_id : UUID):
    return db.query(ProjectModel).filter(ProjectModel.id == project_id)    


def create_project(db: Session, project: ProjectCreate):
    db_project = ProjectModel(**project.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def update_project(db:Session, project_id: UUID, project_update: ProjectBase):
    db_project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not db_project:
        return None
    update_data = project_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_project, key, value)
    db.commit()
    db.refresh(db_project)
    return db_project

def delete_project(db:Session, project_id: UUID):
    db_project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not db_project:
        return None
    db.delete(db_project)
    db.commit()
    return db_project

# archive function
def archive_project(db: Session, project_id: UUID):
    db_project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not db_project:
        return None
    db_project.status = "archived"
    db.commit()
    db.refresh(db_project)
    return db_project

# a member joins a project
def  invite_project(db:Session, project_id: UUID, project_member_details: ProjectMemberCreate):
    db_project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    db_user = db.query(User).filter(User.id == project_member_details.user_id).first()
    if not db_project or not db_user:
        return None
    project_member_new = ProjectMember(**project_member_details.model_dump())
    db.add(project_member_new)
    db.commit()
    db.refresh(project_member_new)
    return project_member_new

# get project members of a project:
def get_project_members(db: Session, project_id: UUID):
    db_project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not db_project:
        return None
    memberships = db.query(ProjectMember).filter(ProjectMember.project_id == project_id).all()
    user_ids = [m.user_id for m in memberships]
    users = db.query(User).filter(User.id.in_(user_ids)).all()
    return users


# get joined projects for a user
def get_my_projects(db: Session, user_id: UUID):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    
    # Step 1: Get all project memberships for the user
    memberships = db.query(ProjectMember).filter(ProjectMember.user_id == user_id).all()

    project_ids = [m.project_id for m in memberships]
    # Step 2: Get all projects with those IDs
    projects = db.query(ProjectModel).filter(ProjectModel.id.in_(project_ids)).all()
    return projects