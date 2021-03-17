import boto3
from botocore.client import BaseClient

from settings import settings


def s3_auth() -> BaseClient:

	 """
       Authenticate to S3 using boto3
     """