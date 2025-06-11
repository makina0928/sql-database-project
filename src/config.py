from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Configuration settings for the application."""
    POSTGRES_URL: str 

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"  # Ignore any extra fields not defined in the model
    )

settings = Settings()
# This will load the environment variables from the .env file
print(settings.model_dump())