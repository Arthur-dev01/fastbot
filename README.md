# Bot de Atendimento WhatsApp para Restaurante

## Descrição

Este projeto implementa um **bot de atendimento via WhatsApp** desenvolvido para otimizar a comunicação entre clientes e restaurantes. O bot permite que os clientes consultem o cardápio, façam pedidos, realizem reservas e obtenham informações sobre o estabelecimento, tudo de maneira automatizada e sem a necessidade de interação humana.

### Tecnologias Utilizadas

- **Baileys**: Biblioteca para a execução do bot no WhatsApp. Utilizada para interagir com a API do WhatsApp de maneira eficiente e flexível.
- **FastAPI**: Framework web para criar a API que conecta o bot ao banco de dados, garantindo alta performance e desenvolvimento rápido.
- **Python**: Linguagem de programação utilizada para o backend do sistema.
- **MySQL**: Banco de dados relacional utilizado para armazenar as informações do restaurante, pedidos, clientes, entre outros.
- **SQLAlchemy**: Biblioteca ORM para Python para facilitar a manipulação do banco de dados MySQL.

## Funcionalidades

- **Consulta ao Cardápio**: O bot permite que os clientes visualizem o cardápio do restaurante de forma interativa.
- **Realização de Pedidos**: Os clientes podem fazer pedidos diretamente pelo WhatsApp, selecionando itens do cardápio.
- **Reservas**: O bot ajuda os clientes a realizar reservas de mesas para uma data e hora específicas.
- **Status do Pedido**: Permite que os clientes acompanhem o status do seu pedido em tempo real.
- **Informações do Restaurante**: O bot fornece informações como endereço, horário de funcionamento, formas de pagamento e mais.

## Requisitos

Antes de rodar o projeto, garanta que tenha as seguintes dependências instaladas:

- **Python 3.8+**
- **MySQL** (ou MariaDB)
- **Baileys**: Biblioteca para interação com o WhatsApp.
- **FastAPI**: Framework para criação de APIs em Python.
- **SQLAlchemy**: Biblioteca ORM para Python para facilitar a manipulação do banco de dados MySQL.
- **Uvicorn**: Servidor ASGI para rodar a API FastAPI.
- **pip** ou **Poetry**: Para gerenciar pacotes Python.

## Instalação

### 1. Clonar o Repositório

Primeiro, faça o clone do repositório para sua máquina local:

```bash
git clone https://github.com/usuario/bot-whatsapp-restaurante.git
cd bot-whatsapp-restaurante
