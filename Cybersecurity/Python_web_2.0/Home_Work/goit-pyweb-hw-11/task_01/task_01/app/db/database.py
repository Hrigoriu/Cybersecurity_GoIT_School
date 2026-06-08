#app/db/database.py
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from app.core.config import settings

# Створення асинхронного рушія бази даних
engine = create_async_engine(settings.database_url, echo=False)

# Фабрика асинхронних сесій
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)

Base = declarative_base()

async def get_db() -> AsyncSession:
    """
    Залежність (Dependency) для FastAPI, що надає сесію бази даних.
    Гарантує закриття сесії після завершення запиту.
    """
    async with AsyncSessionLocal() as session:
        yield session
