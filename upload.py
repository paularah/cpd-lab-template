
from botocore.exceptions import ClientError
from settings import settings
from controller import save_upload


async def upload_file_to_s3(s3_client, file_obj, bucket, folder, object_name=None):
    if object_name is None:
        object_name = file_obj
    # Upload the file
    try:
        """
       Input the code to upload your file to your S3 bucket here
       """

    except ClientError as e:
        print(e)
        return False
    return True

