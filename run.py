from flask import Flask, jsonify
from flask_cors import CORS


app= Flask(__name__)
CORS(app)


MUSICAS_DB = [
    {
        "id": 1,
        "title": "ABALO EMOCIONAL",
        "artist": "Luan Santana",
        "url": "/static/musicas/Luan Santana - ABALO EMOCIONAL.mp3",
        "imageUrl": "/static/assets/abalo.png"
    },
    {
        "id": 2,
        "title": "Espresso",
        "artist": "Sabrina Carpenter",
        "url": "/static/musicas/Sabrina Carpenter - Espresso.mp3",
        "imageUrl": "/static/assets/espresso.png"
    },
    {
        "id": 3,
        "title": "Shape of You",
        "artist": "Ed Sheeran",
        "url": "/static/musicas/Ed Sheeran - Shape of You.mp3"
    },
    {
        "id": 4,    
        "title": "Say So",
        "artist": "Doja cat",
        "url": "/static/musicas/Doja Cat - Say So (Official Video).mp3",
        "imageUrl": "/static/assets/sayso.png"
    },

    {
        "id": 5,
        "title": "Welcome to New York",
        "artist": "Taylor Swift",
        "url": "/static/musicas/Taylor Swift - Welcome To New York (Taylor's Version) (Lyric Video) - TaylorSwiftVEVO (youtube).mp3",
        "imageUrl": "/static/assets/ny.png"
    },
    {
        "id": 6,
        "title": "Toosie Slide",
        "artist": "Drake",
        "url": "/static/musicas/Drake - Toosie Slide (Official Explicit Audio).mp3",
        "imageUrl": "/static/assets/slide.png"
    },
    {
        "id": 7,
        "title": "Solteirou",
        "artist": "Luan Santana",
        "url": "/static/musicas/Luan Santana - SOLTEIROU  (LUAN CITY DELUXE) - Luan Santana (youtube).mp3",
        "imageUrl": "/static/assets/solteirou.png"
    },
    {
        "id": 8,
        "title": "Coração Cigano",
        "artist": "Luan Santana",
        "url": "/static/musicas/Luan Santana - CORAÇÃO CIGANO feat Luísa Sonza (LUAN CITY) - Luan Santana.mp3",
        "imageUrl": "/static/assets/coração-cigano.png"
    },
    {
        "id": 9,
        "title": "Tanto Faz",
        "artist": "Luan Santana",
        "url": "/static/musicas/Luan Santana - Tanto Faz - (DVD O Nosso Tempo é hoje) - Luan Santana.mp3",
        "imageUrl": "/static/assets/tanto_faz.png"
    },
    {
        "id": 10,
        "title": "God's Plan",
        "artist": "Drake",
        "url": "/static/musicas/God's Plan - Drake.mp3",
        "imageUrl": "/static/assets/drake.png"
    },
    {
        "i  d": 11,
        "title": "Ruby",
        "artist": "Kaiser Chiefs",
        "url": "/static/musicas/Kaiser Chiefs - Ruby (Official Video) - KaiserChiefsVEVO.mp3",
        "imageUrl": "/static/assets/ruby.png"
    },
    {
        "id": 12,
        "title": "The Alee On The Radar",
        "artist": "Alee",
        "url": "/static/musicas/The Alee On The Radar Freestyle (OTR Brazil 🇧🇷) - On The Radar Radio.mp3",
        "imageUrl": "/static/assets/alee-on.png"
    },
    {
        "id": 13,
        "title": "Solta minha blusa",
        "artist": "Pumapjl",
        "url": "/static/musicas/01. pumapjl, SonoTWS - SOLTA MINHA BLUSA - pumapjl (youtube).mp3",
        "imageUrl": "/static/assets/solta-blusa.png"
    },
    {
        "id": 14,
        "title": "O que é meu ninguem me tira",
        "artist": "Pumapjl",
        "url": "/static/musicas/04. pumapjl, SonoTWS - OQUE É MEU NINGUÉM ME TIRA - pumapjl (youtube).mp3",
        "imageUrl": "/static/assets/solta-blusa.png"
    },
    {
        "id": 15,
        "title": "Mar",
        "artist": "Pumapjl",
        "url": "/static/musicas/MAR - pumapjl (youtube).mp3",
        "imageUrl": "/static/assets/mar.png"
    }, 
    {
        "id": 16,
        "title": "Ai calica",
        "artist": "Pumapjl, LEALL",
        "url": "/static/musicas/AI CALICA feat. LEALL - pumapjl (youtube).mp3",
        "imageUrl": "/static/assets/mar.png"
    }, 
    {
        "id": 17,
        "title": "Please Please Please",
        "artist": "Sabrina Carpenter",
        "url": "/static/musicas/Please Please Please - Sabrina Carpenter (youtube).mp3",
        "imageUrl": "/static/assets/sabrina-ca.png"
    },
    {
        "id": 18,
        "title": "Naquela Mesa",
        "artist": "Nelson Gonçalves",
        "url": "/static/musicas/Nelson Gonçalves - Naquela Mesa (Pseudo Video) (Pseudo Video) - NelsonGoncalvesVEVO (youtube).mp3",
        "imageUrl": "/static/assets/naquela-mesa.png"
    },
    {
        "id": 19,
        "title": "Preciso Me Encontrar",
        "artist": "Cartola",
        "url": "/static/musicas/Preciso Me Encontrar - Cartola (youtube).mp3",
        "imageUrl": "/static/assets/cartola.png"
    },
    {
        "id": 20,
        "title": "Construção",
        "artist": "Chico Buarque",
        "url": "/static/musicas/Construção.mp3",
        "imageUrl": "/static/assets/construcao.png"
    },
]


@app.route('/api/destaques')
def destaques():
    musicas_selecionadas = [MUSICAS_DB[1], MUSICAS_DB[3], MUSICAS_DB[4], MUSICAS_DB[5]] 
    
    return jsonify(musicas_selecionadas)


@app.route('/api/saude')
def saude():
    return jsonify({"status": "ok", "count": len(MUSICAS_DB)})

@app.route('/api/musicas')
def musicas():
    return jsonify(MUSICAS_DB)


if __name__ ==  '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
 