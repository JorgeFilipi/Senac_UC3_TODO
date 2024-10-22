# Sistema de Gerenciamento de Tarefas

## Descrição

Este é um sistema web desenvolvido com Flask para gerenciar tarefas. O sistema permite adicionar novas tarefas, visualizar a lista de tarefas, marcar tarefas como concluídas, remover tarefas da lista, cadastrar e gerenciar usuários, e muito mais.

## Contato:
- **E-mail:** [dev.jdias@gmail.com](mailto:dev.jdias@gmail.com)
- **LinkedIn:** [Jorge Dias](https://www.linkedin.com/in/jorge-dias-66117629b/)

## Estrutura do Projeto

```bash
todo/
│
├── app.py                         # Arquivo principal da aplicação
├── configurations/                 # Instância do SQLAlchemy
│   ├── database.py
│   └── sql_commands.py
├── repositories/
│   ├── task_repository.py         # Repositório de queries SQL
│   └── user_repository.py         # Repositório de queries SQL
├── controllers/
│   ├── tarefa_controller.py       # Lógica das rotas e interação com as regras de negócio
│   └── user_controller.py         # Lógica das rotas e interação com as regras de negócio
├── services/
│   ├── task_service.py            # Regras de negócio (validações, limites, etc.)
│   └── user_service.py            # Regras de negócio (validações, limites, etc.)
├── models/
│   ├── task_model.py              # Estrutura dos dados de tarefa
│   └── user_model.py              # Estrutura dos dados de usuário
├── templates/
│   ├── task_list.html
│   ├── add_user.html
│   └── login.html
├── static/
│   └── styles.css
├── requirements.txt               # Dependências necessárias do projeto
└── .env                           # Variáveis de ambiente
