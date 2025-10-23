"""
Project controller for managing project directories in the mini_RAG application.

This module handles project-related operations such as creating and managing
project directories for file storage and organization.
"""

from .BaseController import BaseController
from fastapi import UploadFile
from src.models import ResponseSignal
import os


class ProjectController(BaseController):
    """
    Controller class for handling project-related operations.
    
    This class manages project directories and provides methods for
    creating and accessing project-specific file storage locations.
    """
    
    def __init__(self):
        """
        Initialize the project controller.
        
        Calls the parent BaseController constructor to set up common functionality.
        """
        super().__init__()

    def get_project_path(self, project_id: str):
        """
        Get or create the directory path for a specific project.
        
        Creates a project-specific directory if it doesn't exist and returns
        the full path to the project directory for file storage.
        
        Args:
            project_id (str): Unique identifier for the project
            
        Returns:
            str: Full path to the project directory
        """
        # Create project-specific directory path
        project_dir = os.path.join(
            self.file_dir,  # Base file directory from BaseController
            project_id      # Project-specific subdirectory
        )

        # Create directory if it doesn't exist
        if not os.path.exists(project_dir):
            os.makedirs(project_dir)

        return project_dir