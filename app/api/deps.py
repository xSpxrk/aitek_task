from typing import Generator
from app.db.session import SessionLocal


# Получение объекта базы данных.
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
