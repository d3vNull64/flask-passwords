from flask import Blueprint, render_template

generator_bp = Blueprint("generator", __name__)


@generator_bp.route("/generator")
def generator():
    return render_template("generator.djhtml")
