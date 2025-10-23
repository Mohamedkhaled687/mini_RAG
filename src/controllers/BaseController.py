"""
Base controller class for the mini_RAG application.

This module provides a base class that all other controllers inherit from.
It contains common functionality like settings management, directory path handling,
and utility methods that are shared across different controller types.
"""

from src.helpers import get_settings, Settings
import os
import random
import string


class BaseController:
    """
    Base controller class that provides common functionality for all controllers.
    
    This class handles application settings, directory path management,
    and provides utility methods that are commonly used across different controllers.
    """
    
    def __init__(self):
        """
        Initialize the base controller with common settings and paths.
        
        Sets up application settings, base directory path, and file storage directory.
        """
        # Load application settings
        self.app_settings = get_settings()
        
        # Set up directory paths
        self.base_dir = os.path.dirname(os.path.dirname(__file__))  # Go up two levels from controllers/
        self.file_dir = os.path.join(
            self.base_dir,
            "assets/files"  # Directory for storing uploaded files
        )

    def generate_random_string(self, length: int = 12):
        """
        Generate a random string of specified length.
        
        Creates a random string using ASCII letters and digits.
        Used for generating unique filenames and identifiers.
        
        Args:
            length (int): Length of the random string to generate (default: 12)
            
        Returns:
            str: Random string of specified length
        """
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))