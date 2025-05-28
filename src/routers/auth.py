from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from src.schemas.user import UserCreate
from src.schemas.token import TokenSchema
from src.database import get_db
from src.crud import user as crud_user
from src.core.security import hash_password, verify_password, create_access_token


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", response_model=TokenSchema)
def signup(user_data: UserCreate, db: Session = Depends(get_db)):
    existing = crud_user.get_user_by_email(db, user_data.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = crud_user.create_user(db, user_data.email, hash_password(user_data.password))

    access_token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token}


@router.post("/login", response_model=TokenSchema)
def login(user_data: UserCreate, db: Session = Depends(get_db)):
    user = crud_user.get_user_by_email(db, user_data.email)
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token}
