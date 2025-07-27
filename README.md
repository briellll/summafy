# SUMMAFY

Uma API simples e eficiente para sumarização de textos utilizando modelos de linguagem da Hugging Face.

## ✨ Features

* ✔️ API RESTful construída com FastAPI.
* ✔️ Validação de dados de entrada e saída com Pydantic.
* ✔️ Sumarização de alta qualidade com a biblioteca Transformers da Hugging Face.

## 🛠️ Pilha de Tecnologias

* **Framework:** FastAPI
* **Servidor ASGI:** Uvicorn
* **Modelagem de Dados:** Pydantic
* **NLP/IA:** Hugging Face Transformers, PyTorch
* **Gerenciamento de Dependências:** Poetry
* **Testes:** Pytest, Pytest-Cov
* **Qualidade de Código (Lint & Format):** Ruff
* **Gerenciador de Tarefas:** Taskipy

## 🚀 Começando

Siga estas instruções para ter uma cópia do projeto rodando na sua máquina local para desenvolvimento e testes.

### Pré-requisitos

* [Python 3.13+](https://www.python.org/downloads/)
* [Poetry](https://python-poetry.org/docs/#installation)

### Instalação

1.  Clone o repositório para a sua máquina:
    ```bash
    git clone [https://github.com/seu-usuario/summafy.git](https://github.com/seu-usuario/summafy.git)
    cd summafy
    ```

2.  Instale as dependências do projeto com o Poetry:
    ```bash
    poetry install
    ```

### Rodando a Aplicação

Para iniciar o servidor de desenvolvimento com hot-reload, use o comando `taskipy` que configuramos:

```bash
poetry run task run