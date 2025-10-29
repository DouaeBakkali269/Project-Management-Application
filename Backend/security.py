from passlib.context import CryptContext #secure password hashing

#bcrypt is resistant to brute force; passlib handles salts and secure hashing for us.

pwd_context = CryptContext(schemes=["bcrypt"])

# hash password function (When a user registers)
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# check if password is correct function (When a user logs in)
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)