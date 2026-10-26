from pymongo import  MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

#Agregar la URI de conexion a tu base de MOngoDB
MONGO_URL = "mongodb+srv://isabellazambranomartinez_db_user:<db_password>@cluster0.7quvkxo.mongodb.net/"

#Crear una instancia del cliente de MongoDB y asignar un tiempo de espera para la seleccion de servidor 
client = client = MongoClient(MONGO_URL, ServerSelectionTimeoutMS = 3000)

#Crear la base de datos y la coleccion
db = client.data_ap
collection = db.trainee

try: 
    #Intentar obtener informacion del servidor para verificar la conexion
    client.server_info()
    client.admin.command("ping")
    print("Conexion exitosa a MongoDB")
except(ConnectionFailure, ServerSelectionTimeoutError) as e:
    print("Error al conectar a MongoDB: {e}")
    