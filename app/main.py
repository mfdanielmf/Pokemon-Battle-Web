from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def bienvenida():
    return render_template("bienvenida.html")


if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=True)
