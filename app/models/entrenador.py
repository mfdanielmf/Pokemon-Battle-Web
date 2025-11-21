from sqlalchemy import Column, Integer, String
from app.database import db

class Entidad(db.Model):
    __tablename__ = "entrenador"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    contraseña = Column(String(100))