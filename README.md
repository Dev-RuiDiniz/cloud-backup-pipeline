# Cloud Backup Pipeline

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)]()
[![CI: GitHub Actions](https://img.shields.io/badge/CI-GitHub%20Actions-blue)]()

Automação completa para geração, versionamento e armazenamento de relatórios em AWS S3 e Google Cloud Storage com logs estruturados e testes automatizados.

---

## Sumário

- [Sobre o Projeto](#sobre-o-projeto)  
- [Principais Funcionalidades](#principais-funcionalidades)  
- [Arquitetura e Estrutura do Repositório](#arquitetura-e-estrutura-do-repositório)  
- [Pré-requisitos](#pré-requisitos)  
- [Instalação](#instalação)  
- [Configuração (.env)](#configuração-env)  
- [Execução](#execução)  
  - [Executar localmente (Python)](#executar-localmente-python)  
  - [Executar via script Bash](#executar-via-script-bash)  
- [GitHub Actions (CI/CD)](#github-actions-cicd)  
- [Testes](#testes)  
- [Exemplo de Saída](#exemplo-de-saída)  
- [Possíveis Extensões Futuras](#possíveis-extensões-futuras)  
- [Tecnologias](#tecnologias)  
- [Contribuição](#contribuição)  
- [Autor](#autor)  
- [Licença](#licença)

---

## Sobre o Projeto

Este repositório contém uma pipeline de backup em nuvem que:

- Gera relatórios (CSV e Parquet) automaticamente;
- Versiona arquivos por timestamp;
- Faz upload simultâneo para AWS S3 e Google Cloud Storage;
- Mantém logs estruturados por data;
- Pode ser executada manualmente ou por GitHub Actions;
- Inclui testes automatizados (pytest) para garantir confiabilidade.

É ideal como projeto de portfólio para Desenvolvedores Python, Engenheiros de Software e Analistas de Dados.

---

## Principais Funcionalidades

- Geração de relatórios diários (CSV/Parquet).
- Upload para múltiplos provedores (AWS S3 e GCS).
- Versionamento automático por timestamps.
- Logs rotativos e estruturados.
- Execução local e remota (GitHub Actions).
- Testes unitários com fixtures para simular uploads.

---

## Arquitetura e Estrutura do Repositório

Raiz do projeto (resumo):
```
cloud-backup-pipeline/
├── README.md
├── .gitignore
├── requirements.txt
├── .env
├── data/
│   ├── input/
│   └── output/
├── scripts/
│   ├── generate_reports.py
│   └── run_backup.sh
├── src/
│   ├── aws_service.py
│   ├── gcs_service.py
│   ├── backup_pipeline.py
│   └── utils/
│       ├── logger.py
│       └── file_utils.py
├── tests/
│   ├── test_backup.py
└── .github/
    └── workflows/
        └── daily_backup.yml
```

Breve descrição dos componentes:
- scripts/generate_reports.py — Gera relatórios (ex.: vendas, clientes).
- src/aws_service.py — Cliente/operacões AWS S3 (boto3).
- src/gcs_service.py — Cliente/operacões GCS (google-cloud-storage).
- src/backup_pipeline.py — Orquestra geração, versionamento, upload e logs.
- src/utils — Utils (logger, manipulação de arquivos).
- tests — Testes com pytest.

---

## Pré-requisitos

- Python 3.8+
- Contas e credenciais AWS e Google Cloud configuradas
- pip (para instalar dependências)
- (Opcional) virtualenv/venv recomendado

---

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Dev-RuiDiniz/cloud-backup-pipeline.git
cd cloud-backup-pipeline
```

2. Crie um ambiente virtual e instale dependências:
```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
# .venv\Scripts\activate    # Windows (PowerShell)
pip install -r requirements.txt
```

---

## Configuração (.env)

Crie um arquivo `.env` na raiz do projeto com as variáveis necessárias. Exemplo:
```env
# AWS Configuration
AWS_ACCESS_KEY_ID=SEU_AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY=SEU_AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION=us-east-1
AWS_S3_BUCKET=seu-bucket-s3

# Google Cloud Configuration
# Se usar GCP via variável de ambiente, aponte para o arquivo JSON
GOOGLE_APPLICATION_CREDENTIALS=credentials/gcp_key.json
GCS_BUCKET_NAME=seu-bucket-gcs

# Project Settings
LOG_LEVEL=INFO
```

Instruções adicionais:
- Para a GCP você pode definir a variável `GOOGLE_APPLICATION_CREDENTIALS` apontando para o JSON da Service Account, ou injetar o conteúdo via GitHub Secrets (ver seção de CI).
- Coloque o arquivo JSON em `credentials/gcp_key.json` (não comite credenciais sensíveis).

---

## Execução

### Executar localmente (Python)
Execute a pipeline diretamente:
```bash
python src/backup_pipeline.py
```

### Executar via script Bash
```bash
bash scripts/run_backup.sh
```

Ambas as opções geram os relatórios em `data/output/` e fazem upload para os buckets configurados.

---

## GitHub Actions (CI/CD)

O workflow `.github/workflows/daily_backup.yml` está preparado para rodar diariamente (cron) e contém passos para:
- Instalar dependências;
- Configurar credenciais AWS e GCP (via Secrets);
- Executar testes;
- Rodar a pipeline.

Secrets recomendados (Settings → Secrets and variables → Actions):
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION (opcional)
- AWS_S3_BUCKET
- GCP_KEY_JSON (conteúdo do JSON da service account)
- GCS_BUCKET_NAME

Observação: o workflow deve desserializar `GCP_KEY_JSON` para um arquivo durante a execução antes de exportar `GOOGLE_APPLICATION_CREDENTIALS`.

---

## Testes

Executar todos os testes:
```bash
pytest -v
```

Executar testes com cobertura:
```bash
pytest --cov=src --cov-report=html
```

Executar teste específico:
```bash
pytest tests/test_backup.py -v
```

Os testes usam fixtures para simular uploads e arquivos temporários; verifique `tests/test_backup.py`.

---

## Exemplo de Saída

Exemplo de logs e mensagens esperadas:
```
🔄 Iniciando Pipeline de Backup - 2024-01-15 10:30:00
📊 Gerando relatórios...
✅ Relatório CSV gerado: sales_report_20240115_103000.csv
✅ Relatório Parquet gerado: sales_report_20240115_103000.parquet
☁️ Upload para AWS S3... [SUCESSO]
📦 Upload para Google Cloud Storage... [SUCESSO]
📝 Log registrado em: logs/backup_2024-01-15.log
🎯 Pipeline concluída com sucesso!
```

---

## Possíveis Extensões Futuras

- Compressão automática (gzip/zip) dos arquivos antes do upload.
- Notificações (Slack, Telegram, e-mail) sobre o status do backup.
- API REST com FastAPI para acionar backups via HTTP.
- Dashboard em Streamlit com histórico de uploads.
- Suporte a mais provedores (Azure, Backblaze).
- Orquestração com Airflow ou Prefect.
- Política de retenção automática de versões antigas.
- Monitoramento com métricas e alertas.

---

## Tecnologias

- Linguagem: Python 3.8+
- AWS: boto3, S3, IAM
- GCP: google-cloud-storage, Service Accounts
- Data: pandas, CSV, Parquet
- Testes: pytest
- CI/CD: GitHub Actions
- Logging: logging (rotating files)
- Automação: Bash, Cron

---

## Contribuição

Contribuições são bem-vindas! Sugestões de fluxo:
1. Fork o projeto
2. Crie uma branch: `git checkout -b feature/MinhaFeature`
3. Commit suas mudanças: `git commit -m "Add: MinhaFeature"`
4. Push para a branch: `git push origin feature/MinhaFeature`
5. Abra um Pull Request

Leia e siga as boas práticas do repositório e não inclua credenciais em commits.

---

## Autor

Rui Francisco de Paula Inácio Diniz  
Engenheiro de Software | Desenvolvedor Python | Analista de Dados

GitHub: https://github.com/Dev-RuiDiniz  
LinkedIn: (link do perfil)

---

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para detalhes.
