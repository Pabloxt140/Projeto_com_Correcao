# Sistema Distribuído de Solicitações

Este projeto é um sistema web simples para gerenciar solicitações de licenças de empresas, utilizando Flask (Python), MySQL e integração via API REST.

## Funcionalidades

- Listagem de solicitações cadastradas
- Cadastro de novas solicitações via formulário web
- Integração com serviço externo para persistência das solicitações

## Pré-requisitos

- Python 3.x
- MySQL Server
- Pip (gerenciador de pacotes Python)

## Instalação

1. Clone este repositório:
   ```
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio/projeto
   ```

2. Instale as dependências Python:
   ```
   pip install flask pymysql requests
   ```

3. Configure o banco de dados MySQL:
   - Crie um banco chamado `sistema`
   - Crie a tabela `solicitacoes` conforme necessário

4. Ajuste as configurações de conexão no arquivo `adim.py` se necessário.

## Executando o sistema

1. Inicie o serviço externo (API REST) que recebe as solicitações (certifique-se de que está rodando em `localhost:5002`).
2. Execute a aplicação Flask:
   ```
   python adim.py
   ```
3. Acesse `http://localhost:5000` no navegador.

## Estrutura dos arquivos

- `adim.py`: Código principal da aplicação Flask
- `nova.html`: Template para cadastro de novas solicitações
- `README.md`: Este arquivo

## Observações

- Certifique-se de que o MySQL está rodando e acessível.
- O sistema utiliza flash messages para feedback ao usuário.
- Para dúvidas ou melhorias, abra uma issue ou envie um pull request.
