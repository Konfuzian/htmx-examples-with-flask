from flask import Blueprint, render_template


bp = Blueprint("dialogs_custom", __name__, url_prefix="/dialogs_custom")


@bp.route("/")
def index():
    return render_template("dialogs_custom/index.html.j2")


@bp.route("/modal")
def modal():
    return render_template("dialogs_custom/modal.html.j2")
