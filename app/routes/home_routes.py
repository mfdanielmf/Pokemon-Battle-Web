from flask import Blueprint, jsonify, redirect, render_template, session, url_for

from app.services.pokemon_service import listar_pokemon
from app.services.current_year_service import get_current_year
from app.forms.trainer_login_form import TrainerLoginForm
from app.forms.trainer_register_form import TrainerRegisterForm
from app.services.entrenador_service import autenticar_entrenador, registrar_entrenador

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


@home_bp.route("/login", methods=["GET", "POST"])
def login():
    form = TrainerLoginForm()

    # POST (venimos de introducir entrenador)
    if form.validate_on_submit():
        entrenador = form.entrenador.data
        contraseña = form.contraseña.data

        entrenador_existe = autenticar_entrenador(entrenador, contraseña)

        if not entrenador_existe:
            return "error"
        else:
            return "test"

        session["entrenador"] = entrenador
        pokemon = session.get("pokemon_elegido")

        if session.get("battle"):
            session.pop("pokemon_elegido")
            session.pop("battle")
        if entrenador and pokemon:
            return redirect(url_for("battle.battle"))

        return redirect(url_for("pokemon.lista"))

    # GET
    return render_template("formulario_login.html", year=year, form=form)


@home_bp.route("/register", methods=["GET", "POST"])
def register():
    form = TrainerRegisterForm()

    # POST (venimos de introducir entrenador)
    if form.validate_on_submit():
        entrenador = form.entrenador.data
        contraseña = form.contraseña.data

        # Devuelve el entreandor si lo ha creado bien
        entrenador_creado = registrar_entrenador(entrenador, contraseña)

        if not entrenador:
            return redirect(url_for("register"), form=form)

        session.clear()

        session["entrenador"] = entrenador_creado.nombre
        session["entrenador_id"] = entrenador_creado.id

        return redirect(url_for("pokemon.lista"))

    # GET
    return render_template("formulario_register.html", year=year, form=form)


@home_bp.route("/logout")
def logout():
    if session.get("entrenador"):
        session.clear()

    return redirect(url_for("home.index"))
