from fastapi import APIRouter

from backend.api.api_v1.endpoints import login, users, shelves, books

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(shelves.router, prefix="/shelves", tags=["sheves"])
api_router.include_router(books.router, prefix="/books", tags=["books"])
