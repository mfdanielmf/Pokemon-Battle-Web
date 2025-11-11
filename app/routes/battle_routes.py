from flask import Blueprint, redirect, render_template, request, session, url_for

from app.services.pokemon_service import pokemon_existe
from app.services.current_year_service import get_current_year
from app.services.battle_service import random_moves, random_pokemon, get_stat_value
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

    battle.log.append("test")

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

    if pokemon:
        ataque_name = request.form.get("ataque_name")
        battle_object = session.get("battle")

        damage = None
        accuracy = None

        for ataque in pokemon.moves:
            if ataque["name"] == ataque_name:
                damage = ataque["power"]
                accuracy = ataque["accuracy"]

                battle_object["vida_rival"] -= damage * 0.20

                if battle_object["vida_rival"] <= 0:
                    session.pop("battle")
                    session.pop("pokemon_elegido")
                    return "Has ganado"

                if battle_object["vida_jugador"] <= 0:
                    session.pop("battle")
                    session.pop("pokemon_elegido")
                    return "Has perdido"

                session["battle"] = battle_object

                return render_template("battle.html", year=current_year)

         # TODO: implementar lógica finalizar batalla (cuando uno muera, limpiar session y volver a lista de pokemon) - FALTA PENSAR A DONDE LLEVAR EL USUARIO Y QUE HACER AL ACABAR LA BATALLA
         # TODO: hacer que se decida random que pokemon empieza a atacar
         # TODO: hacer que al lanzar un ataque el rival también responda con un ataque aleatorio
         # TODO: hacer que los ataques puedan fallar segundo el valor de precisión
         # TODO: añadir logs al atacar y eso

    return "Test"
