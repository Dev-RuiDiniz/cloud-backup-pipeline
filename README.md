# Cloud Backup Pipeline (AWS S3 + Google Cloud Storage)


Pipeline automatizada para upload, download e versionamento de arquivos (.csv e .parquet) em buckets AWS S3 e Google Cloud Storage.


## Tecnologias Utilizadas
- Python 3.10+
- boto3 (AWS S3)
- google-cloud-storage (GCS)
- pandas
- pyarrow
- logging


## Estrutura do Projeto
```bash
src/
aws_service.py # Funções de upload/download para AWS S3
gcs_service.py # Funções de upload/download para GCS
backup_pipeline.py # Pipeline principal diário
utils/
logger.py # Configuração de logs
file_utils.py # Utilidades de manipulação de arquivos
```


## Funcionalidades
✔ Upload automatizado para S3 e GCS
✔ Download das últimas versões dos arquivos
✔ Versionamento por timestamp
✔ Logs detalhados
✔ Pipeline automatizado usando cron/Airflow


## Como Executar
```bash
pip install -r requirements.txt
python src/backup_pipeline.py
```