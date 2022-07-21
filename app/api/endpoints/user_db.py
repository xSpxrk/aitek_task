from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app import schemas, crud
from app.api import deps


router = APIRouter()


@router.get('/{user_id}', response_model=schemas.User)
def read_user(
        user_id: int,
        db: Session = Depends(deps.get_db),
):
    return crud.user.get(db, user_id)


@router.post('/', response_model=schemas.User)
def create_user(
        user_in: schemas.UserCreate,
        db: Session = Depends(deps.get_db)
):
    return crud.user.create(db=db, obj_in=user_in)


@router.put('/{user_id}', response_model=schemas.User)
def update_user(
        user_id: int,
        user_in: schemas.UserUpdate,
        db: Session = Depends(deps.get_db)
):
    user = crud.user.get(db=db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=400,
            detail='Пользователя не существует'
        )
    return crud.user.update(db, db_obj=user, obj_in=user_in)


@router.delete('/{user_id}', response_model=schemas.User)
def delete_user(
        user_id: int,
        db: Session = Depends(deps.get_db)

):
    return crud.user.remove(db=db, id=user_id)
