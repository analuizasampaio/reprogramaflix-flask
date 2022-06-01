import json
from flask import Flask, request, jsonify, Response
from flask_cors import CORS 
import sqlite3
import jsons
import controller
from dbConfig import create_tables

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

    
@app.route("/")
def hello():
    integrantes = [
        {"Nome": "Ana Luiza Sampaio",
         "RA": "2101183"},
        {"Nome": "Guilherme Portes Bebiano ",
         "RA": "2101494"},
        {"Nome": "Ingrid Priscila Alves de Sousa",
         "RA": "2101204"},
        {"Nome": "Charles Eduardo Felipe de Souza",
         "RA":  "2100038"},
        {"Nome": "Vitor Augusto Silva",
         "RA": "2100534"},
        {"Nome": "Kauê Ribeiro Varjão",
         "RA": "1904284"},
    ]
    
    result = {"mensagem": f'API de filmes para a materia de APIs e microsserviços',
                                "grupo": integrantes}
    
    return Response(json.dumps(result), status=200, mimetype='application/json')

@app.route("/filmes", methods=["GET"])
def get_filmes():
    filmes = controller.get_all_filmes()
    return jsonify(filmes)


@app.route("/filmes/<id>", methods=["GET"])
def get_filme_by_id(id):
    filmes = controller.get_filme_by_id(id)
    return jsonify(filmes)

@app.route("/filmes/search", methods=["GET"])
def get_filme_by_titulo():
    titulo = request.args.get('q')
    filmes = controller.get_filme_by_titulo(titulo)
    return jsonify(filmes)

@app.route("/filmes/cadastrar", methods=["POST"])
def insert_filme():
    body = request.get_json()
    filmes = controller.insert_filme(body)
    return jsonify(filmes)

@app.route("/filmes/<id>/curtir", methods=["PUT"])
def curtir(id):
    filmes = controller.curtir(id)
    return jsonify(filmes)

@app.route("/filmes/<id>/curtir", methods=["DELETE"])
def descurtir(id):
    filmes = controller.descurtir(id)
    return jsonify(filmes)

if __name__ == "__main__":
    create_tables()
    app.run(port = 5000)