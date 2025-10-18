import signal
from fastapi import APIRouter, Depends , UploadFile , status
from fastapi.responses import JSONResponse
import os
from src.models import ResponseSignal
from src.helpers import get_settings, Settings
from src.controllers import DataController, ProjectController
import aiofiles
import logging


logger = logging.getLogger('uvicorn.error')
data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api/v1/data"]
)

@data_router.post("/upload/{project_id}")
async def update_data(project_id: str, file: UploadFile, appsettings: Settings = Depends(get_settings)):
    
    datacontroller = DataController()
    # validate the file properties 
    is_valid , result_signal = datacontroller.validate_uploaded_file(file=file)
    
    if not is_valid :
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST ,
            content =  {
                "signal" : result_signal
            }
                        
        )
    
    project_dir_path = ProjectController().get_project_path(project_id=project_id)

    file_path = datacontroller.generate_unique_filename(
        orig_file_name=file.filename,
        project_id=project_id
    )


    try :
        async with aiofiles.open(file_path , "wb" ) as f :
            while chunk := await file.read(appsettings.FILE_DEFAULT_CHUNCK_SIZE):
                await f.write(chunk)
    except Exception as e :

        logger.error(f"Error while uploading the file {e}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST ,
            content =  {
                "signal" : ResponseSignal.FILE_UPLOAD_FAILED.value
            }
                        
        )
    return JSONResponse (
        content={
            "signal" : result_signal
        }
    )
    
    
    