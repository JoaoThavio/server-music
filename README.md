🎧 Server Music API

Server Music é um servidor simples de músicas que fornece informações por meio de uma API RESTful.
Você pode acessar o servidor online em:
🔗 https://server-music-joao.onrender.com

🧠 Tecnologias Utilizadas

Python 3

Flask — Framework principal para criação da API

Render — Hospedagem do servidor

JSON — Formato de resposta dos endpoints

HTML / CSS (Static) — Arquivos e capas armazenados em /static/assets

🌐 URL Base
https://server-music-joao.onrender.com

📍 Endpoints
GET /

Retorna uma mensagem confirmando que o servidor está ativo.

Exemplo de resposta:

{
  "message": "Server Music API online"
}

GET /api/songs

Retorna uma lista de todas as músicas disponíveis no servidor.

Exemplo de resposta:

[
  {
    "id": 1,
    "title": "Espresso",
    "artist": "Sabrina Carpenter",
    "cover_url": "/static/assets/espresso.png"
  },
  {
    "id": 2,
    "title": "Say So",
    "artist": "Doja Cat",
    "cover_url": "/static/assets/sayso.png"
  }
]

GET /api/songs/<id>

Retorna os dados de uma música específica pelo ID informado.

Exemplo:

GET /api/songs/1


Resposta:

{
  "id": 1,
  "title": "Espresso",
  "artist": "Sabrina Carpenter",
  "cover_url": "/static/assets/espresso.png"
}

GET /static/assets/<filename>

Retorna a imagem da música (capa) diretamente.
Exemplo:

https://server-music-joao.onrender.com/static/assets/espresso.png

⚠️ Códigos de Erro
Código	Descrição	Exemplo de resposta
404	Música não encontrada	{"error": "Song not found"}
500	Erro interno do servidor	{"error": "Internal server error"}
🧩 Estrutura do Projeto
server-music-main/
├── run.py               # Código principal do servidor Flask
├── requirements.txt     # Dependências do projeto
└── static/
    └── assets/          # Capas das músicas
