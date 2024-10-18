from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

def encontrar_indices_numeros(nums: List[int], objetivo: int):
    mapa = {}
    for i, num in enumerate(nums):
        diferencia = objetivo - num
        if diferencia in mapa:
            return [mapa[diferencia], i]
        mapa[num] = i
    raise HTTPException(status_code=400, detail="No se encontraron dos números que sumen el objetivo")

@app.get("/")
def get_fastapi():
    return 200

@app.post("/encontrar-indices/")
def obtener_indices_numeros(nums: List[int], objetivo: int):
    try:
        indices = encontrar_indices_numeros(nums, objetivo)
        return {"indices": indices}
    except HTTPException as e:
        raise e

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8123)
