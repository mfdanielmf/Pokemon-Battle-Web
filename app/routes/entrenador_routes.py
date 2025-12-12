from flask import Blueprint, redirect, render_template

from app.models.exceptions import EntrenadorNotFoundException, JugadorSinBatallasException
from app.services.battle_service import obtener_todas_batallas_id_entrenador
from app.services.current_year_service import get_current_year


entrenador_bp = Blueprint("entrenador", __name__)


@entrenador_bp.route("/historial-batallas/<int:id_entrenador>")
def historial_batallas(id_entrenador):
    try:
        batallas = obtener_todas_batallas_id_entrenador(id_entrenador)
    except EntrenadorNotFoundException or JugadorSinBatallasException:
        return redirect("pokemon.lista")

    return render_template("historial_batallas.html", batallas=batallas, year=get_current_year())
