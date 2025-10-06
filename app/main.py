from flask import Flask, render_template, jsonify, current_app
import json

app = Flask(__name__, static_folder="static")

with open("data/pokemon.json", encoding="utf-8") as f:
    app.config["DATA"] = json.load(f)


@app.route("/data")
def home():
    return jsonify(current_app.config["DATA"])


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test-base")
def bienvenida():
    return render_template("base.html")


if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=True)
