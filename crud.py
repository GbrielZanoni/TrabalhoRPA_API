from models import Chamado
from sqlalchemy.orm import Session
from email_service import enviar_alerta_email

def criar_chamado(db: Session, local_subestacao: str, nome_tecnico: str, acao_tomada: str, gravidade: str, situacao_subestacao: str):
    chamado = Chamado(
        local_subestacao=local_subestacao,
        nome_tecnico=nome_tecnico,
        acao_tomada=acao_tomada,
        gravidade=gravidade,
        situacao_subestacao=situacao_subestacao  
    )
    db.add(chamado)
    db.commit()
    db.refresh(chamado)

    if gravidade in ["Crítica", "Urgente"]:  
        alertas = [{
            "id": chamado.id,
            "local": chamado.local_subestacao,
            "tecnico": chamado.nome_tecnico,
            "situacao": chamado.situacao_subestacao,
            "gravidade": chamado.gravidade,
            "acao": chamado.acao_tomada,
            "data_criacao": chamado.data_hora.strftime('%d/%m/%Y %H:%M'), 
            "motivo": f"Gravidade {chamado.gravidade}" 
        }]
        enviar_alerta_email(alertas)

    return chamado

def listar_chamados(db: Session):
    return db.query(Chamado).all()

def obter_chamado_por_id(db: Session, chamado_id: int):
    return db.query(Chamado).filter(Chamado.id == chamado_id).first()

def depuracao_chamados(db: Session):
    return db.query(Chamado).count(), db.query(Chamado).all()

def remover_todos_chamados(db: Session):
    db.query(Chamado).delete()
    db.commit()

def remover_chamado_por_id(db: Session, chamado_id: int):
    chamado = db.query(Chamado).filter(Chamado.id == chamado_id).first()
    if chamado:
        db.delete(chamado)
        db.commit()

def validar_chamado(db: Session, chamado_id: int, validar: bool):
    chamado = db.query(Chamado).filter(Chamado.id == chamado_id).first()
    if chamado:
        chamado.validacao = validar
        db.commit()
        db.refresh(chamado)
    return chamado
