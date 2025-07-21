import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    SQL_HOST = os.environ.get("SQL_HOST")
    SQL_PORT = os.environ.get("SQL_PORT")
    SQL_USER = os.environ.get("SQL_USER")
    SQL_PASSWORD = os.environ.get("SQL_PASSWORD")
    SQL_NAME = os.environ.get("SQL_NAME")

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.SQL_USER}:{self.SQL_PASSWORD}@{self.SQL_HOST}:{self.SQL_PORT}/{self.SQL_NAME}"


settings = Settings()
