from flask import Blueprint, render_template, request, session
from models import Tools

generator_bp = Blueprint("generator", __name__)


def fill_default_session():
    session.setdefault("lower", 1)
    session.setdefault("upper", 0)
    session.setdefault("number", 0)
    session.setdefault("hash", 0)
    session.setdefault("dots", 0)
    session.setdefault("dash", 0)
    session.setdefault("symbol", 0)
    session.setdefault("bracket", 0)
    session.setdefault("extended", 0)
    session.setdefault("length", 8)


@generator_bp.route("/generator", methods=["GET", "POST"])
def generator():
    # session.clear()
    options = ["lower"]

    if request.method == "POST":
        options = list(request.form.keys())
        options.remove("numberLen")

        # get length and update session length
        length = request.form.get("numberLen", 8)
        session["length"] = length

        # If no selected option set this
        if len(options) == 0:
            options = ["lower"]
            session["lower"] = 1

        # copy session keys, delete length
        # and set 1 only in selected options
        keys = list(session.keys())
        keys.remove("length")

        for key in keys:
            session[key] = 1 if key in options else 0

    fill_default_session()
    password = Tools(int(session["length"]), options)

    return render_template("generator.djhtml", generated_password=password.generated_password())
