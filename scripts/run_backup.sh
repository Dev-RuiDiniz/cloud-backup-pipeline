#!/bin/bash

source .env

echo "Iniciando pipeline de backup..."
python3 src/backup_pipeline.py
echo "Backup finalizado com sucesso."
