from app.database.db import db
from app.models.battle_db import Battle_db
from app.models.entrenador import Entrenador


def crear_batalla(batalla: Battle_db) -> Battle_db:
    db.session.add(batalla)
    db.session.commit()

    return batalla


def obtener_batalla_por_id(id):
    battle = db.session.get(Battle_db, id)

    return battle


def obtener_batallas_por_entrenador(id_entrenador) -> list[Battle_db] | None:
    entrenador = db.session.get(Entrenador, id_entrenador)

    if not entrenador:
        return None

    return entrenador.battles


def eliminar_batalla(id):
    batalla_eliminar = Battle_db.query.get(id)
    if (batalla_eliminar):
        db.session.delete(batalla_eliminar)
        db.session.commit()

        return True
    return False
