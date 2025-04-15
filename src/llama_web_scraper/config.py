from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    database_url: str = Field(default="sqlite:///scraper.db", env="DATABASE_URL")
    log_level: str = Field(default="INFO", env="LOG_LEVEL")

    class Config:
        env_file = ".env"


settings = Settings()
