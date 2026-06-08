#app/main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.contacts import router as contacts_router
from app.db.database import engine, Base
from app.core.logger import log

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan events.
    Створює таблиці при старті, якщо вони не існують.
    В реальному проекті використовуйте Alembic (міграції).
    """
    log.info("SYSTEM BOOT: Ініціалізація бази даних терміналу...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    log.info("SYSTEM READY: База даних синхронізована. Очікування з'єднань...")

    yield

    log.info("SYSTEM SHUTDOWN: Вимкнення терміналу та закриття з'єднань...")
    await engine.dispose()

app = FastAPI(
    title="Terminal OS - Contact Manager",
    description="REST API для управління контактами з естетикою Retro-Tech.",
    version="1.0.0",
    lifespan=lifespan
)

# Підключення роутера з ендпоінтами
app.include_router(contacts_router)

@app.get("/", tags=["Health"])
async def health_check():
    log.info("PING: Здійснено перевірку статусу системи.")
    return {"status": "Terminal OS is online", "database": "connected"}
