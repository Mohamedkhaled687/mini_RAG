
"""
Data controller for handling file operations in the mini_RAG application.

This module provides functionality for file validation, unique filename generation,
and file processing operations. It handles the business logic for file uploads
and ensures files are properly validated and stored.
"""

from .BaseController import BaseController
from fastapi import APIRouter, Depends, UploadFile
from src.models import ResponseSignal
from .ProjectController import ProjectController
import re
import os
import string
import random


class DataController(BaseController):
    """
    Controller class for handling data-related operations.
    
    This class provides methods for file validation, unique filename generation,
    and file processing. It inherits from BaseController for common functionality.
    """
    
    def __init__(self):
        """
        Initialize the data controller with file size scaling factor.
        
        Sets up the size scale for converting MB to bytes for file size validation.
        """
        super().__init__()
        self.size_scale = 1048576  # 1 MB in bytes (1024 * 1024)

    def validate_uploaded_file(self, file: UploadFile):
        """
        Validate an uploaded file for type and size constraints.
        
        Checks if the file meets the application's requirements for file type
        and size limits as defined in the application settings.
        
        Args:
            file (UploadFile): The uploaded file to validate
            
        Returns:
            tuple: (is_valid: bool, signal: str) - Validation result and response signal
        """
        # Check if file type is allowed
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value

        # Check if file size is within limits (convert MB to bytes)
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False, ResponseSignal.FILE_SIZE_EXCEEDED.value

        # File passed all validation checks
        return True, ResponseSignal.FILE_UPLOAD_SUCCESS.value

    def generate_unique_filepath(self, orig_file_name: str, project_id: str):
        """
        Generate a unique file path for storing an uploaded file.
        
        Creates a unique filename by combining a random string with the cleaned
        original filename. Ensures no filename conflicts by checking for existing files.
        
        Args:
            orig_file_name (str): Original filename from the upload
            project_id (str): ID of the project to store the file in
            
        Returns:
            tuple: (file_path: str, file_id: str) - Full file path and unique file ID
        """
        # Generate random filename component
        random_filename = self.generate_random_string()
        
        # Get project directory path
        project_path = ProjectController().get_project_path(project_id=project_id)

        # Clean the original filename
        clean_file_name = self.get_clean_file_name(org_file_name=orig_file_name)

        # Create initial file path
        new_file_path = os.path.join(
            project_path,
            random_filename + "_" + clean_file_name
        )

        # Ensure filename uniqueness by regenerating if file exists
        while os.path.exists(new_file_path):
            random_filename = self.generate_random_string()
            new_file_path = os.path.join(
                project_path,
                random_filename + "_" + clean_file_name
            )

        # Return file path and file ID (combination of random string and clean filename)
        return new_file_path, random_filename + "_" + clean_file_name

    def get_clean_file_name(self, org_file_name: str):
        """
        Clean and sanitize a filename for safe storage.
        
        Removes special characters and replaces spaces with underscores
        to create a filesystem-safe filename.
        
        Args:
            org_file_name (str): Original filename to clean
            
        Returns:
            str: Cleaned filename safe for filesystem storage
        """
        # Remove any special characters except underscore and dot
        clean_file_name = re.sub(r'[^a-zA-Z0-9_.]', '', org_file_name)

        # Replace spaces with underscores
        clean_file_name = clean_file_name.replace(' ', '_')

        return clean_file_name

    def generate_random_string(self, length=8):
        """
        Generate a random string of specified length.
        
        Creates a random string using lowercase letters and digits.
        Used for generating unique filename components.
        
        Args:
            length (int): Length of the random string to generate (default: 8)
            
        Returns:
            str: Random string of specified length
        """
        letters = string.ascii_lowercase + string.digits
        return ''.join(random.choice(letters) for _ in range(length))