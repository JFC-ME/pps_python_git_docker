from pymongo import MongoClient
import os

def get_db():
	host = os.getenv('MONGO_HOST', 'localhost')
	client = MongoClient(f'mongodb://{host}:27017/')
	db = client['bayeta_db']
	return db['frases']

def inicializar_db():
	coleccion = get_db()
	if coleccion.count_documents({}) == 0:
		with open('frases.txt', 'r', encoding='utf-8') as f:
			frases = [{"texto": line.strip()} for line in f if line.strip()]
		if frases:
			coleccion.insert_many(frases)
			print(f"Base de datos inicializada con {len(frases)} frases.")

def consultar_frases(n_frases=1):
	coleccion = get_db()
	pipeline = [{"$sample": {"size": n_frases}}]
	cursor = coleccion.aggregate(pipeline)
	return [doc['texto'] for doc in cursor]
