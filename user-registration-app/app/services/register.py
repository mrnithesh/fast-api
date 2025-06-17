from app.utils.security import hashPassword
from app.schemas.user import User as UserSchema

users = []

def registerUser(user:UserSchema)-> bool:
    if any(user.email == u["email"] for u in users):
        return False
    hashedPW = hashPassword(user.password)
    users.append({"email":user.email,"password":hashedPW})
    return True
