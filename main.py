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
    db: Session = Depends(get_db)
):
    return criar_chamado(db, local_subestacao, nome_tecnico, acao_tomada, gravidade)

@app.get("/chamados/")
def listar_chamados_view(db: Session = Depends(get_db)):
    return listar_chamados(db)

@app.get("/chamado/{chamado_id}")
def obter_chamado(chamado_id: int, db: Session = Depends(get_db)):
    return obter_chamado_por_id(db, chamado_id)

@app.get("/depuracao/")
def depuracao(db: Session = Depends(get_db)):
    total, chamados = depuracao_chamados(db)
    return {"total_chamados": total, "chamados": chamados}