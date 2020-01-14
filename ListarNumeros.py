from Conexao import ConectaSQL
from flask import Flask, request, jsonify

app = Flask(__name__)
conexao = ConectaSQL()


@app.route('/')
def inicio():
    return '######### Números por extenso #########'

@app.route('/<int:id>', methods=['GET'])
def consultar(id):
    aux = []
    aux.append(conexao.consulta(id))

    return jsonify(aux)
