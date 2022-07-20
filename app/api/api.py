from fastapi import FastAPI
from app.core.config import repository_type
from .endpoints import user_db, user_local

app = FastAPI()


if repository_type == 'db':
    app.include_router(user_db.router, prefix='/users', tags=['users'])
elif repository_type == 'local':
    app.include_router(user_local.router, prefix='/users', tags=['users'])
