from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

class Libro(BaseModel):
    titulo: str
    autor: str
    isbn: str
    prestado: Optional[bool] = False

class Miembro(BaseModel):
    nombre: str
    libros_prestados: List[str] = []

# Listas para almacenar libros y miembros (simulando una base de datos)
libros_db: List[Libro] = []
miembros_db: List[Miembro] = []

# Rutas

@app.post("/agregar-libro/")
def agregar_libro(libro: Libro):
    # Verificar si el libro ya existe
    for l in libros_db:
        if l.isbn == libro.isbn:
            raise HTTPException(status_code=400, detail="El libro con ese ISBN ya existe.")
    
    libros_db.append(libro)
    return {"message": f"Libro '{libro.titulo}' agregado a la biblioteca."}

@app.post("/agregar-miembro/")
def agregar_miembro(miembro: Miembro):
    # Verificar si el miembro ya existe
    for m in miembros_db:
        if m.nombre == miembro.nombre:
            raise HTTPException(status_code=400, detail="El miembro ya está registrado.")
    
    miembros_db.append(miembro)
    return {"message": f"Miembro '{miembro.nombre}' agregado."}

@app.get("/mostrar-libros-disponibles/")
def mostrar_libros_disponibles():
    libros_disponibles = [libro for libro in libros_db if not libro.prestado]
    if not libros_disponibles:
        return {"message": "No hay libros disponibles en este momento."}
    return libros_disponibles

@app.post("/prestar-libro/")
def prestar_libro(titulo: str, miembro_nombre: str):
    # Buscar el libro
    libro = next((libro for libro in libros_db if libro.titulo == titulo), None)
    if libro is None:
        raise HTTPException(status_code=404, detail="El libro no se encontró.")
    if libro.prestado:
        raise HTTPException(status_code=400, detail="El libro ya está prestado.")
    
    # Buscar el miembro
    miembro = next((miembro for miembro in miembros_db if miembro.nombre == miembro_nombre), None)
    if miembro is None:
        raise HTTPException(status_code=404, detail="El miembro no se encontró.")
    
    # Prestar el libro
    libro.prestado = True
    miembro.libros_prestados.append(libro.titulo)
    
    return {"message": f"Libro '{libro.titulo}' prestado a {miembro.nombre}."}

@app.post("/devolver-libro/")
def devolver_libro(titulo: str, miembro_nombre: str):
    # Buscar el libro
    libro = next((libro for libro in libros_db if libro.titulo == titulo), None)
    if libro is None:
        raise HTTPException(status_code=404, detail="El libro no se encontró.")
    if not libro.prestado:
        raise HTTPException(status_code=400, detail="El libro no estaba prestado.")
    
    # Buscar el miembro
    miembro = next((miembro for miembro in miembros_db if miembro.nombre == miembro_nombre), None)
    if miembro is None:
        raise HTTPException(status_code=404, detail="El miembro no se encontró.")
    if titulo not in miembro.libros_prestados:
        raise HTTPException(status_code=400, detail="El miembro no tenía este libro prestado.")
    
    # Devolver el libro
    libro.prestado = False
    miembro.libros_prestados.remove(libro.titulo)
    
    return {"message": f"Libro '{libro.titulo}' devuelto por {miembro.nombre}."}

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8123)

