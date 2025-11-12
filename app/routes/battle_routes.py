from flask import Blueprint, redirect, render_template, request, session, url_for

from app.services.pokemon_service import pokemon_existe
from app.services.current_year_service import get_current_year
from app.services.battle_service import random_moves, random_pokemon, get_stat_value, random_atacar, atacar_jugador, atacar_rival
from app.models.battle import Battle

current_year = get_current_year()
battle_bp = Blueprint('battle', __name__)


@battle_bp.route("/")
def battle():
    pokemon_name = session.get("pokemon_elegido")
    entrenador = session.get("entrenador")

    # Si intenta acceder directamente por la url sin haber elegido pokemon o entrenador, lo redirigimos
    if not pokemon_name or not entrenador:
        return redirect(url_for("pokemon.lista"))

    # Obtenemos el pokemon
    pokemon_elegido = pokemon_existe(pokemon_name)

    # Por si a pesar de validar en lista consiguen llegar aquí
    if not pokemon_elegido:
        return redirect(url_for("pokemon.lista"))

    # Obtenemos rival y movimientos aleatorios
    pokemon_rival = random_pokemon()
    moves_elegido = random_moves(pokemon_elegido)
    moves_rival = random_moves(pokemon_rival)

    battle = Battle(
        datos_pokemon_jugador=pokemon_elegido,
        datos_pokemon_rival=pokemon_rival,
        vida_jugador=get_stat_value(pokemon_elegido, "hp"),
        vida_rival=get_stat_value(pokemon_rival, "hp"),
        ataques_jugador=moves_elegido,
        ataques_rival=moves_rival
    )

    session["battle"] = battle.__dict__

    return render_template("battle.html", year=current_year)


@battle_bp.route("/ataque", methods=["GET", "POST"])
def atacar():
    # GET (venimos directamente por la url)
    if request.method == "GET":
        return redirect(url_for("pokemon.lista"))

    # POST (seleccionamos ataque en battle)
    # Obtenemos el pokemon para acceder a sus ataques
    pokemon_name = session.get("pokemon_elegido")
    pokemon = pokemon_existe(pokemon_name)

    if not pokemon:
        return redirect(url_for("pokemon.lista"))

    ataque_name = request.form.get("ataque_name")
    battle_object = session.get("battle")

    for ataque in pokemon.moves:
        if ataque["name"] == ataque_name:
            # TURNO JUGADOR
            acabar_batalla = atacar_jugador(damage=ataque["power"],
                                            accuracy=ataque["accuracy"],
                                            battle_object=battle_object,
                                            pokemon_name=pokemon_name,
                                            ataque_name=ataque_name)

            # Si el pokemon tiene 0 de vida, acabamos
            if acabar_batalla:
                return redirect(url_for("battle.resultado"))

            # TURNO RIVAL
            ataque_rival = random_atacar(
                battle_object.get("ataques_rival"))

            acabar_batalla = atacar_rival(damage=ataque_rival["power"],
                                          accuracy=ataque_rival["accuracy"],
                                          battle_object=battle_object,
                                          pokemon_name=pokemon_name,
                                          ataque_name=ataque_rival["name"])

            # Si el pokemon tiene 0 de vida, acabamos
            if acabar_batalla:
                return redirect(url_for("battle.resultado"))

            return render_template("battle.html", year=current_year)

    return redirect(url_for("pokemon.lista"))


@battle_bp.route("/resultado")
def resultado():
    # Obtenemos los datos antes de quitarlos de la sesión
    battle_object = session.get("battle")
    pokemon_name = session.get("pokemon_elegido")

    if not battle_object or not pokemon_name:
        return redirect(url_for("pokemon.lista"))

    session.pop("battle")
    session.pop("pokemon_elegido")

    return render_template("resultado.html", year=current_year, battle=battle_object)

# TODO: acabar pestaña de resultado de logs
