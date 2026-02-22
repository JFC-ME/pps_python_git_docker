from database import consultar_frases, inicializar_db, insertar_frases

inicializar_db()

def frotar(n_frases: int = 1) -> list():
	return consultar_frases(n_frases)

def anyadir_frases_nuevas(frases: list):
	insertar_frases(frases)
