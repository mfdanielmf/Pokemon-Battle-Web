from flask import Blueprint, abort, current_app, render_template, request
from datetime import datetime
from app.services import pokemon_service

current_year = datetime.now().year
pokemon_bp = Blueprint('pokemon', __name__, template_folder= 'templates')

@pokemon_bp.route("/lista_pokemon/", methods=["POST", "GET"])
def lista():
    if request.method == "POST":
        entrenador = request.form.get("entrenador")
    else:
        entrenador = None

    # Si no mandamos entrenador, cargamos la lista y pasamos entrenador como None
    if (entrenador is None):
        return render_template("lista_pokemon.html", pokemons=pokemon_service.listar_pokemon(), year=current_year, entrenador=None)

    # Validamos longitud del nombre y que no tenga espacios ni caracteres especiales
    if len(entrenador) < 3 or len(entrenador) > 15 or not entrenador.isalpha():
        return "El nombre debe de tener entre 3 y 15 letras sin espacios ni caracteres especiales", 400

    return render_template("lista_pokemon.html", pokemons=pokemon_service.listar_pokemon(), year=current_year, entrenador=entrenador )


@pokemon_bp.route("/pokemon_detallado/<int:id>")
def pokemon_detalles(id):
    # DATA para pasar la lista de pokemon y recorrerla para buscar el pokemon
    lista_pokemons = current_app.config["DATA"]
    pokemon = pokemon_service.obtener_pokemon_por_id(id)
    if pokemon is None:
        abort(404)
    return render_template("pokemon_detallado.html", pokemon_recibir=pokemon)