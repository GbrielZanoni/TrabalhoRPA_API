from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class Chamado(Base):
    __tablename__ = "chamados"
    id = Column(Integer, primary_key=True, index=True)
    data_hora = Column(DateTime, default=func.now())
    local_subestacao = Column(String)
    nome_tecnico = Column(String)
    acao_tomada = Column(String)
    gravidade = Column(String)
    situacao_subestacao = Column(String)