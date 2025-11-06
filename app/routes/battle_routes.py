

from flask import Blueprint, render_template


battle_bp = Blueprint('battle', __name__, template_folder= 'templates')

@battle_bp.route("/battle")
def battle():
    return render_template("battle.html")