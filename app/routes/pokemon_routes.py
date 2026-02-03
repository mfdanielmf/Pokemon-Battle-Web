from flask import Blueprint, abort, redirect, render_template, request, session, url_for

from app.services import pokemon_service
from app.services.current_year_service import get_current_year
from app.forms.pokemon_select_form import PokemonSelectForm
from app.models.exceptions import NoHayDataException


current_year = get_current_year()
pokemon_bp = Blueprint('pokemon', __name__)


@pokemon_bp.route("/", methods=["GET", "POST"])
def lista():
    page = request.args.get("pagina")

    try:
        if not page or int(page) < 1:
            page = 1
        else:
            page = int(page)
    except Exception:
        page = 1

    form = PokemonSelectForm()

    # POST (formulario seleccionar)
    if form.validate_on_submit():
        entrenador = session.get("entrenador")
        pokemon_name = form.pokemon.data

        try:
            pokemon_service.obtener_pokemon_por_nombre_cliente(
                pokemon_name)
        except NoHayDataException:
            form.pokemon.errors.append(
                f"El pokemon '{pokemon_name}' no existe. Elige uno válido")
            # Para que no se quede el valor introducido en el input
            form.pokemon.data = ""

            data = pokemon_service.obtener_pokemon_adaptado2(page)

            return render_template("lista_pokemon.html", pokemons=data["pokemons_adaptados"], form=form, year=current_year, pagina_actual=data["pagina"])

        session["pokemon_elegido"] = pokemon_name

        if not entrenador:
            return redirect(url_for("home.login"))

        # Si pasamos las validaciones anteriores, vamos a la batalla
        return redirect(url_for("battle.battle"))

    # GET (cargamos la lista directamente o venimos de elegir entrenador)
    data = pokemon_service.obtener_pokemon_adaptado2(page)

    return render_template("lista_pokemon.html", pokemons=data["pokemons_adaptados"], year=current_year, form=form, pagina_actual=data["pagina"], previous=data["previous"], next=data["next"])


@pokemon_bp.route("/<int:id>")
def pokemon_detalles(id):
    try:
        pokemon = pokemon_service.obtener_pokemon_por_id_client(id)
    except NoHayDataException:
        abort(404)

    return render_template("pokemon_detallado.html", pokemon_recibir=pokemon, year=current_year)
