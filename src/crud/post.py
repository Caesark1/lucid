from fastapi import HTTPException

from src.models.post import Post


def get_posts(db, user_id: int) -> list[Post]:
    return db.query(Post).filter(Post.user_id == user_id).all()


def create_post(db, title: str, user_id: int) -> Post:
    post = Post(title=title, user_id=user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def remove_post(db, post_id: int, user_id: int) -> None:
    post = db.query(Post).filter(Post.id == post_id, Post.user_id==user_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(post)
    db.commit()
