from flask import Flask

from app.routes.battle_routes import battle_bp
from app.routes.pokemon_routes import pokemon_bp
from app.routes.home_routes import home_bp

app = Flask(__name__, static_folder="static")

app.secret_key = "no se me ocurre que poner"

app.register_blueprint(home_bp, url_prefix="/")
app.register_blueprint(pokemon_bp, url_prefix="/pokemons")
app.register_blueprint(battle_bp, url_prefix="/battle")


# @app.route("/formulario")
# def formulario():
#     return render_template("formulario.html", year=current_year)


if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=True)
