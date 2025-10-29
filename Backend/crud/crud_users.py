from models import User as UserModel
from schemas import UserCreate, UserBase
from uuid import UUID
from sqlalchemy.orm import Session
from security import verify_password, get_password_hash


"""
Session is a class from SQLAlchemy that manages interactions with the database. It handles tasks like querying, adding, updating, and deleting records.

Why is it used?

It provides a workspace for all database operations.
It keeps track of changes to objects and commits them to the database.
It ensures efficient and safe communication with the database.
In FastAPI, you typically use a Session object to perform CRUD operations within your API endpoints or CRUD functions.
""" 

# get all users
def get_all_users(db: Session):
    return db.query(UserModel)

# Create User
def create_user(db: Session, user: UserCreate):
    user_data = user.model_dump()
    user_data["hashed_password"] = get_password_hash(user_data.pop("password"))
    db_user = UserModel(**user_data) # unpack Pydantic dict into SQLAlchemy model (**user.dict() unpacks that dictionary, so each key-value pair becomes an argument for the User constructor: User(name="John", email="john@example.com", ...).)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)  #refresh to get updated data like the generated UUID
    return db_user

#get User by Email
def get_user_by_email(db: Session, email:str):
    return db.query(UserModel).filter(UserModel.email == email).first()



# Get User by ID
def get_user(db: Session, user_id: UUID):
    return db.query(UserModel).filter(UserModel.id == user_id).first()

# Update User 
def update_user(db:Session, user_id: UUID, user_update: UserBase):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if db_user:
        update_data = db_user.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
        return db_user
    

# Delete User by ID
def delete_user(db: Session, user_id: UUID):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user # This is useful if you want to confirm what was deleted or send info about the deleted user back in your API response.


# Authenticate function 
def authenticate_user(db: Session, email: str, password: str):
    db_user = get_user_by_email(db, email)
    if not db_user:
        return None
    if verify_password(password, db_user.hashed_password):
        return db_user
    return None
