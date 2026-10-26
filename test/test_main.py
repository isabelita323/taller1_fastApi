from pymongo import MongoClient
from pymongo .errors import ConnectionFailure, ServerSelectionTimeoutError

#Agregar la URI de conexion a tu base de MOngoDB
MONGO_URL = "mongodb+srv://lunaguasmejia_db_user:ERM2RlMt4pGsvQuY@cluster0.h4elust.mongodb.net/?appName=Cluster0"

#Crear una instancia del cliente de MongoDB y asignar un tiempo de espera para la seleccion de servidor 
client = MongoClient(MONGO_URL, ServerSelectionTimeoutMS = 3000)
#Crear la base de datos y la coleccion
db = client.ambiente703
collection = db.mesa

#Crear el modelo de datos para la coleccion
nueva_mesa = {
    "name": "Luna Aguas",
    "status": "Alive",
    "species": "Human",
    "gender": "Male"
}
#Insertar el modelo de datos en la coleccion
collection.insert_one(nueva_mesa)
print("Documento insertado en la coleccion 'mesa' de la base de datos 'ambiente703'")

try: 
    #Intentar obtener informacion del servidor para verificar la conexion
    client.server_info()
    client.admin.command("ping")
    print("Conexion exitosa a MongoDB")
except(ConnectionFailure, ServerSelectionTimeoutError) as e:
    print("Error al conectar a MongoDB: {e}")

finally:
    #Cerrar la conexion al cliente de MongoDB
    client.close()