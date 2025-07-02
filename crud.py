from models import Chamado
from sqlalchemy.orm import Session

def criar_chamado(db: Session, local_subestacao: str, nome_tecnico: str, acao_tomada: str, gravidade: str):
    chamado = Chamado(local_subestacao=local_subestacao, nome_tecnico=nome_tecnico, acao_tomada=acao_tomada, gravidade=gravidade)
    db.add(chamado)
    db.commit()
    db.refresh(chamado)
    return chamado

def listar_chamados(db: Session):
    return db.query(Chamado).all()

def obter_chamado_por_id(db: Session, chamado_id: int):
    return db.query(Chamado).filter(Chamado.id == chamado_id).first()

def depuracao_chamados(db: Session):
    return db.query(Chamado).count(), db.query(Chamado).all()