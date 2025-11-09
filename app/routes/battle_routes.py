from flask import Blueprint, redirect, render_template, request, url_for

from app.services.pokemon_service import pokemon_existe
from app.services.current_year_service import get_current_year
from app.services.battle_service import random_moves, random_pokemon

current_year = get_current_year()
battle_bp = Blueprint('battle', __name__)


@battle_bp.route("/")
def battle():
    pokemon_name = request.args.get("pokemon_elegido", None)
    entrenador = request.args.get("entrenador", None)

    # Si intenta acceder directamente por la url sin haber elegido pokemon o entrenador, lo redirigimos
    if not pokemon_name or not entrenador:
        return redirect(url_for("pokemon.lista"))

    # Obtenemos el pokemon
    pokemon_elegido = pokemon_existe(pokemon_name)

    # Si pone en la url un pokemon que no existe devolvemos a lista
    if pokemon_elegido is None:
        return redirect(url_for("pokemon.lista"))

    # Obtenemos rival y movimientos aleatorios
    pokemon_rival = random_pokemon()
    moves_elegido = random_moves(pokemon_elegido)

    return render_template("battle.html", year=current_year, pokemon_elegido=pokemon_elegido, moves_elegido=moves_elegido, pokemon_rival=pokemon_rival, entrenador=entrenador)
