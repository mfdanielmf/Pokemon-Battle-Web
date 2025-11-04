from datetime import datetime
from flask import Flask, render_template, jsonify, current_app, request
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

@app.route("/battle")
def battle():
    lista_pokemons = current_app.config["DATA"]
    pokemon = None
    for p in lista_pokemons:
        if p["id"] == 6:
            pokemon = p
            
    moves = []
    while len(moves) < 4:
        movimiento_random = random.choice(pokemon["moves"])
        if movimiento_random not in moves:
            moves.append(movimiento_random)
            
    pokemon_random = random.choice(lista_pokemons)
    
    
    return render_template("battle.html", year=current_year, pokemon_elegido=pokemon, moves_elegido=moves, pokemon_rival=pokemon_random)

if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=True)
