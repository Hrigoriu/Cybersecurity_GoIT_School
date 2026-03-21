from utils.logger import RetroLogger


class Settings:
    """
    Клас конфігурації проєкту.
    """

    DB_USER = "postgres"
    DB_PASSWORD = "supermysecretpassword"
    DB_HOST = "127.0.0.1"
    DB_PORT = "5433"
    DB_NAME = "postgres"

    @property
    def database_url(self) -> str:
        """Формує DSN (Data Source Name) для підключення SQLAlchemy."""
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
