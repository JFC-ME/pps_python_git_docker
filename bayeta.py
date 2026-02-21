import random

def frotar(n_frases: int = 1) -> list():
	try:
		with open('frases.txt', 'r', encoding='utf-8') as f:
			frases = [line.strip() for line in f if line.strip()]

		if not frases:
			return ["La bayeta está seca... (archivo vacío"]

		return random.choices(frases, k=n_frases)
	except FileNotFoundError:
		return ["Error: No se encontró a la fuente de sabiduría (frases.txt)"]
