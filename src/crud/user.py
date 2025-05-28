from pydantic import EmailStr

from src.models.user import User


def get_user_by_email(db, email: EmailStr):
    return db.query(User).filter(User.email == email).first()


def create_user(db, email: EmailStr, hashed_password: str):
    user = User(email=email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
