[![Build](https://github.com/GbrielZanoni/TrabalhoRPA/actions/workflows/streamlit-check.yml/badge.svg)](https://github.com/GbrielZanoni/TrabalhoRPA/actions/workflows/streamlit-check.yml)
[![API Health Check](https://github.com/GbrielZanoni/TrabalhoRPA_API/actions/workflows/api-health.yml/badge.svg)](https://github.com/GbrielZanoni/TrabalhoRPA_API/actions/workflows/api-health.yml)
![Python](https://img.shields.io/badge/python-3.11+-blue)
![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-ff4b4b?logo=streamlit&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-336791?logo=postgresql)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![VirtualEnv](https://img.shields.io/badge/Env-.venv-green)
![Poetry](https://img.shields.io/badge/dependencies-poetry-blue)
![License](https://img.shields.io/github/license/GbrielZanoni/TrabalhoRPA)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-blue)
[![Wiki](https://img.shields.io/badge/docs-wiki-blue)](https://github.com/GbrielZanoni/TrabalhoRPA/wiki)
![Coverage](https://img.shields.io/badge/Coverage-95%25-success)
![CodeQL](https://img.shields.io/badge/CodeQL-Static%20Analysis-blue?logo=github)
![Gitter](https://img.shields.io/badge/Chat-Gitter-red?logo=gitter&logoColor=white)
![Discord](https://img.shields.io/badge/Discord-Energral-blue?logo=discord&logoColor=white)
![PyPI](https://img.shields.io/badge/PyPI-Not%20Published-lightgrey?logo=pypi)
![Made with Love](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)

# 🤖 Atividade de Automação

Este repositório contém a solução desenvolvida pelos integrantes do bootcamp para realizar a prática de **RPA**.

---

## 📌 Sobre o Projeto

O projeto consiste em um sistema completo de **Checklist Digital para Técnicos de Campo**, permitindo:

- Preenchimento digital de inspeções em subestações elétricas via API FastAPI
- Armazenamento em banco PostgreSQL
- Visualização gerencial via painel analítico com **Streamlit**
- Análise de métricas operacionais, alertas e chamados
- CI para monitoramento da API e validação de integridade do sistema

---

## 🧠 Tecnologias Utilizadas

- `Python 3.11+`
- `FastAPI`, `Uvicorn`, `SQLAlchemy`
- `Streamlit`, `Plotly`
- `PostgreSQL` (Render)
- `Pandas`, `OpenPyXL`, `FPDF`, `PyPDF2`
- Organização com `Poetry`, `.env`, `.gitignore`, e `GitHub Actions`

---

## 🌐 Aplicação Online

| Componente | Link |
|------------|------|
| 🔌 **API FastAPI (Render)** | [https://trabalhorpa-api.onrender.com/docs](https://trabalhorpa-api.onrender.com/docs) |
| 📊 **Painel Streamlit**     | *(local ou hospedagem futura)* |

---

## 👨‍💻 Integrantes

| Nome              | GitHub                                     |
|-------------------|--------------------------------------------|
| Ana Julia         | [@4nanotfound](https://github.com/4nanotfound)     |
| Gabriel Zanoni    | [@GbrielZanoni](https://github.com/GbrielZanoni)   |
| Mateus Euzébio    | [@mateuseuz](https://github.com/mateuseuz)         |
| Gabriel Moura     | [@gmoura0](https://github.com/gmoura0 )            |
| João Gabriel      | [@JoaoGabFB](https://github.com/JoaoGabFB)         |
| Maria Delmonaco   | [@mariadelmonaco](https://github.com/mariadelmonaco)|

---

## 📁 Estrutura do Repositório

```text
.github/workflows/       → Workflows de CI 
├── check-api.yml

.env                     → Variáveis de ambiente (não versionadas)
.gitignore               → Arquivos e pastas ignoradas pelo Git
requirements.txt         → Lista de dependências do projeto
README.md                → Documentação principal do repositório

main.py                  → Arquivo principal da API FastAPI
crud.py                  → Lógica de manipulação dos dados
database.py              → Configuração do banco de dados e ORM
models.py                → Definição das tabelas (modelos do banco)
```
