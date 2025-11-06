from flask import Blueprint, render_template


battle_bp = Blueprint('battle', __name__)


@battle_bp.route("/battle")
def battle():
    return render_template("battle.html")
