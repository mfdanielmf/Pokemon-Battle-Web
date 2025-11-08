from flask import Blueprint, abort, render_template, request

from app.services import pokemon_service
from app.services.current_year_service import get_current_year

current_year = get_current_year()
pokemon_bp = Blueprint('pokemon', __name__)


@pokemon_bp.route("/lista_pokemon/", methods=["GET"])
def lista():
    entrenador = request.args.get("entrenador", None)

    # Si no mandamos entrenador, cargamos la lista y pasamos entrenador como None
    if (entrenador is None):
        return render_template("lista_pokemon.html", pokemons=pokemon_service.listar_pokemon(), year=current_year, entrenador=None)

    return render_template("lista_pokemon.html", pokemons=pokemon_service.listar_pokemon(), year=current_year, entrenador=entrenador)


@pokemon_bp.route("/pokemon_detallado/<int:id>")
def pokemon_detalles(id):
    pokemon = pokemon_service.obtener_pokemon_por_id(id)
    if pokemon is None:
        abort(404)
    return render_template("pokemon_detallado.html", pokemon_recibir=pokemon, year=current_year)
