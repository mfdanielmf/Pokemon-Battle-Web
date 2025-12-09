from flask import Blueprint, jsonify

from app.repositories.entrenador_repo import obtener_batallas_entrenador


entrenador_bp = Blueprint("entrenador", __name__)


@entrenador_bp.route("/historial-batallas/<int:id_entrenador>")
def historial_batallas(id_entrenador):
    batallas = obtener_batallas_entrenador(id_entrenador)

    print(batallas)

    return jsonify(batallas)
