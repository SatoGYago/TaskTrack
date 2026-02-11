# TaskTrack (Console Task Tracker)

TaskTrack is a simple **console-based task manager** built in **Python**.  
It lets you **add**, **list**, **complete**, and **remove** tasks, saving everything to a `tasks.json` file so your data persists between runs.

## Features

- Add tasks with:
  - Title
  - Date (string input)
  - Priority (1 / 2 / 3)
- List tasks by priority (1/2/3) or list completed tasks
- Mark tasks as completed by ID
- Remove tasks by ID
- Persistent storage using JSON (`tasks.json`)
- Modular project structure (`main.py`, `logic.py`, `storage.py`)

## Project Structure

tasktrack/
├── main.py # CLI menu + user interaction
├── logic.py # task operations (add/list/complete/remove)
├── storage.py # JSON persistence (load/save)
└── tasks.json # created automatically after saving tasks


## Requirements

- Python 3.10+ (recommended)
- No external libraries required

## How to Run

1. Clone or download this project
2. Open a terminal inside the project folder
3. Run:

```bash
python main.py

Usage (Menu Options)

When you run the program, you will see:

1 Add tasks

2 Complete tasks

3 Remove tasks

4 List tasks

5 Clean console

6 Exit

Add Task

You will be prompted for:

Title

Date

Priority (1/2/3)

Complete Task

Enter the task ID you want to mark as completed.

Remove Task

Enter the task ID you want to remove.

List Tasks

Enter:

1 → list pending tasks with priority 1

2 → list pending tasks with priority 2

3 → list pending tasks with priority 3

4 → list completed tasks

Data Format (tasks.json)

Tasks are stored as a list of dictionaries like:
[
  {
    "id": 1,
    "title": "Study CS50",
    "date": "2026-02-11",
    "priority": 2,
    "done": false
  }
]

Notes

IDs are generated automatically (max existing ID + 1).

Listing tasks does not modify the file (only add/complete/remove operations save).

Possible Improvements (Future Ideas)

Validate date format (YYYY-MM-DD)

Add an option to list all pending tasks (sorted by priority)

Edit task title/date/priority

Add search by keyword

Add automated tests

Made for practice with:
functions, lists/dicts, file handling, JSON, and modular code organization.

---

## 🇧🇷 Versão em Português

### Sobre o Projeto

O **TaskTrack** é um gerenciador de tarefas em modo console desenvolvido em **Python**.  
Ele permite adicionar, listar, concluir e remover tarefas, salvando os dados em um arquivo `tasks.json` para manter a persistência entre execuções.

###  Funcionalidades

- Adicionar tarefas com:
  - Título
  - Data (texto simples)
  - Prioridade (1 / 2 / 3)
- Listar tarefas por prioridade
- Listar tarefas concluídas
- Marcar tarefas como concluídas pelo ID
- Remover tarefas pelo ID
- Persistência de dados utilizando JSON
- Estrutura modular separando lógica, armazenamento e interface

### Estrutura do Projeto

tasktrack/
├── main.py # Interface e menu interativo
├── logic.py # Regras de negócio (add, list, complete, remove)
├── storage.py # Leitura e escrita no arquivo JSON
└── tasks.json # Criado automaticamente após salvar tarefas


### Tecnologias Utilizadas

- Python 3
- Manipulação de arquivos
- JSON
- Estrutura modular de código

### Como Executar

1. Baixe ou clone o projeto
2. Abra o terminal na pasta do projeto
3. Execute:

```bash
python main.py

Objetivo do Projeto

Este projeto foi desenvolvido para praticar:

Funções

Listas e dicionários

Manipulação de arquivos

Persistência com JSON

Organização modular do código

Separação de responsabilidades

Melhorias Futuras

Validação de formato de data

Listar todas as tarefas pendentes ordenadas por prioridade

Editar tarefas existentes

Busca por palavra-chave

Implementação de testes automatizados

::contentReference[oaicite:0]{index=0}
