from fastapi import FastAPI, APIRouter

from src.routers import auth, post

app = FastAPI()

api_v1_router = APIRouter(prefix="/api/v1")



api_v1_router.include_router(auth.router)
api_v1_router.include_router(post.router)


app.include_router(api_v1_router)
