from flask import Blueprint, jsonify, render_template

from app.services.pokemon_service import listar_pokemon
from app.services.current_year_service import get_current_year
# from app.forms.trainer_form import TrainerForm

home_bp = Blueprint('home', __name__)

year = get_current_year()


@home_bp.route("/")
def index():
    return render_template("index.html", year=year)


@home_bp.route("/data")
def data():
    pokemons = listar_pokemon()
    # Pasamos los datos a diccionario, porque no podemos serializar a json objetos en python
    return jsonify([p.to_dict() for p in pokemons])


@home_bp.route("/formulario")
def formulario():
    # form = TrainerForm()
    # if form.validate_on_submit():
    #     entrenador = form.entrenador.data
    return render_template("formulario.html", year=year)

    # return render_template("formulario.html", form=form)
