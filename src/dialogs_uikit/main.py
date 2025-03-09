from flask import Blueprint, render_template

bp = Blueprint(
    "dialogs_uikit",
    __name__,
    url_prefix="/dialogs_uikit",
    template_folder="templates",
)


@bp.route("/")
def index():
    return render_template("dialogs_uikit/index.html.j2")


@bp.route("/modal")
def modal():
    return render_template("dialogs_uikit/modal.html.j2")
