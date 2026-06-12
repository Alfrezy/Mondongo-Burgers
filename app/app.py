import os
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Kubernetes inyectará estos valores automáticamente
DB_HOST = os.environ.get("DB_HOST", "mondongo-base-service")
DB_NAME = os.environ.get("DB_NAME", "mondongo_db")
DB_USER = os.environ.get("DB_USER", "Osiris_God")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "12345")

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port="5432"
    )

@app.route('/')
def home():
    return jsonify({"mensaje": "¡Bienvenidos a Mondongo Burgers API en Kubernetes!"})

if __name__ == '__main__':
    # Para que Docker pueda exponer el puerto
    app.run(host='0.0.0.0', port=5000)