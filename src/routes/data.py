"""
Data processing API routes for the mini_RAG application.

This module handles file upload operations, validation, and storage.
It provides endpoints for uploading files to specific projects with proper validation.
"""

import signal
from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
import os
from src.models import ResponseSignal
from src.helpers import get_settings, Settings
from src.controllers import DataController, ProjectController
import aiofiles
import logging
from .schemes.data import ProcessRequest

# Configure logger for error tracking
logger = logging.getLogger('uvicorn.error')

# Create the data router for file processing endpoints
data_router = APIRouter(
    prefix="/api/v1/data",  # API prefix for data operations
    tags=["api/v1/data"]    # OpenAPI documentation tags
)


@data_router.post("/upload/{project_id}")
async def update_data(project_id: str, file: UploadFile, appsettings: Settings = Depends(get_settings)):
    """
    Upload a file to a specific project.
    
    This endpoint handles file uploads with validation for file type, size, and content.
    Files are stored in project-specific directories with unique filenames to prevent conflicts.
    
    Args:
        project_id (str): Unique identifier for the target project
        file (UploadFile): The uploaded file from the request
        appsettings (Settings): Application settings for validation rules
        
    Returns:
        JSONResponse: Success response with file_id or error response with signal
    """
    # Initialize data controller for file operations
    datacontroller = DataController()
    
    # Validate the uploaded file (type, size, etc.)
    is_valid, result_signal = datacontroller.validate_uploaded_file(file=file)
    
    # Return error response if validation fails
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": result_signal
            }
        )
    
    # Generate unique file path and file ID for the uploaded file
    file_path, file_id = datacontroller.generate_unique_filepath(
        orig_file_name=file.filename,
        project_id=project_id
    )

    # Attempt to save the file asynchronously
    try:
        async with aiofiles.open(file_path, "wb") as f:
            # Read file in chunks and write to disk
            while chunk := await file.read(appsettings.FILE_DEFAULT_CHUNCK_SIZE):
                await f.write(chunk)
    except Exception as e:
        # Log error and return failure response
        logger.error(f"Error while uploading the file {e}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": ResponseSignal.FILE_UPLOAD_FAILED.value
            }
        )
    
    # Return success response with file information
    return JSONResponse(
        content={
            "signal": result_signal,
            "file_id": file_id
        }
    )
    
    

@data_router.post("/process/{project_id}")          

async def process_endpoint(project_id : str , process_request : ProcessRequest):

    file_id = process_request.file_id

    return file_id

    