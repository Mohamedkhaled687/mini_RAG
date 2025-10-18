
from .BaseController import BaseController
from fastapi import APIRouter, Depends , UploadFile
from src.models import ResponseSignal
from .ProjectController import ProjectController
import re
import os
import string
import random 


class DataController(BaseController):
    
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576

    
    def validate_uploaded_file(self , file : UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES :
            return False , ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value

        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale :
            return False , ResponseSignal.FILE_SIZE_EXCEEDED.value

        return True , ResponseSignal.FILE_UPLOAD_SUCCESS.value

    
    def generate_unique_filename(self , orig_file_name : str , project_id : str):
        random_filename = self.generate_random_string()
        project_path = ProjectController().get_project_path(project_id=project_id)

        clean_file_name = self.get_clean_file_name(org_file_name=orig_file_name)

        new_file_path = os.path.join(
            project_path ,
            random_filename + "_" + clean_file_name
        )

        while os.path.exists(new_file_path):
            random_filename = self.generate_random_string()
            new_file_path = os.path.join(
                project_path , 
                random_filename + "_" + clean_file_name
            )

        return new_file_path
        

    def get_clean_file_name(self , org_file_name : str):
        #remove any special characters , except the underscore and the dot
        clean_file_name = re.sub(r'[^a-zA-Z0-9_.]', '', org_file_name)

        # replace spaces with underscores
        clean_file_name = clean_file_name.replace(' ', '_')

        return clean_file_name

    def generate_random_string(self, length=8):
        """Generate a random string of specified length"""
        letters = string.ascii_lowercase + string.digits
        return ''.join(random.choice(letters) for _ in range(length))