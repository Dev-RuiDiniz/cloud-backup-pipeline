📦 Cloud Backup Pipeline
https://img.shields.io/badge/python-3.8+-blue.svg
https://img.shields.io/badge/license-MIT-green.svg
https://img.shields.io/badge/CI-GitHub%2520Actions-blue

Automação completa de geração, versionamento e armazenamento de relatórios em AWS S3 e Google Cloud Storage.

📋 Sobre o Projeto
Este projeto implementa uma solução completa de backup distribuído em nuvem, com geração automática de relatórios, upload simultâneo para AWS S3 e Google Cloud Storage, logs estruturados, testes automatizados e execução diária via GitHub Actions.

Ele foi projetado para demonstrar habilidades reais em:

Arquitetura de pipelines de dados

Python para automação

Infraestrutura em nuvem

Desenvolvimento escalável e modular

Boas práticas de engenharia de software

Operações contínuas com GitHub Actions

É um projeto ideal para compor o portfólio de um Desenvolvedor Python / Engenheiro de Software / Analista de Dados em ambientes modernos de nuvem.

🎯 Objetivo do Projeto
Criar uma pipeline completa capaz de:

✅ Gerar relatórios automaticamente (CSV e Parquet)

✅ Versioná-los utilizando timestamps

✅ Enviar os arquivos simultaneamente para dois provedores de nuvem:

AWS S3

Google Cloud Storage

✅ Registrar logs estruturados por data

✅ Ser executada manualmente ou automaticamente via GitHub Actions

✅ Garantir confiabilidade com testes automatizados (pytest)

🏗️ Arquitetura da Solução







📁 Estrutura do Projeto
text
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
│   ├── run_backup.sh
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
🧩 Componentes do Sistema
1. 📊 Geração de Relatórios
Arquivo: scripts/generate_reports.py
Gera relatórios diários com vendas, clientes e ticket médio.

2. ☁️ Serviço AWS S3
Arquivo: src/aws_service.py
Upload e download via Boto3.

3. 📦 Serviço Google Cloud Storage
Arquivo: src/gcs_service.py
Upload e download via Google Cloud SDK.

4. 🔄 Pipeline Principal
Arquivo: src/backup_pipeline.py
Integra toda a automação: geração, versionamento, logs e upload.

5. 🛠️ Utilitários
Gerador de timestamps

Log estruturado por dia

Salvamento de CSV/Parquet

6. 🧪 Testes
Arquivo: tests/test_backup.py
Testa upload em S3 e GCS usando fixtures.

7. ⚙️ Automação via GitHub Actions
Arquivo: .github/workflows/daily_backup.yml
Executa diariamente às 03:00 AM.

8. 🖥️ Execução Local
Arquivo: scripts/run_backup.sh

🚀 Quick Start
Pré-requisitos
Python 3.8+

Contas ativas na AWS e Google Cloud

Acesso programático configurado

▶️ Como Executar Localmente
1. Instale as dependências
bash
pip install -r requirements.txt
2. Configure as variáveis de ambiente
Crie um arquivo .env na raiz do projeto:

env
# AWS Configuration
AWS_ACCESS_KEY_ID=seu_acesso_aqui
AWS_SECRET_ACCESS_KEY=sua_chave_secreta_aqui
AWS_DEFAULT_REGION=us-east-1
AWS_S3_BUCKET=seu-bucket-s3

# Google Cloud Configuration
GOOGLE_APPLICATION_CREDENTIALS=credentials/gcp_key.json
GCS_BUCKET_NAME=seu-bucket-gcs

# Project Settings
LOG_LEVEL=INFO
3. Configure as credenciais da Google Cloud
Crie a pasta credentials/ e adicione o arquivo JSON da service account:

bash
mkdir credentials
# Cole o arquivo JSON da service account da GCP aqui
4. Execute a pipeline
Opção 1 - Python:

bash
python src/backup_pipeline.py
Opção 2 - Script Bash:

bash
bash scripts/run_backup.sh
☁️ Execução na Nuvem (GitHub Actions)
A pipeline está configurada para execução automática diária às 03:00 UTC.

Configuração necessária no GitHub:
Acesse Settings → Secrets and variables → Actions

Adicione os seguintes secrets:

Secret Name	Description
AWS_ACCESS_KEY_ID	Sua Access Key da AWS
AWS_SECRET_ACCESS_KEY	Sua Secret Access Key da AWS
GCP_KEY_JSON	Conteúdo JSON da service account da GCP
AWS_S3_BUCKET	Nome do bucket S3
GCS_BUCKET_NAME	Nome do bucket GCS
Fluxo do GitHub Actions:
✅ Instalação automática do ambiente Python

✅ Configuração das credenciais AWS e GCP

✅ Execução dos testes automatizados

✅ Execução da pipeline de backup

✅ Logs detalhados da execução

🧪 Testando o Projeto
Execute a suíte completa de testes:

bash
# Todos os testes
pytest -v

# Testes com cobertura
pytest --cov=src --cov-report=html

# Testes específicos
pytest tests/test_backup.py -v
📊 Exemplo de Saída
text
🔄 Iniciando Pipeline de Backup - 2024-01-15 10:30:00
📊 Gerando relatórios...
✅ Relatório CSV gerado: sales_report_20240115_103000.csv
✅ Relatório Parquet gerado: sales_report_20240115_103000.parquet
☁️ Upload para AWS S3... [SUCESSO]
📦 Upload para Google Cloud Storage... [SUCESSO]
📝 Log registrado em: logs/backup_2024-01-15.log
🎯 Pipeline concluída com sucesso!
🧠 Principais Aprendizados
✔ Arquitetura e Modularização Avançada
Organização do código em camadas de serviço, utils, scripts e testes.

✔ Armazenamento em Nuvem
Autenticação com AWS IAM

Uso do Boto3 para upload e download

Autenticação com Google Service Account

Utilização do Google Cloud Storage client library

✔ Automação com Python
Criação de relatórios dinâmicos com Pandas

Manipulação de dados e serialização em múltiplos formatos

Versionamento automático por timestamps

Estruturação de logs profissionais

✔ DevOps e CI/CD
Pipeline automatizada com GitHub Actions

Execução diária (cron schedule)

Configuração de secrets e variáveis sensíveis

Instalação de dependências e ambiente isolado no workflow

✔ Testes Automatizados
Validação de rotinas de upload

Garantia de estabilidade da pipeline

Uso de fixtures e arquivos temporários

✔ Documentação e Boas Práticas
README profissional

Estrutura limpa de diretórios

Comentários técnicos e código limpo

🚀 Possíveis Extensões Futuras
Compressão automática (gzip/zip) dos arquivos

Sistema de notificações em Slack, Telegram ou e-mail

API REST com FastAPI para acionar backups via HTTP

Dashboard em Streamlit mostrando últimos uploads

Suporte a múltiplos provedores (Azure, Backblaze, Cloudflare)

Orquestração profissional com Airflow ou Prefect

Política de retenção automática de versões antigas

Monitoramento com métricas e alertas

Interface web para gerenciamento dos backups

🛠️ Tecnologias Utilizadas
Categoria	Tecnologias
Linguagem	Python 3.8+
Cloud AWS	Boto3, AWS S3, IAM
Cloud Google	Google Cloud Storage, Service Accounts
Data Processing	Pandas, CSV, Parquet
Testing	Pytest, Fixtures
CI/CD	GitHub Actions, Secrets
Logging	Logging module, Rotating files
Automation	Cron, Bash scripts
👨‍💻 Autor
Rui Francisco de Paula Inácio Diniz
Engenheiro de Software | Desenvolvedor Python | Analista de Dados

https://img.shields.io/badge/GitHub-Dev--RuiDiniz-black?style=flat&logo=github
https://img.shields.io/badge/LinkedIn-Perfil-blue?style=flat&logo=linkedin

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

🔄 Fluxo de Desenvolvimento
Desenvolvimento Local: Teste e validação das funcionalidades

Commit e Push: Versionamento no GitHub

CI/CD Automático: GitHub Actions executa testes

Deploy Automático: Pipeline é executada diariamente

Monitoramento: Verificação dos logs e status

🤝 Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para:

Fork o projeto

Criar uma branch para sua feature (git checkout -b feature/AmazingFeature)

Commit suas mudanças (git commit -m 'Add some AmazingFeature')

Push para a branch (git push origin feature/AmazingFeature)

Abrir um Pull Request

⭐ Se este projeto foi útil, considere dar uma estrela no repositório!

Este projeto foi desenvolvido para demonstrar habilidades reais em arquitetura de pipelines de dados, Python para automação, infraestrutura em nuvem e desenvolvimento escalável e modular.

