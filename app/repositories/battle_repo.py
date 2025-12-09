from app.database.db import db
from app.models.battle_db import Battle_db
from app.models.entrenador import Entrenador


def crear_batalla(entrenador_atacante, entrenador_defensor, pokemon_atacante, pokemon_defensor, resultado, log):
    battle_nueva = Battle_db(entrenador_atacante=entrenador_atacante, entrenador_defensor=entrenador_defensor,
                             pokemon_atacante=pokemon_atacante, pokemon_defensor=pokemon_defensor, resultado=resultado, log=log)

    db.session.add(battle_nueva)
    db.session.commit()

    return battle_nueva


def obtener_batalla_por_id(id):
    battle = db.session.get(Battle_db, id)

    return battle


def obtener_batallas_por_entrenador(id_entrenador):
    entrenador = Battle_db.query.filter_by(id=id_entrenador)

    return entrenador


def eliminar_batalla(id):
    batalla_eliminar = Battle_db.query.get(id)
    if (batalla_eliminar):
        db.session.delete(batalla_eliminar)
        db.session.commit()

        return True
    return False
