from datetime import datetime
from flask import Flask, redirect, render_template, jsonify, current_app, request, url_for
import random

from app.routes.battle_routes import battle_bp
from app.routes.pokemon_routes import pokemon_bp
from app.routes.home_routes import home_bp


# current_year = datetime.now().year

app = Flask(__name__, static_folder="static")

app.register_blueprint(home_bp, url_prefix="/")
app.register_blueprint(pokemon_bp, url_prefix="/pokemons")
app.register_blueprint(battle_bp, url_prefix="/battle")


# @app.route("/data")
# def home():
#     return jsonify(current_app.config["DATA"])


# @app.route("/pokemon_detallado/<int:id>")
# def pokemon_detalles(id):
#     # DATA para pasar la lista de pokemon y recorrerla para buscar el pokemon
#     lista_pokemons = current_app.config["DATA"]
#     pokemon = None
#     for p in lista_pokemons:
#         if p["id"] == id:
#             pokemon = p

#     return render_template("pokemon_detallado.html", pokemon_recibir=pokemon, year=current_year)


# @app.route("/formulario")
# def formulario():
#     return render_template("formulario.html", year=current_year)


if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=True)
