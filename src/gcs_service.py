from google.cloud import storage
import os


class GCSService:
def __init__(self, bucket_name: str):
self.bucket_name = bucket_name
self.client = storage.Client()
self.bucket = self.client.bucket(bucket_name)


def upload_file(self, file_path: str, destination_blob: str):
try:
blob = self.bucket.blob(destination_blob)
blob.upload_from_filename(file_path)
return True
except Exception as e:
print(f"Erro ao enviar para GCS: {e}")
return False


def download_file(self, blob_name: str, destination: str):
try:
blob = self.bucket.blob(blob_name)
blob.download_to_filename(destination)
return True
except Exception as e:
print(f"Erro ao baixar do GCS: {e}")
return False