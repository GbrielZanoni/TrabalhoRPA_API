from fastapi import FastAPI, File, Form, UploadFile, Depends
from sqlalchemy.orm import Session
from crud import criar_registro, listar_registros
from database import SessionLocal, engine
from models import Base
import shutil

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/enviar/")
async def enviar_dados(
    nome: str = Form(...),
    observacao: str = Form(...),
    imagem: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    img_bytes = await imagem.read()
    return criar_registro(db, nome, observacao, img_bytes)

@app.get("/registros/")
def listar(db: Session = Depends(get_db)):
    return listar_registros(db)
