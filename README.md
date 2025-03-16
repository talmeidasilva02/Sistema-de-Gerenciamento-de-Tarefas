# Sistema de Gerenciamento de Tarefas (To-Do List) em Python
Sistema de Gerenciamento de Tarefas (To-Do List) com funcionalidades básicas

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Um projeto simples, porém bem estruturado, de um sistema de gerenciamento de tarefas (To-Do List) desenvolvido em Python. O projeto utiliza técnicas de programação avançadas, como **MVC (Model-View-Controller)**, **type hints**, **testes unitários** e manipulação de arquivos JSON.

## Funcionalidades

- **Adicionar Tarefa**: Adiciona uma nova tarefa à lista.
- **Listar Tarefas**: Exibe todas as tarefas cadastradas.
- **Concluir Tarefa**: Marca uma tarefa como concluída.
- **Remover Tarefa**: Remove uma tarefa da lista.
- **Salvar e Carregar Tarefas**: As tarefas são salvas em um arquivo JSON e carregadas ao iniciar o programa.

## Como Executar

### Pré-requisitos

- Python 3.8 ou superior instalado.
- Git (opcional, para clonar o repositório).

### Passos para Execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/todo-list-python.git
   cd todo-list-python

2. (Opcional) Crie um ambiente virtual:
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate

3. Execute o programa:
    python main.py

4. Siga as instruções no terminal para interagir com o sistema.

### Executando Testes Unitários
Para garantir que todas as funcionalidades estão funcionando corretamente, execute os testes unitários:
python -m unittest tests/test_task.py

### Tecnologias e Técnicas Utilizadas
Python: Linguagem de programação principal.

MVC (Model-View-Controller): Padrão de arquitetura para organizar o código.

Type Hints: Adição de tipos estáticos para melhorar a legibilidade e manutenção do código.

Testes Unitários: Uso da biblioteca unittest para testar as funcionalidades.

Manipulação de Arquivos JSON: Salvamento e carregamento de tarefas em um arquivo JSON.

### Licença
Este projeto está licenciado sob a licença MIT.

### Contato
Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato:

Nome: Tiago Almeida

Email: tiago@codecity.app