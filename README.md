# Cloud Backup Pipeline (AWS S3 + Google Cloud Storage)

Pipeline automatizada para upload, download e versionamento de arquivos (.csv e .parquet) em buckets AWS S3 e Google Cloud Storage.

## Tecnologias Utilizadas
- Python 3.10+
- boto3
- google-cloud-storage
- pandas
- pyarrow
- logging

## Estrutura do Projeto
src/
  aws_service.py
  gcs_service.py
  backup_pipeline.py
  utils/
    logger.py
    file_utils.py

## Funcionalidades
✔ Upload automatizado para S3 e GCS  
✔ Download das últimas versões  
✔ Versionamento por timestamp  
✔ Logs detalhados  
✔ Pipeline automatizada (cron/Airflow)

## Como Executar
pip install -r requirements.txt  
python src/backup_pipeline.py
