from fastapi import APIRouter, HTTPException
from app.schemas.user import User as userSchema
from app.services.register import registerUser

router = APIRouter()

@router.post("/register")
def register(user: userSchema):
    result = registerUser(user)
    if not result:
        raise HTTPException(status_code=400,detail="user already exists")
    return {"message":"User registerd successfully"}