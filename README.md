# Sistema de Gerenciamento de Tarefas
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/JorgeFilipi/JorgeFilipi/blob/main/LICENSE) 

## Origem do prjeto

Este projeto foi desenvolvido durante as aulas do curso de Python, ministrado pelo Senac, na terceira disciplina, sob a orientação e supervisão do professor Luis Paulo Lessa de Assis. Segue o link do GitHub do professor:
- **GitHubn:** [lpjunior](https://github.com/lpjunior)

## Descrição

Este é um sistema web desenvolvido com Flask para gerenciar tarefas. O sistema traz algumas funcionalidades:
  - Adicionar novas tarefas;
  - Visualizar a lista de tarefas;
  - Marcar tarefas como concluídas;
  - Remover tarefas da lista;
  - Cadastrar e gerenciar usuários.




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

```

## Contato:
- **E-mail:** [dev.jdias](mailto:dev.jdias@gmail.com)
- **LinkedIn:** [Jorge Dias](https://www.linkedin.com/in/jorge-dias-66117629b/)
