# Bot de Atendimento WhatsApp para Restaurante 🍽️📱

## Descrição

Este projeto implementa um **bot de atendimento via WhatsApp** desenvolvido para otimizar a comunicação entre clientes e restaurantes. O bot permite que os clientes consultem o cardápio, façam pedidos, realizem reservas e obtenham informações sobre o estabelecimento, tudo de maneira automatizada e sem a necessidade de interação humana. 🤖🍴

### Tecnologias Utilizadas 💻⚙️

- **Baileys**: Biblioteca para a execução do bot no WhatsApp. Utilizada para interagir com a API do WhatsApp de maneira eficiente e flexível.
- **FastAPI**: Framework web para criar a API que conecta o bot ao banco de dados, garantindo alta performance e desenvolvimento rápido.
- **Python**: Linguagem de programação utilizada para o backend do sistema.
- **MySQL**: Banco de dados relacional utilizado para armazenar as informações do restaurante, pedidos, clientes, entre outros.
- **SQLAlchemy**: Biblioteca ORM para Python para facilitar a manipulação do banco de dados MySQL.

## Funcionalidades 🌟

- **Consulta ao Cardápio**: O bot permite que os clientes visualizem o cardápio do restaurante de forma interativa.
- **Realização de Pedidos**: Os clientes podem fazer pedidos diretamente pelo WhatsApp, selecionando itens do cardápio.
- **Reservas**: O bot ajuda os clientes a realizar reservas de mesas para uma data e hora específicas.
- **Status do Pedido**: Permite que os clientes acompanhem o status do seu pedido em tempo real.
- **Informações do Restaurante**: O bot fornece informações como endereço, horário de funcionamento, formas de pagamento e mais.

## Estrutura 🧱
```plaintext
bot-whatsapp-restaurante/
│
├── app/
│   ├── bot/
│   │   ├── __init__.py
│   │   ├── client.py
│   │   └── handlers.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── session.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── routers.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── pedido.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   └── main.py
│
├── requirements.txt
├── .env.example
└── README.md

```

## Requisitos 📦

Antes de rodar o projeto, garanta que tenha as seguintes dependências instaladas:

- **Python 3.8+**
- **MySQL**
- **Baileys**: Biblioteca para interação com o WhatsApp.
- **FastAPI**: Framework para criação de APIs em Python.
- **SQLAlchemy**: Biblioteca ORM para Python para facilitar a manipulação do banco de dados MySQL.
- **Uvicorn**: Servidor ASGI para rodar a API FastAPI.
- **pip**: Para gerenciar pacotes Python.

## Contribuidores 👥

Este projeto está sendo desenvolvido por:

- [Flávio Davi](https://github.com/flavio-davi) 🧑‍💻
- [Arthur Daladier](https://github.com/Arthur-dev01) 🧑‍💻
- **Luís Felipe** 👨‍💻
- **Renan Pinto** 👨‍💻
- [Thiago Sousa](https://github.com/thiago21sousa21) 🧑‍💻

## Contexto Acadêmico 🎓

Este projeto faz parte da disciplina **Engenharia de Software** do **Curso Técnico em Desenvolvimento de Sistemas** do **IFPI** (Instituto Federal do Piauí), ministrada pelo professor **[Osiris Pires Coelho Filho](https://abrir.link/ooDva)**. 📚

## Licença 📝

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.
