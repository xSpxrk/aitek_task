from sqlalchemy import Integer, Column, String

from app.db.base_class import Base


class User(Base):
    """
        Класс пользователя, если репозиторий настроен для хранения данных в базе данных.
    """
    id = Column(Integer, primary_key=True)
    fio = Column(String)
