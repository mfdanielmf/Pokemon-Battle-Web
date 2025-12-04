from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from app.database.db import db
from sqlalchemy.orm import relationship


class Battle_db(db.Model):
    __tablename__ = "battles"

    id = Column(Integer, primary_key=True, autoincrement=True)

    entrenador_atacante = Column(Integer, nullable=False)
    entrenador_defensor = Column(Integer, nullable=False)
    pokemon_atacante = Column(Integer, nullable=False)
    pokemon_defensor = Column(Integer, nullable=False)
    creada_en = Column(DateTime, default= datetime.now, nullable=False)
    resultado = Column(String, nullable=False)
    log = Column(String, nullable=False )
    entrenador = relationship("Entrenador", secondary= "participar", back_populates="battles", passive_deletes=True)

    def __init__(self, entrenador_atacante, entrenador_defensor, pokemon_atacante, pokemon_defensor, resultado, log):
        self.entrenador_atacante = entrenador_atacante
        self.entrenador_defensor = entrenador_defensor
        self.pokemon_atacante = pokemon_atacante
        self.pokemon_defensor = pokemon_defensor
        self.resultado = resultado
        self.log = log