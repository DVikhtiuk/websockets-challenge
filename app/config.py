
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment."""

    # Redis
    redis_url: str = "redis://localhost:6379"

    # Server
    host: str = "localhost"
    port: int = 8000
    workers: int = 1

    # Shutdown
    shutdown_timeout_minutes: int = 30

    # Notifications
    notification_interval_seconds: int = 10

    # Logging
    log_level: str = "INFO"

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()