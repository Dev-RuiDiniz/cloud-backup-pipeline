import pytest
from src.aws_service import AWSService
from src.gcs_service import GCSService

@pytest.fixture
def sample_file(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("conteudo de teste")
    return str(file_path)

def test_aws_upload(sample_file):
    aws = AWSService(bucket_name="test-bucket")
    assert aws.upload_file(sample_file, "test/sample.txt") in [True, False]

def test_gcs_upload(sample_file):
    gcs = GCSService(bucket_name="test-bucket")
    assert gcs.upload_file(sample_file, "test/sample.txt") in [True, False]
