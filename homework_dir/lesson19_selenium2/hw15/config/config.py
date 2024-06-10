from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    """
    Base configuration class that sets common configurations for all child configurations.

    Attributes:
        model_config (dict): Provides configuration settings for handling environment files:
                             specifying the environment file encoding and handling of extra fields.
    """
    model_config = SettingsConfigDict(env_file_encoding="utf-8", extra="ignore")


class BrowserConfig(BaseConfig):
    """Configuration settings specific to the browser used for automation tests."""
    type: str
    supported_browsers: str
    base_url: str
    page_title: str
    timeout: int
    region: str
    app_version: str
    db_type: str
