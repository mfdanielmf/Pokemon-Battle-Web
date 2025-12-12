from app.models.entrenador import Entrenador
from app.database.db import db


def crear_entrenador(nombre, contraseña):
    entrenador_nuevo = Entrenador(nombre, contraseña)

    db.session.add(entrenador_nuevo)
    db.session.commit()

    return entrenador_nuevo


def obtener_entrenador_por_nombre(nombre) -> Entrenador | None:
    entrenador = Entrenador.query.filter_by(nombre=nombre).first()

    return entrenador


def obtener_todos_los_entrenadores():
    entrenadores = Entrenador.query.all()

    return entrenadores


def check_pass(entrenador: Entrenador, contraseña) -> bool:
    return entrenador.check_Password(contraseña)


def obtener_entrenador_por_id(id) -> Entrenador | None:
    entrenador = db.session.get(Entrenador, id)

    return entrenador
