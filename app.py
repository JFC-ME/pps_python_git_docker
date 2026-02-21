from flask import Flask, jsonify
from bayeta import frotar

app = Flask(__name__)

@app.route('/')
def hola_mundo():
	return "<h1>Hola, mundo</h1><p>Esta es la Bayeta de la fortuna</p>"

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def get_frotar(n_frases):
	resultado = frotar(n_frases)
	return jsonify({"frases": resultado})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)

