# Sistema Verde - Licenciamento Ambiental

Este projeto é uma aplicação web simples para gerenciamento de solicitações de licença ambiental de empresas, desenvolvida com Flask e MySQL.

## Funcionalidades

- Cadastro de empresas que solicitam licença ambiental
- Listagem das solicitações cadastradas
- Aceitação e exclusão de solicitações
- Interface web moderna e responsiva

## Requisitos

- Python 3.x
- Flask
- PyMySQL
- MySQL Server (banco de dados chamado `sistema` com tabela `solicitacoes`)

## Instalação

1. Clone o repositório ou baixe os arquivos.
2. Instale as dependências Python:
   ```sh
   pip install flask pymysql
   ```
3. Crie o banco de dados MySQL:
   ```sql
   CREATE DATABASE sistema;
   USE sistema;
   CREATE TABLE solicitacoes (
       id INT AUTO_INCREMENT PRIMARY KEY,
       empresa VARCHAR(255),
       cnpj VARCHAR(20),
       endereco VARCHAR(255),
       proprietario VARCHAR(255),
       tipo_licenca VARCHAR(100)
   );
   ```
4. Configure o acesso ao banco de dados em `app.py` se necessário.

## Como executar

Execute o arquivo principal:

```sh
python app.py
```

Acesse no navegador: [http://localhost:5000](http://localhost:5000)

## Estrutura do Projeto

- [`app.py`](app.py): Código principal da aplicação Flask, rotas e frontend.

## Licença

Projeto acadêmico para fins de estudo.
