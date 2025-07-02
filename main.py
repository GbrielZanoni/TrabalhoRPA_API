from fastapi import FastAPI, Form, Depends
from sqlalchemy.orm import Session
from crud import criar_chamado, listar_chamados, obter_chamado_por_id, depuracao_chamados, remover_todos_chamados, remover_chamado_por_id, validar_chamado
from database import SessionLocal, engine
from models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/chamado/")
async def enviar_chamado(
    local_subestacao: str = Form(...),
    nome_tecnico: str = Form(...),
    acao_tomada: str = Form(...),
    gravidade: str = Form(...),
    situacao_subestacao: str = Form(...),  
    db: Session = Depends(get_db)
):
    return criar_chamado(
        db, local_subestacao, nome_tecnico, acao_tomada, gravidade, situacao_subestacao
    )

@app.get("/chamados/")
async def obter_chamados(db: Session = Depends(get_db)):
    return listar_chamados(db)

@app.get("/chamado/{chamado_id}")
async def obter_chamado(chamado_id: int, db: Session = Depends(get_db)):
    return obter_chamado_por_id(db, chamado_id)

@app.delete("/chamados/")
async def deletar_todos_chamados(db: Session = Depends(get_db)):
    remover_todos_chamados(db)
    return {"message": "Todos os chamados foram removidos"}

@app.delete("/chamado/{chamado_id}")
async def deletar_chamado(chamado_id: int, db: Session = Depends(get_db)):
    remover_chamado_por_id(db, chamado_id)
    return {"message": f"Chamado {chamado_id} foi removido"}

@app.put("/chamado/{chamado_id}/validar")
async def validar_chamado_api(chamado_id: int, validar: bool, db: Session = Depends(get_db)):
    chamado = validar_chamado(db, chamado_id, validar)
    return {"message": f"Chamado {chamado_id} {'validado' if validar else 'desvalidado'}"}
