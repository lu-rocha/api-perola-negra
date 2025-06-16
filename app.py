from flask import Flask, jsonify, request
from tripulantes import personagens

app = Flask(__name__)

@app.route('/personagens', methods=['GET'])
def obter_todos_tripulantes():
    return jsonify(personagens) 

@app.route('/personagens/<int:id>', methods=['GET'])
def obter_por_id(id):
    for personagem in personagens:
        if personagem.get('id') == id:
            return jsonify(personagem) 

@app.route('/personagens', methods=['POST'])       
def adicionar_personagem():
    novo_personagem = request.get_json()
    personagens.append(novo_personagem)
    return jsonify(personagens) 

@app.route('/personagens/<int:id>', methods=['PUT'])
def editar_personagem_por_id(id):
    personagem_alterado = request.get_json()
    for indice, personagem in enumerate(personagens):
        if personagem.get('id') == id:
                personagens[indice].update(personagem_alterado)
                return jsonify(personagens[indice]) 
        
@app.route('/personagens/<int:id>', methods=['DELETE'])       
def deletar_personagem_por_id(id):
     for indice,personagem in enumerate(personagens):
            if personagem.get('id') == id:
                 del personagens[indice]
                 return jsonify(personagens) 
        


app.run(port=5000, host='0.0.0.0', debug=True)
