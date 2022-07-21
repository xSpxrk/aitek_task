import os

from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

repository_type = os.getenv('REP_TYPE')


if repository_type == 'db':
    from .endpoints import user_db
    app.include_router(user_db.router, prefix='/users', tags=['users'])
elif repository_type == 'local':
    from .endpoints import user_local
    app.include_router(user_local.router, prefix='/users', tags=['users'])
