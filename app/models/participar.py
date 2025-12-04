from sqlalchemy import Column, ForeignKey, Integer
from app.database.db import db


class Participar(db.Model):
    __tablename__ = "participar"
    entrenador_id = Column(Integer, ForeignKey("entrenador.id", ondelete="RESTRICT"), primary_key=True)
    battle_id = Column(Integer, ForeignKey("battles.id", ondelete="RESTRICT"), primary_key=True)