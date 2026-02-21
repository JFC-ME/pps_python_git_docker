from bayeta import frotar

print("--- Probando la bayeta de la fortuna ---")
predicciones = frotar(3)
for i, p in enumerate(predicciones, 1):
	print(f"{i}. {p}")
