<<<<<<< HEAD
# Sistema Verde - Solicitação de Licença Ambiental

Este projeto é um sistema web simples para cadastro e gerenciamento de solicitações de licença ambiental para empresas.

## Funcionalidades

- Cadastro de empresas solicitando licença ambiental
- Listagem das solicitações cadastradas
- Aceitar ou excluir solicitações
- Interface web moderna e responsiva

## Tecnologias Utilizadas

- Python 3
- Flask
- MySQL (pymysql)
- HTML, CSS, JavaScript

## Como Executar

1. **Clone ou baixe este repositório.**
2. **Instale as dependências Python:**
   ```
   pip install flask pymysql
   ```
3. **Configure o banco de dados MySQL:**
   - Crie um banco chamado `sistema`.
   - Crie a tabela `solicitacoes`:
     ```sql
     CREATE TABLE solicitacoes (
         id INT AUTO_INCREMENT PRIMARY KEY,
         empresa VARCHAR(255),
         cnpj VARCHAR(32),
         endereco VARCHAR(255),
         proprietario VARCHAR(255),
         tipo_licenca VARCHAR(128)
     );
     ```
   - Ajuste as credenciais de acesso ao banco no arquivo `app.py` se necessário.

4. **Execute o servidor Flask:**
   ```
   python app.py
   ```

5. **Acesse no navegador:**
   - [http://localhost:5000/](http://localhost:5000/)

## Observações

- O sistema é apenas um exemplo didático e não possui autenticação.
- Para uso em produção, recomenda-se adicionar camadas de segurança e validação.

---
Desenvolvido para o Projeto de Empresas Sustentáveis - 2025.
=======
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
>>>>>>> b23a182504da41bab998ee2935374cdf6017fbfa
