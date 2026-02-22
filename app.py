from flask import Flask, jsonify, request
from bayeta import frotar, anyadir_frases_nuevas

app = Flask(__name__)

@app.route('/')
def hola_mundo():
	return "<h1>Hola, mundo</h1><p>Esta es la Bayeta de la fortuna</p>"

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def get_frotar(n_frases):
	resultado = frotar(n_frases)
	return jsonify({"frases": resultado})

@app.route('/frotar/add', methods=['POST'])
def post_frotar():
	datos = request.get_json()
	nuevas_frases = datos.get('frases', [])

	if not nuevas_frases:
		return jsonify({"error": "No se enviaron frases"}), 400

	anyadir_frases_nuevas(nuevas_frases)
	return jsonify({"mensaje": "Frases añadidas correctamente"}), 200

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)

