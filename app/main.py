import os
from flask import Flask
from flask_session import Session

from app.routes.battle_routes import battle_bp
from app.routes.pokemon_routes import pokemon_bp
from app.routes.home_routes import home_bp
from app.routes.entrenador_routes import entrenador_bp
from app.database.db import db

from app.models.entrenador import Entrenador
from app.models.battle_db import Battle_db
from app.models.participar import Participar


app = Flask(__name__, static_folder="static")

app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_FILE_DIR"] = "./.flask_session"
app.secret_key = "no se me ocurre que poner"

# Inicializar flask-session
Session(app)

# SQLAlchemy config
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
db_path = os.path.join(base_dir, "data", "pokemons.db")

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.cli.command("crear-tablas")
def crear_tablas():
    db.drop_all()
    db.create_all()
    entrenador_aleatorio_1 = Entrenador(nombre="TheGrefg", contraseña="1234")
    db.session.add(entrenador_aleatorio_1)
    entrenador_aleatorio_2 = Entrenador(nombre="Plex", contraseña="1234")
    db.session.add(entrenador_aleatorio_2)
    entrenador_aleatorio_3 = Entrenador(nombre="Aitana", contraseña="1234")
    db.session.add(entrenador_aleatorio_3)
    db.session.commit()
    print("Base de datos creada correctamente.")


app.register_blueprint(home_bp, url_prefix="/")
app.register_blueprint(pokemon_bp, url_prefix="/pokemons")
app.register_blueprint(battle_bp, url_prefix="/battle")
app.register_blueprint(entrenador_bp, url_prefix="/entrenador")


if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=True)
