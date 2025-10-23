"""
Data schemas for the mini_RAG application.

This module defines Pydantic models for request/response validation
and data serialization in the API endpoints.
"""

from pydantic import BaseModel
from typing import Optional


class ProcessRequest(BaseModel):
    """
    Request model for file processing operations.
    
    This model defines the structure for requests that initiate file processing
    operations such as text chunking and embedding generation.
    """
    file_id: str                    # Unique identifier for the file to process
    chunk_size: Optional[int] = 100  # Size of text chunks for processing (default: 100)
    overlap_size: Optional[int] = 20 # Overlap between consecutive chunks (default: 20)
    do_reset: Optional[int] = 0      # Flag to reset previous processing data (0=no, 1=yes)

    