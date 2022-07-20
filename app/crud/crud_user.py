from app.crud.base import CRUDBase
from app.models.user_db import User
from app.schemas.user import UserCreate, UserUpdate

from sqlalchemy.orm import Session


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):

    def create(self, db: Session, obj_in: UserCreate) -> User:
        db_obj = User(
            fio=obj_in.fio
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, *, db_obj: User, obj_in: UserUpdate) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


user = CRUDUser(User)
