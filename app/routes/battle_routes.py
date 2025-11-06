import random
from flask import Blueprint, redirect, render_template, request, url_for

from app.services.pokemon_service import listar_pokemon, pokemon_existe
from app.services.current_year_service import get_current_year

current_year = get_current_year()
battle_bp = Blueprint('battle', __name__)


@battle_bp.route("/", methods=["GET", "POST"])
def battle():
    lista_pokemons = listar_pokemon()

    # POST
    if request.method == "POST":
        pokemon_name = request.form.get("pokemon", "").strip().lower()
        entrenador = request.form.get("entrenador")

        # Buscamos si el pokemon existe
        pokemon_elegido = pokemon_existe(pokemon_name)

        # Si el pokemon no existe
        if not pokemon_elegido:
            return render_template(
                "lista_pokemon.html",
                pokemons=lista_pokemons,
                year=current_year,
                mensaje_error="No has introducido un pokemon válido"
            )

        if not entrenador:
            return redirect(url_for("home.formulario"))

        pokemon_rival = random.choice(lista_pokemons)
        moves_elegido = random.sample(
            pokemon_elegido.moves, min(4, len(pokemon_elegido.moves)))

        # Redirigir al GET de /battle con los datos
        return redirect(url_for(
            "battle.battle",
            year=current_year,
            pokemon_name=pokemon_name,
            entrenador=entrenador
        ))

    # GET
    if request.method == "GET":
        pokemon_name = request.args.get("pokemon_name")
        year = request.args.get("year", current_year)
        entrenador = request.args.get("entrenador")

        # Si no recibimos un nombre de pokemon
        if not pokemon_name:
            return redirect(url_for("pokemon.lista"))

        pokemon_elegido = pokemon_existe(pokemon_name)

        if not pokemon_elegido:
            return redirect(url_for("pokemon.lista"))

        moves_elegido = random.sample(
            pokemon_elegido.moves, min(4, len(pokemon_elegido.moves)))

        pokemon_rival = random.choice(lista_pokemons)

        return render_template(
            "battle.html",
            year=year,
            pokemon_elegido=pokemon_elegido,
            moves_elegido=moves_elegido,
            pokemon_rival=pokemon_rival,
            entrenador=entrenador
        )
