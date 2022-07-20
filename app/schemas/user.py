from pydantic import BaseModel


class UserBase(BaseModel):
    fio: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    pass


class UserCreate(UserBase):
    pass
