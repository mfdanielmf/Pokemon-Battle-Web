from datetime import datetime
from flask import Flask, redirect, render_template, jsonify, current_app, request, url_for
import json
import random

current_year = datetime.now().year

app = Flask(__name__, static_folder="static")

with open("data/pokemon.json", encoding="utf-8") as f:
    app.config["DATA"] = json.load(f)


@app.route("/data")
def home():
    return jsonify(current_app.config["DATA"])


@app.route("/")
def index():
    return render_template("index.html", year=current_year)


@app.route("/lista_pokemon/", methods=["POST", "GET"])
def lista():
    if request.method == "POST":
        entrenador = request.form.get("entrenador")
    else:
        entrenador = None

    # Si no mandamos entrenador, cargamos la lista y pasamos entrenador como None
    if (entrenador is None):
        return render_template("lista_pokemon.html", pokemons=current_app.config["DATA"], year=current_year, entrenador=None)

    # Validamos longitud del nombre y que no tenga espacios ni caracteres especiales
    if len(entrenador) < 3 or len(entrenador) > 15 or not entrenador.isalpha():
        return "El nombre debe de tener entre 3 y 15 letras sin espacios ni caracteres especiales", 400

    return render_template("lista_pokemon.html", pokemons=current_app.config["DATA"], year=current_year, entrenador=entrenador)


@app.route("/pokemon_detallado/<int:id>")
def pokemon_detalles(id):
    # DATA para pasar la lista de pokemon y recorrerla para buscar el pokemon
    lista_pokemons = current_app.config["DATA"]
    pokemon = None
    for p in lista_pokemons:
        if p["id"] == id:
            pokemon = p

    return render_template("pokemon_detallado.html", pokemon_recibir=pokemon, year=current_year)


@app.route("/formulario")
def formulario():
    return render_template("formulario.html", year=current_year)


@app.route("/battle", methods=["POST", "GET"])
def battle():
    lista_pokemons = current_app.config["DATA"]

    # POST
    if request.method == "POST":
        pokemon_name = request.form.get("pokemon", "").strip().lower()
        entrenador = request.form.get("entrenador")

        # Buscamos si el pokemon existe
        pokemon_elegido = None
        for p in lista_pokemons:
            if p["name"].lower() == pokemon_name:
                pokemon_elegido = p
                break

        # Si el pokemon no existe
        if not pokemon_elegido:
            return render_template(
                "lista_pokemon.html",
                pokemons=lista_pokemons,
                year=current_year,
                mensaje_error="No has introducido un pokemon válido"
            )

        if not entrenador:
            return redirect(url_for("formulario"))

        pokemon_rival = random.choice(lista_pokemons)
        moves_elegido = random.sample(
            pokemon_elegido["moves"], min(4, len(pokemon_elegido["moves"])))

        # Redirigir al GET de /battle con los datos
        return redirect(url_for(
            "battle",
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
            return redirect(url_for("lista"))

        pokemon_elegido = None
        for p in lista_pokemons:
            if p["name"].lower() == pokemon_name:
                pokemon_elegido = p
                break

        if not pokemon_elegido:
            return redirect(url_for("lista"))

        moves_elegido = random.sample(
            pokemon_elegido["moves"], min(4, len(pokemon_elegido["moves"])))

        pokemon_rival = random.choice(lista_pokemons)

        return render_template(
            "battle.html",
            year=year,
            pokemon_elegido=pokemon_elegido,
            moves_elegido=moves_elegido,
            pokemon_rival=pokemon_rival,
            entrenador=entrenador
        )


if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=True)
