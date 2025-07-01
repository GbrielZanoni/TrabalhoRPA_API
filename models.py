from sqlalchemy import Column, Integer, String, LargeBinary
from database import Base

class Registro(Base):
    __tablename__ = "registros"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    observacao = Column(String)
    imagem = Column(LargeBinary)
