from botocore.client import BaseClient
from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
from fastapi.responses import JSONResponse
from s3 import s3_auth
from upload import upload_file_to_s3
from settings import settings
from typing import Optional
from schema import FileList
from controller import get_all_files

router = APIRouter()

@router.post("/upload", status_code=status.HTTP_201_CREATED, summary="Upload files to AWS S3 Buckets",
             description="Upload a file to AWS S3 bucket", name="UPLOAD file to AWS S3",
             response_description="uploaded file successfully")
async def upload_file(folder: Optional[str] = '/', s3: BaseClient = Depends(s3_auth), myFile: UploadFile = File(...)):
      """
       call upload_file_to_s3 function and pass boto3 client
     """  
        

@router.get("/files",  description="returns all files in the database", name="GET files from db")
async def get_files():
      """
       Retrieve data from DB by calling get_all_files function
     """
