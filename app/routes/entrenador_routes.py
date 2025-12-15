from flask import Blueprint, redirect, render_template, session, url_for

from app.models.exceptions import EntrenadorNotFoundException, JugadorSinBatallasException
from app.services.battle_service import obtener_todas_batallas_id_entrenador
from app.services.current_year_service import get_current_year


entrenador_bp = Blueprint("entrenador", __name__)


@entrenador_bp.route("/historial-batallas")
def historial_batallas():
    id_entrenador = session.get("entrenador_id")

    try:
        batallas = obtener_todas_batallas_id_entrenador(id_entrenador)
    except EntrenadorNotFoundException or JugadorSinBatallasException:
        return redirect(url_for("home.index"))

    return render_template("historial_batallas.html", batallas=batallas, year=get_current_year())
