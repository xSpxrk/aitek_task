from fastapi import APIRouter, HTTPException

from app import schemas
from app.models.user_local import User


router = APIRouter()

users = dict()  # Переменная для хранения данных


@router.get('/{user_id}', response_model=schemas.User)
def read_user(
        user_id: int,
) -> User:
    return users.get(user_id)


@router.post('/', response_model=schemas.User)
def create_user(
        user_in: schemas.UserCreate,
) -> User:
    user = User(user_in.fio)
    users[user.id] = user
    return user


@router.put('/{user_id}', response_model=schemas.User)
def update_user(
        user_id: int,
        user_in: schemas.UserUpdate,
) -> User:
    user = users.get(user_id)
    if not user:
        raise HTTPException(
            status_code=400,
            detail='Пользователя не существует'
        )
    user.fio = user_in.fio
    users[user_id] = user
    return user


@router.delete('/{user_id}', response_model=schemas.User)
def delete_user(
        user_id: int,
) -> User:
    user = users.get(user_id)
    if not user:
        raise HTTPException(
            status_code=400,
            detail='Пользователь не найден'
        )
    del users[user_id]
    return user
