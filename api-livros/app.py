from flask import Flask, jsonify

app = Flask(__name__)

livros = [
    {
        "id": 1,
        "titulo": "Jogos Vorazes",
        "autor": "Suzanne Collins",
        "ano": 2008
    },
    {
        "id": 2,
        "titulo": "A Seleção",
        "autor": "Kiera Cass",
        "ano": 2012
    },
    {
        "id": 3,
        "titulo": "Tartarugas até lá embaixo",
        "autor": "John Green",
        "ano": 2017
    }
]

@app.route('/livros', methods=['GET'])
def obter_livros():
    """Rota GET /livros que retorna os livros cadastrados em formato JSON."""
    return jsonify({"livros": livros})

if __name__ == '__main__':
    app.run(debug=True)
