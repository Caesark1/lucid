from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from src.core.security import get_current_user
from src.models.user import User
from src.database import get_db
from src.schemas.post import PostCreate, PostOut, PostDelete
from src.crud.post import get_posts, create_post, remove_post


router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("/my", response_model=list[PostOut])
def get_post(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    posts = get_posts(db, current_user.id)
    return posts


@router.post("/add", response_model=PostOut)
def add_post(post_data: PostCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    post = create_post(db, post_data.title, current_user.id)
    return post


@router.delete("/delete", response_model=PostDelete)
def delete_post(
        post_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    remove_post(db, post_id, current_user.id)
    return PostDelete(message="Post deleted")
