from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from routers.file_router import file_router
from routers.auth_router import auth_router
from helper.config import config

app = FastAPI()
app.include_router(auth_router)
app.include_router(file_router)

register_tortoise(
    app,
    db_url=config['DATABASE_URL'],
    modules={"models":["models.auth"]},
    generate_schemas=True,
    add_exception_handlers=True
)