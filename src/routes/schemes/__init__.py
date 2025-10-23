"""
Schemes package for the mini_RAG application.

This package contains Pydantic models and data schemas used for
request/response validation and serialization in the API endpoints.
"""

from .data import ProcessRequest

# Export public API
__all__ = ["ProcessRequest"]
