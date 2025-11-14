# ☁️ Cloud Backup Pipeline

Pipeline em Python para gerar relatórios (CSV/Parquet), registrar logs e enviar backups para
AWS S3 e Google Cloud Storage (GCS). Inclui versionamento simples por timestamp e testes automatizados.

**Status:** em desenvolvimento

---

**Sumário**
- **Descrição:** breve visão geral
- **Estrutura:** layout dos arquivos
- **Requisitos:** dependências do projeto
- **Instalação & Configuração:** como preparar o ambiente
- **Uso:** comandos principais
- **CI / Execução agendada:** GitHub Actions
- **Testes:** como executar os testes
- **Contribuição:** como ajudar

---

**Descrição**

Este repositório contém um pipeline de backup que gera relatórios a partir de fontes locais,
converte para formatos CSV/Parquet e envia os artefatos para buckets em AWS S3 e Google Cloud Storage.

---

**Estrutura do repositório** (resumo)

- `scripts/` — scripts auxiliares (ex.: `generate_reports.py`, `run_backup.sh`)
- `src/` — código principal
  - `src/backup_pipeline.py` — orquestra o processo de geração e upload
  - `src/aws_service.py` — funções de integração com AWS S3
  - `src/gcs_service.py` — funções de integração com GCS
  - `src/utils/` — utilitários (`file_utils.py`, `logger.py`)
- `tests/` — testes (ex.: `test_backup.py`)
- `requirements.txt` — dependências Python
- `.github/workflows/` — workflows do GitHub Actions

---

**Requisitos**

- Python 3.10+
- Dependências listadas em `requirements.txt` (instalar via `pip`)
- Credenciais AWS e GCP configuradas (ver seção Configuração)

---

**Instalação & Configuração (local)**

1. Criar e ativar um ambiente virtual (exemplo com PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instalar dependências:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. Configurar credenciais:

- AWS: configure as variáveis de ambiente `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` e `AWS_DEFAULT_REGION`.
- GCP: crie uma service account com permissão para Storage e salve o JSON; exporte `GOOGLE_APPLICATION_CREDENTIALS` apontando para esse arquivo.

Exemplo (PowerShell):

```powershell
$env:AWS_ACCESS_KEY_ID = 'SEU_ACESSO'
$env:AWS_SECRET_ACCESS_KEY = 'SUA_CHAVE'
$env:AWS_DEFAULT_REGION = 'us-east-1'
$env:GOOGLE_APPLICATION_CREDENTIALS = 'C:\caminho\para\credentials\gcp_key.json'
```

Observação: para CI (GitHub Actions) defina os secrets apropriados no repositório.

---

**Uso**

- Gerar relatórios via script:

```powershell
python scripts\generate_reports.py
```

- Executar pipeline (local):

```powershell
python src\backup_pipeline.py
```

- Existe também um script shell em `scripts/run_backup.sh` para ambientes Unix.

---

**Execução agendada (GitHub Actions)**

O workflow em `.github/workflows/daily_backup.yml` executa o pipeline diariamente (configuração do horário no YAML).
No GitHub defina os secrets necessários, por exemplo:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `GCP_KEY_JSON` (ou use `GOOGLE_APPLICATION_CREDENTIALS` com upload seguro do JSON)

---

**Testes**

Executar testes com `pytest`:

```powershell
pytest -q
```

Adicione testes em `tests/` cobrindo funções de upload, geração de arquivos e utilitários.

---

**Como contribuir**

- Abra uma issue descrevendo a proposta ou bug.
- Crie um branch com nome descritivo `feature/...` ou `fix/...`.
- Envie um pull request com descrição e testes quando aplicável.

---

**Autor & Contato**

Rui Francisco de Paula Inácio Diniz — https://github.com/Dev-RuiDiniz

---

