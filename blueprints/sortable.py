from flask import Blueprint, render_template


bp = Blueprint("sortable", __name__, url_prefix="/sortable")


@bp.route("/")
def index():
    return render_template("sortable/index.html.j2")


@bp.route("/items", methods=("POST",))
def items():
    # store order of items here
    return ("", 204)
