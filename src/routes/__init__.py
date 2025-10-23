"""
Routes package for the mini_RAG application.

This package contains all API route modules that define the endpoints
and request/response handling for the FastAPI application.
"""

# Import route modules
from . import base, data

# Export public API
__all__ = ["base", "data"]
