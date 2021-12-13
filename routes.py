from fastapi import APIRouter
from microblog import blog


my_routes = APIRouter()

my_routes.include_router(router=blog.router, prefix="/blog")
