from flask import Flask, jsonify, request
from rutas import rutas

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def home():
    return "<h1>Viajar en coche eléctrico BLABLABLA.</h1><p>Esta API nos permite obtener posibles rutas para viajar en coche eléctrico.</p>"

@app.route('/api/v1/resources/rutas/all', methods=['GET'])
def get_all():
    return jsonify(rutas)

@app.route('/api/v1/resources/rutas/<id>', methods=['GET'])
def valor_id(id):
    for diccionario in rutas:
        if str(diccionario['id']) == id:
            return jsonify(diccionario)
    return "El elemento no existe"

if __name__ == '__main__':
    app.run(debug=True)

#La api corre en Heroku: https://electriccars.herokuapp.com/api/v1/resources/rutas/all