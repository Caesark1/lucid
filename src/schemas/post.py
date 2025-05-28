from pydantic import BaseModel, constr


class PostCreate(BaseModel):
    title: constr(max_length=1_000_000)


class PostOut(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes = True


class PostDelete(BaseModel):
    message: str
