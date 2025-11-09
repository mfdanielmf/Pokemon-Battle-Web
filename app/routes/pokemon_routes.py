from flask import Blueprint, abort, redirect, render_template, request, url_for

from app.services import pokemon_service
from app.services.current_year_service import get_current_year
from app.forms.pokemon_select_form import PokemonSelectForm

current_year = get_current_year()
pokemon_bp = Blueprint('pokemon', __name__)


@pokemon_bp.route("/", methods=["GET", "POST"])
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
            # Para que no se quede el valor introducido en el input
            form.pokemon.data = ""
            return render_template("lista_pokemon.html", pokemons=pokemon_service.listar_pokemon(), entrenador=entrenador, form=form, year=current_year)

        if not entrenador:
            return redirect(url_for("home.formulario"))

        # Si pasamos las validaciones anteriores, vamos a la batalla
        return redirect(url_for("battle.battle",
                                pokemon_elegido=pokemon_elegido.name,
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


@pokemon_bp.route("/<int:id>")
def pokemon_detalles(id):
    pokemon = pokemon_service.obtener_pokemon_por_id(id)
    if pokemon is None:
        abort(404)
    return render_template("pokemon_detallado.html", pokemon_recibir=pokemon, year=current_year)
