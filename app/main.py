import sqlite3
from flask import Flask
from flask_session import Session

from app.routes.battle_routes import battle_bp
from app.routes.pokemon_routes import pokemon_bp
from app.routes.home_routes import home_bp
from app.database.db import db

app = Flask(__name__, static_folder="static")

app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_FILE_DIR"] = "./.flask_session"
app.secret_key = "no se me ocurre que poner"

# Inicializar flask-session
Session(app)

# SQLAlchemy config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data/pokemons.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(home_bp, url_prefix="/")
app.register_blueprint(pokemon_bp, url_prefix="/pokemons")
app.register_blueprint(battle_bp, url_prefix="/battle")


if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=True)
