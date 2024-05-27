from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    """
    Base configuration class that sets common configurations for all child configurations.

    Attributes:
        model_config (dict): Provides configuration settings for handling environment files:
                             specifying the environment file encoding and handling of extra fields.
    """
    model_config = SettingsConfigDict(env_file_encoding="utf-8", extra="ignore")


class APIConfig(BaseConfig):
    """Configuration settings for API testing."""
    url: str
