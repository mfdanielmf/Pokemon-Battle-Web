from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Text
from app.database.db import db
from sqlalchemy.orm import relationship


class Battle_db(db.Model):
    __tablename__ = "battles"

    id = Column(Integer, primary_key=True, autoincrement=True)

    pokemon_atacante = Column(String, nullable=False)
    pokemon_defensor = Column(String, nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.now, nullable=False)
    id_ganador = Column(String, nullable=False)

    entrenadores = relationship("Entrenador", secondary="participar",
                                back_populates="battles", passive_deletes=True)

    def __init__(self, pokemon_atacante, pokemon_defensor, id_ganador, log):
        self.pokemon_atacante = pokemon_atacante
        self.pokemon_defensor = pokemon_defensor
        self.id_ganador = id_ganador
