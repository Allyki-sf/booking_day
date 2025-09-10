from pydantic import BaseModel
from pydantic_settings import BaseSettings


class DbSettings(BaseModel):
    db_url: str = "sqlite+aiosqlite:///./db.sqlite3"
    db_echo: bool = True
    #db_echo: bool = False


class Settings(BaseSettings):
    db_run: DbSettings = DbSettings()

settings = Settings()