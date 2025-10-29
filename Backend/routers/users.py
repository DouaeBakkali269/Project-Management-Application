from typing import List
from fastapi import  Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from crud.crud_users import create_user, get_user, update_user, delete_user, get_all_users
from schemas import UserCreate, UserBase, UserRead, Token
from uuid import UUID
from dependencies import get_db, get_current_user, require_roles

router = APIRouter(prefix="/api/v1/users", tags=["users"])

# Create User
@router.post("/", response_model=UserRead)
def api_create_user(user: UserCreate, db: Session = Depends(get_db)):
	db_user = create_user(db, user)
	return db_user

# Get User by ID
@router.get("/{user_id}", response_model=UserRead, dependencies=[Depends(get_current_user)])
def api_get_user(user_id: UUID, db: Session = Depends(get_db)):
	db_user = get_user(db, user_id)
	if not db_user:
		raise HTTPException(status_code=404, detail="User not found")
	return db_user

# Update User
@router.put("/{user_id}", response_model=UserRead, dependencies=[Depends(get_current_user)])
def api_update_user(user_id: UUID, user_update: UserBase, db: Session = Depends(get_db)):
	db_user = update_user(db, user_id, user_update)
	if not db_user:
		raise HTTPException(status_code=404, detail="User not found")
	return db_user

# update my profile - check the user logged-in through token
@router.put("/me", response_model=UserBase)
def update_my_profile(user_update: UserBase, current_user: UserBase = Depends(get_current_user), db: Session = Depends(get_db)):
    updated_user = update_user(db, current_user.id, user_update)
    return updated_user


# Delete User
@router.delete("/{user_id}", response_model=UserBase, dependencies=[Depends(get_current_user), Depends(require_roles(["admin"]))])
def api_delete_user(user_id: UUID, db: Session = Depends(get_db)):
	db_user = delete_user(db, user_id)
	if not db_user:
		raise HTTPException(status_code=404, detail="User not found")
	return db_user


# Only admins could see the list of the users
@router.get("/", response_model=List[UserBase] , dependencies=[Depends(get_current_user), Depends(require_roles(["admin"]))])
def list_users(db: Session = Depends(get_db)):
    return get_all_users(db)
