from sqlalchemy import Column, Integer, String
from app.database.db import db
from werkzeug.security import generate_password_hash, check_password_hash


class Entrenador(db.Model):
    __tablename__ = "entrenador"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    contraseña = Column(String, nullable=False)

    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = generate_password_hash(password=contraseña)

    def check_Password(self, contraseña):
        return check_password_hash(self.contraseña, contraseña)
