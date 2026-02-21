# --- Fase 1: Resolución de dependencias ---
FROM python:3.12-slim AS builder

WORKDIR /app

# Evitamos que Python genere ficheros .pyc y use buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalamos dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Fase 2: Ejecución ---
FROM builder AS runtime

# Copiamos el código de la aplicación y las frases
COPY app.py bayeta.py frases.txt .

# Exponemos el puerto de Flask
EXPOSE 5000

# Ejecutamos la aplicación
CMD ["python3", "app.py"]
