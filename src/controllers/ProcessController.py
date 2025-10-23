from .BaseController import BaseController
from .ProjectController import ProjectController
import os
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyMuPDFLoader


class ProcessController(BaseController):

    def __init__(self , project_id : str):
        super().__init__()
        self.project_id = project_id # Get the project_id from caller
        self.project_path = ProjectController().get_project_path(project_id=project_id) # get the project path from ProjectController

    

    def get_file_extension(self , file_id : str):
        return os.path.splitext(file_id)[-1]