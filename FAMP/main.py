from imp import reload
from fastapi import FastAPI, HTTPException, status
from models import Curso
from typing import Optional, List

app = FastAPI()


# @app.get('/')
# async def raiz():
#     return {"msg": "FastAPI Curso"}

cursos = {
    1: {
        "titulo": "Programação",
        "aulas": 112,
        "horas": 58
    },
    2: {
        "titulo": "Algoritimos",
        "aulas": 48,
        "horas": 12
    }
}


@app.get("/cursos")
async def get_curso():
    return cursos


@app.get("/cursos/{id}")
async def get_curso(id: int):
    try:
        curso = cursos[id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")


@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    return curso


@app.put("/cursos/{id}")
async def put_curso(id: int, curso: Curso):
    if id in cursos:
        cursos[id] = curso
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Não existe um curso com o id:{id} informado!")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000,
                log_level="info", reload=True)
