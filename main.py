from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from typing import List
from pydantic import BaseModel
from database import Modulo, Curso, create_modulo_table, create_curso_table, insert_modulo, insert_curso, \
    get_all_modulos, get_all_cursos, update_modulo, update_curso, delete_modulo, delete_curso, close_connection

app = FastAPI()
create_modulo_table()
create_curso_table()
app.title = "Cursos API"
app.version = "0.0.1"


class Modulo(BaseModel):
    id: int
    nombre: str
    duracion: int
    nivel: str

class Curso(BaseModel):
    id: int
    titulo: str
    descripcion: str
    precio: float
    duracion: int

@app.get('/modulos', response_model=List[Modulo], tags=['Modulos'])
def get_modulos():
    modulos = get_all_modulos()
    return modulos

@app.post('/modulos', response_model=Modulo, tags=['Modulos'])
def create_modulo(modulo: Modulo):
    insert_modulo(modulo)
    return modulo

@app.get('/cursos', response_model=List[Curso], tags=['Cursos'])
def get_cursos():
    cursos = get_all_cursos()
    return cursos

@app.post('/cursos', response_model=Curso, tags=['Cursos'])
def create_curso(curso: Curso):
    insert_curso(curso)
    return curso

@app.on_event("shutdown")
def shutdown_event():
    close_connection()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)