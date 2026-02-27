from dotenv import load_dotenv

load_dotenv(override=True)

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    DATABASE_URL: str
    PORT: int
    HOST: str
    RELOAD: bool

    pass


settings = Settings()
