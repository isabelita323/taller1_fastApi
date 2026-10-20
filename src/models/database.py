import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

# Permite configurar la conexión por variable de entorno y usa una base local por defecto.
MONGO_URL =  os.getenv("MONGO_URL", "mongodb://localhost:27017")

client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=3000)
db = client.get_database("data_ap")
collection = db.trainee

try:
    client.admin.command("ping")
    print("Conexion exitosa a MongoDB")
except (ConnectionFailure, ServerSelectionTimeoutError) as e:
    print(f"Advertencia: no se pudo conectar a MongoDB: {e}")
    print("Asegurate de tener MongoDB corriendo o configurar MONGO_URL")
