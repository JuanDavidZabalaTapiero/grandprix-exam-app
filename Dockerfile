# Descargar imagen de Python
FROM python:3.12-slim

# Insalar dependencias del sistema operativo requeridas para mysqlclient
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev pkg-config && rm -rf /var/lib/apt/lists/*

# Directorio creado por Docker
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "run.py"]