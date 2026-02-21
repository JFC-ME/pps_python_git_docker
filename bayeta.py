from database import consultar_frases, inicializar_db

inicializar_db()

def frotar(n_frases: int = 1) -> list():
	return consultar_frases(n_frases)
