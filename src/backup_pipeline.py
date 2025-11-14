from utils.logger import logger
from utils.file_utils import FileUtils
from aws_service import AWSService
from gcs_service import GCSService
import pandas as pd

class BackupPipeline:
    def __init__(self):
        self.aws = AWSService(bucket_name="seu-bucket-s3")
        self.gcs = GCSService(bucket_name="seu-bucket-gcs")

    def run(self):
        logger.info("Pipeline iniciada.")

        df = pd.DataFrame({"vendas": [10, 20, 30]})

        timestamp = FileUtils.generate_timestamp()
        filename = f"relatorio_{timestamp}"

        csv_path, parquet_path = FileUtils.save_dataframe(df, filename)
        logger.info(f"Relatórios gerados: {csv_path}, {parquet_path}")

        self.aws.upload_file(csv_path, f"relatorios/{filename}.csv")
        self.aws.upload_file(parquet_path, f"relatorios/{filename}.parquet")

        self.gcs.upload_file(csv_path, f"relatorios/{filename}.csv")
        self.gcs.upload_file(parquet_path, f"relatorios/{filename}.parquet")

        logger.info("Pipeline concluída com sucesso.")

if __name__ == "__main__":
    pipeline = BackupPipeline()
    pipeline.run()
