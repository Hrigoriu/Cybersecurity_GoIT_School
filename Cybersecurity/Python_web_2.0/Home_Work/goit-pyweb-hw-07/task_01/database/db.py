from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager
from config import settings
from utils.logger import RetroLogger

# Ініціалізація рушія бази даних
try:
    engine = create_engine(settings.database_url, echo=False)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
except Exception as e:
    RetroLogger.error(f"Помилка підключення до БД: {e}")
    raise


@contextmanager
def get_db_session():
    """Контекстний менеджер для управління життєвим циклом сесії БД."""
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        RetroLogger.error(f"Транзакцію скасовано через помилку: {e}")
        raise
    finally:
        db.close()
