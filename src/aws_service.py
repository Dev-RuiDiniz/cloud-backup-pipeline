import boto3
from botocore.exceptions import ClientError

class AWSService:
    def __init__(self, bucket_name: str):
        self.bucket = bucket_name
        self.s3 = boto3.client("s3")

    def upload_file(self, file_path: str, key: str):
        try:
            self.s3.upload_file(file_path, self.bucket, key)
            return True
        except ClientError as e:
            print(f"Erro ao enviar para S3: {e}")
            return False

    def download_file(self, key: str, destination: str):
        try:
            self.s3.download_file(self.bucket, key, destination)
            return True
        except ClientError as e:
            print(f"Erro ao baixar do S3: {e}")
            return False
