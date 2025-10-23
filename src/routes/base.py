"""
Base API routes for the mini_RAG application.

This module defines the basic API endpoints that provide application information
and health check functionality.
"""

from fastapi import APIRouter, Depends
import os
from src.helpers import get_settings, Settings

# Create the base router with API versioning
base_router = APIRouter(
    prefix="/api/v1",  # API version prefix
    tags=["api/v1"]    # OpenAPI documentation tags
)


@base_router.get("/")
async def welcome(app_settings: Settings = Depends(get_settings)):
    """
    Welcome endpoint that returns basic application information.
    
    This endpoint provides the application name and version from environment settings.
    It serves as a health check and basic API information endpoint.
    
    Args:
        app_settings (Settings): Application settings injected via dependency injection
        
    Returns:
        dict: Dictionary containing app_name and app_version
    """
    # Extract application information from settings
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION

    return {
        "app_name": app_name,
        "app_version": app_version
    }