from flask import Blueprint, render_template

bp = Blueprint("dialogs_bootstrap", __name__, url_prefix="/dialogs_bootstrap",
    template_folder="templates",)


@bp.route("/")
def index():
    return render_template("dialogs_bootstrap/index.html.j2")


@bp.route("/modal")
def modal():
    return render_template("dialogs_bootstrap/modal.html.j2")
