from database import SessionLocal
from fastapi import Depends , HTTPException, status

# Depends: This is FastAPI's dependency injection system. It allows you to declare dependencies (like database session) that FastAPI will automatically provide when calling an endpoint function.   
# yield db :
#    This is a generator function.
#    FastAPI will use the db session during the request (e.g., inside your endpoint).
#    The yield keyword allows FastAPI to pause here, run the endpoint logic, and then resume to the finally block afterward.

from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from auth_utils import SECRET_KEY, ALGORITHM
import crud, models
from uuid import UUID
from sqlalchemy.orm import Session



def get_db():
    db= SessionLocal()      # setup: create DB session
    try:
        yield db            # give session to caller (endpoint)
    finally:
        db.close()          # teardown: close session after use    

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/signin") 

#f someone wants a token, they should get it from this URL (/auth/token) by sending username & password


# get logged-in user
def get_current_user(token: str= Depends(oauth2_schema), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id  = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = crud.get_user(db,UUID(user_id))
    if user is None:
        raise credentials_exception
    return user

# role-based acces control helper
def require_roles(*required_roles: str):
    def role_checker(current_user = Depends(get_current_user)):
        user_roles = current_user.roles or []
        if not any(r in user_roles for r in required_roles):
            raise HTTPException(status_code=403, detail="Operation not permitted")
        return current_user
    return role_checker