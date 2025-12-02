import datetime
from sqlalchemy import Column, DateTime, Integer, String
from app.database import db
from sqlalchemy.orm import relationship


class Battle_db(db.Model):
    __tablename__ = "battles"

    id = Column(Integer, primary_key=True)

    entrenador_atacante = Column(Integer, nullable=False)
    entrenador_defensor = Column(Integer, nullable=False)
    pokemon_atacante = Column(Integer, nullable=False)
    pokemon_defensor = Column(Integer, nullable=False)
    creada_en = Column(DateTime, default= datetime.now(), nullable=False)
    resultado = Column(String, nullable=False)
    entrenador = relationship("Entrenador", back_populates="battles")

    