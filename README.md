# 🏥 Sistema de Gerenciamento de Pacientes Hospitalares

## 📋 Descrição

Este projeto é um sistema de gerenciamento de pacientes para hospitais, que permite:

- 👤 **Cadastro de pacientes** com nome, CPF e prioridade médica.
- 📄 **Visualização dos pacientes** em uma lista ordenada por prioridade.
- 🔁 **Ordenação dinâmica** clicando nos cabeçalhos das colunas CPF e Prioridade.
- 📤 **Exportação dos dados** dos pacientes para um arquivo XML.
- 💻 **Interface tanto em linha de comando (CLI)** quanto **interface gráfica (Tkinter)**.
- 📊 **Estrutura de dados não linear** utilizando Heap (fila de prioridade) e Hash Table.

---

## 🏗️ Estrutura do Projeto

sistema_hospitalar/

├── sistema.py   # Lógica do sistema e estrutura dos dados

├── interface_cli.py   # Interface de linha de comando (CLI)

├── interface_tkinter.py   # Interface gráfica com Tkinter

├── pacientes.xml   # Arquivo gerado na exportação dos dados

├── diagrama_estrutura.png   # Diagrama da estrutura de dados

├── README.md   # Este arquivo

└── requisitos.txt   # Bibliotecas necessárias (opcional)


---

## 💻 Como Executar

### ✅ Requisitos:

- Python 3.10 ou superior  
- Bibliotecas padrão do Python (não requer bibliotecas externas)

### 🚀 Executar Interface Gráfica (Tkinter):

python interface_tkinter.py

### 🚀 Executar Interface de Linha de Comando (CLI):

python interface_cli.py


---


## 🔗 Funcionalidades

- 👤 Cadastro de Pacientes: Nome, CPF e Prioridade (1 a 10).

- 🔍 Busca e Ordenação: Clique nos cabeçalhos CPF ou Prioridade para ordenar crescente/decrescente.

- 🗂️ Exportação XML: Dados salvos em pacientes.xml para backup ou leitura em outros sistemas.



---


## 🗺️ Diagrama da Estrutura de Dados

Diagrama da estrutura

- Hash Table: Relaciona CPF com os dados do paciente.

- Heap (Fila de Prioridade): Garante que pacientes mais urgentes apareçam primeiro.

- Árvore (em desenvolvimento): Para histórico de atendimentos.


---


## 👨‍💻 Desenvolvido por:
-Gabriel Gonçalves da Silva

-Luiz Felipe Barbosa de Lucena



---
## Disciplina 

Estruturas de Dados I - UDF 

Professora: Kadidja Valeria Reginaldo de Oliveira





 
