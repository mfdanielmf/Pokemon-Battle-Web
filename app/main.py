import sqlite3
from flask import Flask
from flask_session import Session

from app.routes.battle_routes import battle_bp
from app.routes.pokemon_routes import pokemon_bp
from app.routes.home_routes import home_bp

app = Flask(__name__, static_folder="static")

app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_FILE_DIR"] = "./.flask_session"
app.secret_key = "no se me ocurre que poner"

# Inicializar flask-session
Session(app)

app.register_blueprint(home_bp, url_prefix="/")
app.register_blueprint(pokemon_bp, url_prefix="/pokemons")
app.register_blueprint(battle_bp, url_prefix="/battle")

def get_connection():
    conn = sqlite3.connect("data/pokemons.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/productos")
def listar_productos():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, precio FROM productos ORDER BY id;")
    productos = cur.fetchall()  #obtener los productos en una lista
    cur.close()
    conn.close()
    return render_template("productos.html", productos=productos)

if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=True)
