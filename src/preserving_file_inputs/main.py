from flask import Blueprint, render_template

bp = Blueprint(
    "preserving_file_inputs",
    __name__,
    url_prefix="/preserving_file_inputs",
    template_folder="templates",
)


@bp.route("/")
def index():
    return render_template("preserving_file_inputs/index.html.j2")


@bp.route("/upload", methods=("POST",))
def upload_hyperscript():
    return "Uploaded!"
