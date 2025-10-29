from fastapi import APIRouter, HTTPException, Depends, status
from schemas import UserCreate, UserRead, Token
from crud.crud_users import get_user_by_email, create_user, authenticate_user
from auth_utils import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from dependencies import get_db

router = APIRouter(prefix="/api/v1/auth")
# sign up endpoint
@router.post("/register", response_model=UserRead)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
	existing = get_user_by_email(db,user.email)
	if existing:
		raise HTTPException(status_code=400, detail="User already registered")
	new_user = create_user(db,user)
	return new_user

# sign in endpoint
@router.post("/signin", response_model = Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)): # Depends() means FastAPI will handle extracting and validating the login form data for you.
	user = authenticate_user(db, form_data.username, form_data.password)
	if not user:
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= "Incorrect Credentials")
	access_token = create_access_token({"sub":str(user.id), "roles":user.roles})
	token = Token(access_token= access_token, token_type= "bearer")
	return token

# Question : WHY use OAuth2 form