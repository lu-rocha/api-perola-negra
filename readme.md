🏴‍☠️ API Pérola Negra


API desenvolvida com Flask em Python, representando o navio Pérola Negra (Piratas do Caribe). A aplicação permite consultar, adicionar, atualizar e remover tripulantes fictícios do navio.


📁 Estrutura do Projeto

.
├── api.py               # Arquivo principal da aplicação Flask
├── tripulantes.json     # "Banco de dados" com os personagens (ID e nome)
├── requirements.txt     # Dependências do projeto
├── Dockerfile           # Configuração para build da imagem Docker


🚀 Tecnologias Utilizadas


Python 3.11-slim
Flask
JSON (para armazenamento dos dados)
Docker (opcional, para containerizar a aplicação)


🔧 Instalação e Execução Local


1. Clone o repositório
git clone https://github.com/toolbox-tech/onboarding
cd  1-criacao-api / lucimara
2. Crie e ative um ambiente virtual (opcional)
python -m venv venv
source venv/bin/activate  # ou `venv\Scripts\activate` no Windows
3. Instale as dependências
pip install -r requirements.txt
4. Execute a aplicação
python api.py


A API estará disponível em: http://localhost:5000


🧭 Rotas da API


Método	Rota	Descrição
GET	/personagens	Retorna todos os personagens
GET	/personagens/<id>	Retorna um personagem pelo ID
POST	/personagens	Adiciona um novo personagem
PUT	/personagens/<id>	Atualiza os dados de um personagem
DELETE	/personagens/<id>	Remove um personagem da tripulação


📦 Docker (opcional)


Se desejar rodar a API em um container:


# Build da imagem
docker build -t perola-negra-api .


# Execução do container
docker run -p 5000:5000 perola-negra-api


👥 Tripulação Inicial
A aplicação começa com 3 tripulantes fictícios armazenados em um arquivo .json. Você pode expandir a tripulação utilizando a rota de criação (POST).


📌 Observações


A API é simples e usa um arquivo .json como base de dados apenas para fins de aprendizado.
Ideal para treinar conceitos de Flask, rotas REST e Docker.