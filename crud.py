from models import Registro
from sqlalchemy.orm import Session

def criar_registro(db: Session, nome: str, observacao: str, imagem: bytes):
    registro = Registro(nome=nome, observacao=observacao, imagem=imagem)
    db.add(registro)
    db.commit()
    db.refresh(registro)
    return registro

def listar_registros(db: Session):
    return db.query(Registro).all()
