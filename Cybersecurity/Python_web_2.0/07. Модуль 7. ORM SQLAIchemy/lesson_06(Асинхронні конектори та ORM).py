"""
import asyncio
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import async_sessionmaker
"""
# =================================================================================================`
"""
# engine
engine = create_async_engine(
    "postgresql+asyncpg://user:password@host/database",
    echo=True
)

# session factory
AsyncDBSession = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

async def main():

    # варіант 1 — пряме з'єднання
    async with engine.connect() as conn:
        result = await conn.execute(select(User))
        rows = result.fetchall()
        print(rows)

    # варіант 2 — через ORM session (правильніше)
    async with AsyncDBSession() as session:
        result = await session.execute(
            select(User).where(User.name == "Alice")
        )
        user = result.scalars().first()
        print(user)

asyncio.run(main())
"""
# =================================================================================================
"""
engine: AsyncEngine = create_async_engine('postgresql+asyncpg://user:password@host/database', echo=True)
AsyncDBSession = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
"""
# =================================================================================================
"""
повністю асинхронні ORM, які спочатку розроблялися з підтримкою asyncio:
Gino
Pony.
Tortoise
Peewee
"""
# =================================================================================================
