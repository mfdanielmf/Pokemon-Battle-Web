from flask import Blueprint, redirect, render_template, request, session, url_for

from app.services.pokemon_service import obtener_pokemon_por_nombre
from app.services.current_year_service import get_current_year
from app.services.battle_service import random_atacar, atacar_turno, inicializar_batalla, elegir_rival_aleatorio, insertar_batalla_base
from app.models.exceptions import BatallaIncompletaException, NoHayEntrenadoresException

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
    pokemon_elegido = obtener_pokemon_por_nombre(pokemon_name)

    # Por si a pesar de validar en lista consiguen llegar aquí
    if not pokemon_elegido:
        return redirect(url_for("pokemon.lista"))

    # Si no hay pokemon rival, lo generamos
    if not session.get("entrenador_rival"):
        try:
            pokemon_rival = elegir_rival_aleatorio(entrenador)

            session["entrenador_rival"] = pokemon_rival.nombre
        except NoHayEntrenadoresException:
            return redirect(url_for("pokemon.lista"))

    # Creamos una nueva batalla si no lo habíamos hecho
    if not session.get("battle"):
        battle = inicializar_batalla(pokemon_elegido)
        session["battle"] = battle.__dict__

    return render_template("battle.html", year=current_year)


@battle_bp.route("/ataque", methods=["GET", "POST"])
def atacar():
    # GET (venimos directamente por la url)
    if request.method == "GET":
        return redirect(url_for("battle.battle"))

    # POST (seleccionamos ataque en battle)
    # Obtenemos el pokemon para acceder a sus ataques
    pokemon_name = session.get("pokemon_elegido")
    pokemon = obtener_pokemon_por_nombre(pokemon_name)

    if not pokemon:
        return redirect(url_for("pokemon.lista"))

    ataque_name = request.form.get("ataque_name")
    battle_object = session.get("battle")

    for ataque in pokemon.moves:
        if ataque["name"] == ataque_name:
            # TURNO JUGADOR
            acabar_batalla, battle_object_service = atacar_turno(damage=ataque["power"],
                                                                 accuracy=ataque["accuracy"],
                                                                 battle_object=battle_object,
                                                                 pokemon_name=pokemon_name,
                                                                 ataque_name=ataque_name,
                                                                 # para controlar si el personaje que ataca es el jugador en el service
                                                                 atacante_jugador=True)

            session["battle"] = battle_object_service

            # Si el pokemon tiene 0 de vida, acabamos
            if acabar_batalla:
                try:
                    batalla_sesion = session.get("battle")

                    pokemon_jugador = batalla_sesion["datos_pokemon_jugador"].name
                    pokemon_rival = batalla_sesion["datos_pokemon_rival"].name
                    id_ganador = session.get("entrenador_id")

                except BatallaIncompletaException:
                    return redirect("pokemon.lista")

                return redirect(url_for("battle.resultado"))

            # TURNO RIVAL
            ataque_rival = random_atacar(
                battle_object.get("ataques_rival"))

            acabar_batalla, battle_object_service = atacar_turno(damage=ataque_rival["power"],
                                                                 accuracy=ataque_rival["accuracy"],
                                                                 battle_object=battle_object,
                                                                 pokemon_name=pokemon_name,
                                                                 ataque_name=ataque_rival["name"],
                                                                 atacante_jugador=False)

            session["battle"] = battle_object_service

            # Si el pokemon tiene 0 de vida, acabamos
            if acabar_batalla:
                try:
                    batalla_sesion = session.get("battle")

                    pokemon_jugador = batalla_sesion["datos_pokemon_jugador"].name
                    pokemon_rival = batalla_sesion["datos_pokemon_rival"].name

                    # batalla = insertar_batalla_base()

                except BatallaIncompletaException:
                    return redirect("pokemon.lista")

                return redirect(url_for("battle.resultado"))

            return redirect(url_for("battle.battle"))

    return redirect(url_for("pokemon.lista"))


@battle_bp.route("/resultado")
def resultado():
    # Obtenemos los datos antes de quitarlos de la sesión
    battle_object = session.get("battle")
    pokemon_name = session.get("pokemon_elegido")

    if not battle_object or not pokemon_name:
        return redirect(url_for("pokemon.lista"))

    session.pop("battle")
    session.pop("pokemon_elegido")
    session.pop("entrenador_rival")

    return render_template("resultado.html", year=current_year, battle=battle_object)
