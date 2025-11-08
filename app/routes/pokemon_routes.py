import random
from flask import Blueprint, abort, redirect, render_template, request, url_for

from app.services import pokemon_service
from app.services.current_year_service import get_current_year
from app.forms.pokemon_select_form import PokemonSelectForm
from app.services.pokemon_service import listar_pokemon

current_year = get_current_year()
pokemon_bp = Blueprint('pokemon', __name__)
lista_pokemons = listar_pokemon()


@pokemon_bp.route("/lista_pokemon/", methods=["GET", "POST"])
def lista():
    form = PokemonSelectForm()

    # POST (formulario seleccionar)
    if form.validate_on_submit():
        entrenador = form.entrenador.data
        pokemon_name = form.pokemon.data

        pokemon_elegido = pokemon_service.pokemon_existe(pokemon_name)

        if pokemon_elegido is None:
            form.pokemon.errors.append(
                f"El pokemon '{pokemon_name}' no existe. Elige uno válido")
            return render_template("lista_pokemon.html", pokemons=pokemon_service.listar_pokemon(), entrenador=entrenador, form=form, year=current_year)

        if not entrenador:
            return redirect(url_for("home.formulario"))

        # Si pasamos las validaciones anteriores, vamos a la batalla
        moves_elegido = random.sample(
            pokemon_elegido.moves, min(4, len(pokemon_elegido.moves)))

        pokemon_rival = random.choice(lista_pokemons)

        return redirect(url_for("battle.battle",
                                pokemon_elegido=pokemon_elegido,
                                moves_elegido=moves_elegido,
                                pokemon_rival=pokemon_rival,
                                entrenador=entrenador
                                )
                        )

    # GET (cargamos la lista directamente o venimos de elegir entrenador)
    entrenador = request.args.get("entrenador", None)

    # Si no mandamos entrenador, cargamos la lista y pasamos entrenador como None
    if (entrenador is None):
        return render_template("lista_pokemon.html", pokemons=pokemon_service.listar_pokemon(), year=current_year, entrenador=None, form=form)

    # Con esto le ponemos de value a un campo oculto el nombre de entrenador para pasárselo a la batalla
    form.entrenador.data = entrenador
    return render_template("lista_pokemon.html", pokemons=pokemon_service.listar_pokemon(), year=current_year, entrenador=entrenador, form=form)


@pokemon_bp.route("/pokemon_detallado/<int:id>")
def pokemon_detalles(id):
    pokemon = pokemon_service.obtener_pokemon_por_id(id)
    if pokemon is None:
        abort(404)
    return render_template("pokemon_detallado.html", pokemon_recibir=pokemon, year=current_year)
