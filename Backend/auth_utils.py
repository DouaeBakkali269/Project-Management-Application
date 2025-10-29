from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import jwt # create and verify JWT tokens: encode/decode
import os  # Allows reading environment variables (secret keys stored outside code).
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env into the environment

SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120
ACCESS_TOKEN_EXPIRES_DAYS = 7

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp" : expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM)
    return encoded_jwt

def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days= ACCESS_TOKEN_EXPIRES_DAYS)
    to_encode.update({"exp":expire, "scope":"refresh_token"})
