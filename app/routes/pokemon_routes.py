from flask import Blueprint, abort, redirect, render_template, request, session, url_for

from app.services import pokemon_service
from app.services.current_year_service import get_current_year
from app.forms.pokemon_select_form import PokemonSelectForm


current_year = get_current_year()
pokemon_bp = Blueprint('pokemon', __name__)


@pokemon_bp.route("/", methods=["GET", "POST"])
def lista():

    # ADAPTAR POST (CUANDO ESTAMOS POR EJEMPLO EN LA PÁGINA 2 E INTRODUCIMOS EL NOMBRE DE USUARIO, QUE VUELVA A LA PÁGINA EN LA QUE ESTABA)

    form = PokemonSelectForm()

    # POST (formulario seleccionar)
    if form.validate_on_submit():
        entrenador = session.get("entrenador")
        pokemon_name = form.pokemon.data

        pokemon_elegido = pokemon_service.obtener_pokemon_por_nombre_cliente(
            pokemon_name)

        if pokemon_elegido is None:
            form.pokemon.errors.append(
                f"El pokemon '{pokemon_name}' no existe. Elige uno válido")
            # Para que no se quede el valor introducido en el input
            form.pokemon.data = ""
            return render_template("lista_pokemon.html", pokemons=pokemon_service.obtener_pokemon_adaptado(), form=form, year=current_year)

        session["pokemon_elegido"] = pokemon_name

        if not entrenador:
            return redirect(url_for("home.login"))

        # Si pasamos las validaciones anteriores, vamos a la batalla
        return redirect(url_for("battle.battle"))

    # GET (cargamos la lista directamente o venimos de elegir entrenador)
    page = request.args.get("pagina")

    if not page:
        page = 1
    else:
        page = int(page)

    return render_template("lista_pokemon.html", pokemons=pokemon_service.obtener_pokemon_adaptado2(page), year=current_year, form=form)


@pokemon_bp.route("/<int:id>")
def pokemon_detalles(id):
    pokemon = pokemon_service.obtener_pokemon_por_id_client(id)
    if pokemon is None:
        abort(404)
    return render_template("pokemon_detallado.html", pokemon_recibir=pokemon, year=current_year)
