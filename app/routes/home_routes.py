from flask import Blueprint, jsonify, redirect, render_template, session, url_for

from app.models.exceptions import EntrenadorExistenteException, EntrenadorNoCreadoException, EntrenadorNotFoundException, ContraseñaIncorrectaException
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
        id_antigua = session.get("entrenador_id")

        try:
            entrenador_existe = autenticar_entrenador(entrenador, contraseña)
        except ContraseñaIncorrectaException:
            form.form_errors.append("Contraseña incorrecta")

            return render_template("formulario_login.html", form=form, year=year)

        except EntrenadorNotFoundException:
            form.form_errors.append("Credenciales incorrectas")

            return render_template("formulario_login.html", form=form, year=year)

        # Si inicia sesión en la misma cuenta, no reiniciamos la batalla ni nada
        if id_antigua == entrenador_existe.id:
            return redirect(url_for("pokemon.lista"))

        session["entrenador"] = entrenador_existe.nombre
        session["entrenador_id"] = entrenador_existe.id

        pokemon = session.get("pokemon_elegido")

        if session.get("battle"):
            session.pop("pokemon_elegido")
            session.pop("battle")

        # Si elegimos otro usuario reiniciamos el rival
        if session.get("entrenador_rival"):
            session.pop("entrenador_rival")

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
        try:
            entrenador_creado = registrar_entrenador(entrenador, contraseña)

        except EntrenadorNoCreadoException:
            form.form_errors.append("Error al insertar los datos")

            return render_template("formulario_register.html", year=year, form=form)

        except EntrenadorExistenteException:
            form.form_errors.append(f"El usuario {entrenador} ya existe")

            return render_template("formulario_register.html", year=year, form=form)

        session["entrenador"] = entrenador_creado.nombre
        session["entrenador_id"] = entrenador_creado.id

        # Si teníamos una batalla en curso y nos registramos, eliminamos la batalla y el pokemon que había elegido
        if session.get("battle"):
            session.pop("battle")
            session.pop("pokemon_elegido")

        if session.get("entrenador_rival"):
            session.pop("entrenador_rival")

        # Si venimos de la lista y elegimos pokemon, lo llevmaos a la batalla directamente
        if session.get("pokemon_elegido"):
            return redirect(url_for("battle.battle"))

        return redirect(url_for("pokemon.lista"))

    # GET
    return render_template("formulario_register.html", year=year, form=form)


@home_bp.route("/logout")
def logout():
    if session.get("entrenador"):
        session.clear()

    return redirect(url_for("home.index"))
