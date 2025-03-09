from flask import Blueprint, render_template

bp = Blueprint("keyboard_shortcuts", __name__, url_prefix="/keyboard_shortcuts",
    template_folder="templates",)


@bp.route("/")
def index():
    return render_template("keyboard_shortcuts/index.html.j2")


@bp.route("/doit", methods=("POST",))
def do_it():
    return "Did it!"
