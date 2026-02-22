# pps_python_git_docker
Esta va a ser una aplicación Python del estilo "galleta de la fortuna" o "servilleta de
bar"

### Como ejecutar la aplicación

Para garantizar que la aplicación funcione, por favor, sigue los siguientes pasos:

### 1. Preparar el entorno virtual
Se recomienda usar el entorno virtual de Python:
- **Windows:** `python -m venv .venv` y activarlo con `.venv\Scripts\Activate.ps1`
- **Mac/Linux:** `python -m venv .venv` y activarlo con `source .venv/bin/activate`

### 2. Instalar dependencias
Una vez activado el entorno, instala las librerías necesarias con el siguiente comando:
```bash
pip install -r requirements.txt
```

### 3. Comprobación
Para comprobar que la aplicación funciona ejecuta:
`python3 app.py`

### NOTA:
Asegúrate de tener un fichero `frases.txt` con frases separadas por un salto de línea

### Despliegue en Docker
Si tienes Docker instalado, puedes ejecutar la aplicación sin configurar Python localmente:

1. **Construir una imagen:** `docker build -t bayeta-app .`
2. **Ejecutar el contenedor:** `docker run -p 5000:5000 bayeta-app`

### MongoDB
Ahora se necesita un contenedor MongoDB corriendo en la misma red.

### Docker-Compose
Para levantar todo el entorno (aplicación + base de datos) solo necesitas ejecutar:
```bash
docker compose up --build
```

### POST
Realizando una petición POST al endpoint `/frotar/add` se pueden agregar frases a la base de datos de nuestra aplicación web.
