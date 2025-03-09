from flask import Blueprint, render_template

bp = Blueprint(
    "confirm",
    __name__,
    url_prefix="/confirm",
    template_folder="templates",
)


@bp.route("/")
def index():
    return render_template("confirm/index.html.j2")
