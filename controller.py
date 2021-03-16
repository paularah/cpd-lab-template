from model import Files as FilesModel
from fastapi_sqlalchemy import db


async def save_upload(filename:str, filelink):
    File = FilesModel(filename=filename, filelink=filelink)
    """
    save the s3 file details to the database here
    """
    print('file succefully saved to db')

async def get_all_files():
    # all_files = some query here
     """
     input the query for getting all the fikles from the database here
     """
     return all_files
