from typing import TypeVar, Type, List, Optional
from sqlalchemy.orm import Session
from database.db import Base

T = TypeVar("T", bound=Base)


class BaseRepository:
    """Базовий репозиторій, що інкапсулює стандартні CRUD операції."""

    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model = model

    def create(self, **kwargs) -> T:
        instance = self.model(**kwargs)
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def get_all(self) -> List[T]:
        return self.session.query(self.model).all()

    def get_by_id(self, record_id: int) -> Optional[T]:
        return self.session.query(self.model).filter(self.model.id == record_id).first()

    def update(self, record_id: int, **kwargs) -> Optional[T]:
        instance = self.get_by_id(record_id)
        if instance:
            for key, value in kwargs.items():
                setattr(instance, key, value)
            self.session.commit()
            self.session.refresh(instance)
        return instance

    def delete(self, record_id: int) -> bool:
        instance = self.get_by_id(record_id)
        if instance:
            self.session.delete(instance)
            self.session.commit()
            return True
        return False
