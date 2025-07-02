from fastapi import FastAPI, Form, Depends
from sqlalchemy.orm import Session
from crud import criar_chamado, listar_chamados, obter_chamado_por_id, depuracao_chamados
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
