from fastapi import APIRouter, HTTPException, status, Depends
from crud import crud_project
from uuid import UUID
from typing import List
from sqlalchemy.orm import Session
from dependencies import get_db, get_current_user, require_roles
from schemas import ProjectBase, ProjectCreate, ProjectMemberCreate, ProjectMemberRead, ProjectRead, UserBase, UserRead


router = APIRouter(prefix = "/api/v1/projects", tags=["projects"])

@router.post("/", response_model= ProjectRead, dependencies=[Depends(get_current_user), Depends(require_roles("admin", "project_manager"))])
def api_create_project(project: ProjectCreate, db: Session= Depends(get_db)):
    db_project = crud_project.create_project(db, project)
    return db_project

@router.get("/", response_model=List[ProjectRead], dependencies=[Depends(get_current_user), Depends(require_roles("admin"))])
def api_get_all_projects(db: Session= Depends(get_db)):
    db_projects = crud_project.get_all_project(db)
    return db_projects

@router.get("/{project_id}", response_model=ProjectRead, dependencies=[Depends(get_current_user)])
def api_get_project_by_id(project_id: UUID, db: Session = Depends(get_db)):
    db_project = crud_project.get_project_by_id(db, project_id)
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@router.put("/{project_id}", response_model= ProjectRead , dependencies=[Depends(get_current_user), Depends(require_roles("admin", "project_manager"))])
def api_update_project( project_id : UUID , project_update: ProjectBase, db:Session = Depends(get_db)):
    updated_project = crud_project.update_project(db, project_id, project_update)
    if not updated_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated_project


@router.delete("/{project_id}", response_model= ProjectRead, dependencies=[Depends(get_current_user), Depends(require_roles("admin", "project_manager"))])
def api_delete_project(project_id: UUID, db:Session=Depends(get_db)):
    db_project = crud_project.delete_project(db,project_id)
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@router.put("/{project_id}/archive", response_model=ProjectRead , dependencies=[Depends(get_current_user), Depends(require_roles("admin", "project_manager"))])
def api_archive_project(project_id: UUID, db:Session = Depends(get_db)):
    db_project = crud_project.archive_project(db, project_id)
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@router.post("/{project_id}/invite", response_model= ProjectMemberRead, dependencies=[Depends(get_current_user), Depends(require_roles("admin", "project_manager"))])
def api_invite_to_project(project_member_details: ProjectMemberCreate, project_id:UUID, db:Session = Depends(get_db)):
    project_member_new = crud_project.invite_project(db, project_id, project_member_details)
    if not project_member_new:
        raise HTTPException(status_code=404, detail= "user or project not found")
    return project_member_new


@router.get("/users/{user_id}/projects", response_model= List[ProjectRead] , dependencies=[Depends(get_current_user)] )
def api_get_user_projects(user_id: UUID, db : Session = Depends(get_db)):
    projects = crud_project.get_my_projects(db, user_id)

    if not projects:
        raise HTTPException(status_code=404, detail="User does not exist")
    return projects

@router.get("/{project_id}/members", response_model=List[UserRead], dependencies=[Depends(get_current_user)] )
def api_get_project_members(project_id : UUID, db: Session = Depends(get_db)):
    members = crud_project.get_project_members(db, project_id)
    if not members:
        raise HTTPException(status_code=404, detail="project does not exist")
    return members

@router.get("/{project_id}/available-users", response_model=List[UserRead], dependencies=[Depends(get_current_user)])
def api_get_available_users(project_id: UUID, db: Session = Depends(get_db)):
    available_users = crud_project.get_available_users(db, project_id)
    if available_users is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return available_users

@router.delete("/{project_id}/members/{user_id}", response_model=ProjectMemberRead, dependencies=[Depends(get_current_user), Depends(require_roles("admin", "project_manager"))])
def api_remove_project_member(project_id: UUID, user_id: UUID, db: Session = Depends(get_db)):
    removed_member = crud_project.remove_project_member(db, project_id, user_id)
    if not removed_member:
        raise HTTPException(status_code=404, detail="Member not found in project")
    return removed_member

@router.get("/me/projects", response_model=List[ProjectRead], dependencies=[Depends(get_current_user)])
def api_get_my_projects(current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    projects = crud_project.get_my_projects(db, current_user.id)
    if projects is None:
        return []
    return projects