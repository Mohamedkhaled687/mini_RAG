"""
Configuration management for the mini_RAG application.

This module defines the application settings using Pydantic BaseSettings,
which automatically loads configuration from environment variables and .env files.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings class that loads configuration from environment variables.
    
    All settings are loaded from the .env file located in the src directory.
    This class provides type validation and default value handling for configuration.
    """
    # Application metadata
    APP_NAME: str                    # Name of the application
    APP_VERSION: str                 # Current version of the application
    
    # API configuration
    OPEN_API_KEY: str                # OpenAI API key for external services
    
    # File upload configuration
    FILE_ALLOWED_TYPES: list         # List of allowed MIME types for file uploads
    FILE_MAX_SIZE: int               # Maximum file size in MB
    FILE_DEFAULT_CHUNCK_SIZE: int    # Default chunk size for file reading/writing
    
    class Config:
        """Pydantic configuration for settings loading."""
        env_file = "src/.env"        # Path to the environment file


def get_settings():
    """
    Factory function to create and return a Settings instance.
    
    This function is used as a FastAPI dependency to inject settings
    into route handlers and other components.
    
    Returns:
        Settings: Configured settings instance
    """
    return Settings()