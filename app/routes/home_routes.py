import json
from flask import Blueprint, app, current_app, jsonify, render_template
from app.forms.trainer_form import TrainerForm

home_bp = Blueprint('home', __name__, template_folder= 'templates')


@home_bp.route("/")
def index():
    return render_template("index.html")

@home_bp.route("/data")
def home():
    return jsonify(current_app.config["DATA"])

@home_bp.route("/formulario")
def formulario():
    form = TrainerForm()
    if form.validate_on_submit():
        entrenador = form.entrenador.data
       
    
    return render_template("formulario.html", form = form)