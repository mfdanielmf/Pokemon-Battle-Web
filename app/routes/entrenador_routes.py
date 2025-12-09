from flask import Blueprint, jsonify

from app.repositories.battle_repo import obtener_batallas_por_entrenador


entrenador_bp = Blueprint("entrenador", __name__)


@entrenador_bp.route("/historial-batallas/<int:id_entrenador>")
def historial_batallas(id_entrenador):
    batallas = obtener_batallas_por_entrenador(id_entrenador)

    # TEST TODO ESTO
    print(batallas)

    return jsonify(batallas)
