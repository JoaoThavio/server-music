# 🎵 Server Music

Um servidor simples e eficiente desenvolvido em **Flask (Python)** para **disponibilizar músicas** (arquivos MP3, WAV etc.) a outros projetos, como **aplicativos mobile**, **sites de música** ou **players integrados**.  

Ideal para desenvolvedores que precisam de um **endpoint backend leve e rápido** para servir faixas de áudio hospedadas localmente.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.10+**
- **Flask**
- **Flask-CORS**
- **Gunicorn** (para deploy em produção, ex: Render, Railway, etc.)

---

## 📁 Estrutura do Projeto

server-music/
│
├── app/
│ ├── init.py
│ ├── routes.py # Rotas principais do servidor
│ ├── static/
│ │ └── musics/ # Pasta onde ficam os arquivos de música (.mp3, .wav)
│ └── templates/ # Páginas HTML, se houver interface opcional
│
├── run.py # Ponto de entrada do servidor Flask
├── requirements.txt # Dependências do projeto
└── README.md

yaml
Copiar código

---

## ⚙️ Instalação e Execução Local

### 1. Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/server-music.git
cd server-music
2. Crie um ambiente virtual
bash
Copiar código
python -m venv .venv
source .venv/bin/activate   # (Linux/Mac)
.venv\Scripts\activate      # (Windows)
3. Instale as dependências
bash
Copiar código
pip install -r requirements.txt
4. Execute o servidor
bash
Copiar código
python run.py
O servidor estará disponível em:
👉 http://127.0.0.1:5000

🎧 Endpoints Principais
🔹 GET /musics
Retorna uma lista com todas as músicas disponíveis no servidor.
