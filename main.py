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
    if filmes == [] :
            return Response(f'Não foi encontrado filmes', status=404, mimetype='application/json')
    else:

        return Response(json.dumps(filmes), status=201, mimetype='application/json')


@app.route("/filmes/<id>", methods=["GET"])
def get_filme_by_id(id):
    filmes = controller.get_filme_by_id(id)
    if filmes == {} :
            return Response(f'Não foi encontrado filmes', status=404, mimetype='application/json')
    else:

        return Response(json.dumps(filmes), status=201, mimetype='application/json')


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

@app.route("/user/cadastrar", methods=["POST"])
def insert_user():
    body = request.get_json()
    user = controller.insert_user(body)
    if user == None:
        return Response(f'não foi possivel cadastrar usuario', status=500, mimetype='application/json')
    else:
        result = {"mensagem": f'Usuário {user["nome"]} criado com sucesso',
                             "data": user}
        return Response(json.dumps(result), status=201, mimetype='application/json')

@app.route("/user/all", methods=["GET"])
def get_all_users():
    users = controller.get_all_users()
    if users == None:
        return Response(f'Não foi encontrados usuário', status=404, mimetype='application/json')
    else:

        return Response(json.dumps(users), status=201, mimetype='application/json')


@app.route("/user/<id>", methods=["GET"])
def get_user_by_id(id):
    users = controller.get_user_by_id(id)
    if users == {} or users == None:
            return Response(f'Não existe usuário id {id}', status=404, mimetype='application/json')
    else:

        return Response(json.dumps(users), status=201, mimetype='application/json')

@app.route("/user/login", methods=["POST"])
def login():
    body = request.get_json()
    user = controller.login(body)
    return jsonify(user)

@app.route("/user/<id>/logout", methods=["PUT"])
def logout(id):
    user = controller.logout(id)
    return jsonify(user)

@app.route("/user/<id>/filmes", methods=["GET"])
def get_filmes_user(id):
    filmes = controller.get_filmes_user(id)
    return jsonify(filmes)

@app.route("/user/<user_id>/filmes/favorite", methods=["PUT"])
def favorite(user_id):
    filme_id = request.get_json()
    filmes = controller.favorite(filme_id, user_id)
    return jsonify(filmes)

@app.route("/user/<user_id>/filmes/unfavorite", methods=["PUT"])
def unfavorite(user_id):
    filme_id = request.get_json()
    filmes = controller.unfavorite(filme_id, user_id)
    return jsonify(filmes)

@app.route('/reset', methods=["POST"])
def reset():
    controller.reset_database()
    
@app.route('/filmes/<id>', methods=["DELETE"])
def delete_filme(id):
    controller.delete_filme(id)

if __name__ == "__main__":
    create_tables()
    app.run(port = 5000)