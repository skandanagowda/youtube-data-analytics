import boto3
import os
from dotenv import load_dotenv

# Load AWS credentials from .env
load_dotenv()

# Get credentials from environment variables
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")

# S3 details
BUCKET_NAME = os.getenv("BUCKET_NAME")
FILE_NAME = os.getenv("FILE_NAME")
KEY_NAME = os.getenv("KEY_NAME") 

def upload_to_s3():

    # Initialize S3 client
    s3 = boto3.client(
        "s3",
        region_name=AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )

    # Upload the file
    try:
        with open(FILE_NAME, "rb") as file:
            s3.upload_fileobj(file, BUCKET_NAME, KEY_NAME)
        print(f"Uploaded '{FILE_NAME}' to s3://{BUCKET_NAME}/{KEY_NAME}")
    except Exception as e:
        print(f"Upload failed: {e}")

if __name__ == "__main__":
    upload_to_s3()
