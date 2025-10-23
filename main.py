"""
Main FastAPI application entry point for the mini_RAG project.

This module initializes the FastAPI application and includes all route routers.
The application provides API endpoints for file uploads and basic application information.
"""

from fastapi import FastAPI
from src.routes import base, data

# Initialize the FastAPI application
app = FastAPI(
    title="Mini RAG API",
    description="A minimal RAG (Retrieval-Augmented Generation) application for file processing",
    version="0.1.0"
)

# Include API route routers
app.include_router(base.base_router)  # Base API routes (welcome endpoint)
app.include_router(data.data_router)  # Data processing routes (file upload)
