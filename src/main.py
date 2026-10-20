from src.templates.controllers import create_trainee, get_all_trainees,get_trainee_by_id, update_trainee, delete_trainee

from src.models.models import TraineeModel, TraineeUpdateModel
from fastapi import FastAPI, HTTPException, status

#uvicorn src.main:app --reload
app = FastAPI(title = "Gestion de bases de datos de los aprendices", description = "API simple con FastAPI para consumir los datos de los aprendices", version = "1.0.0",)

#Mensaje de bienvenida
@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de aprendices"}

#Registrar aprendices
@app.post(
    "/trainees/",response_description = "Registrar un nuevo aprendiz",
    status_code = status.HTTP_201_CREATED,
    )
def create_trainee_api(trainee: TraineeModel):
    #Validar si ya existe el documento
    return create_trainee(trainee)

#obtener la lista de aprendices
@app.get(
    "/trainees/", response_description = "Listar todos los aprendices"
)

def get_all_trainees_appi():
    return get_all_trainees()

#obtener un aprendiz por ID
@app.get(
    "/trainees/{id}", response_description = "Obtener un aprendiz por ID"
)
def get_trainee_by_id_api(id: str):
    trainee = get_trainee_by_id(id)
    if not trainee:
        raise HTTPException(status_code = 404, detail = "Aprendiz no encontrado")
    return trainee

#Actualizar aprendiz
@app.put(
    "/trainees/{id}", response_description = "Actualizar un aprendiz"
)

def update_trainee_api(id: str, trainee: TraineeUpdateModel):
    trainee = update_trainee(id, trainee)
    if not trainee:
        raise HTTPException(status_code = 404, detail = "Aprendiz no encontrado")
    return trainee

#Eliminar aprendiz
@app.delete(
    "/trainees/{id}", response_description = "Eliminar un aprendiz"
)

def delete_trainee_api(id: str):
    trainee = delete_trainee(id)
    if not trainee:
        raise HTTPException(status_code = 404, detail = "Aprendiz no encontrado")
    return {"message": "Aprendiz eliminado correctamente"}
