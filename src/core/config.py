from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """For base project settings."""
    DATABASE_URL: str
    SECRET_KEY: str

    class Config:
        env_file = ".envs/.env"


settings = Settings() # noqa
