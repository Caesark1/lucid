from pydantic import BaseModel, EmailStr, constr


class UserCreate(BaseModel):
    email: EmailStr
    password: constr(min_length=6, max_length=128)


class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True
