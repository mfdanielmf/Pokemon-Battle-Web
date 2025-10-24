from datetime import datetime
from flask import Flask, render_template, jsonify, current_app, request
import json

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
    # Si tenemos nombre de entrenador
    if request.method == "get":
        entrenador = request.args.get("entrenador")
        if len(entrenador) < 3 or len(entrenador) > 15:  # entrenador = NONE ahora mismo
            return "El nombre debe de tener entre 3 y 15 caracteres", 400
        return render_template("lista_pokemon.html", pokemons=current_app.config["DATA"], year=current_year)
    else:
        return render_template("lista_pokemon.html", pokemons=current_app.config["DATA"], year=current_year)


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


if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=True)
