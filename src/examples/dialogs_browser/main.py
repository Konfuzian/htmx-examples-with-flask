from flask import Blueprint, render_template, request

bp = Blueprint("dialogs_browser", __name__, url_prefix="/dialogs_browser",
    template_folder="templates",)


@bp.route("/")
def index():
    return render_template("dialogs_browser/index.html.j2")


@bp.route("/submit", methods=("POST",))
def graph():
    response = request.headers["HX-Prompt"]
    return f"User entered <i>{response}</i>"
