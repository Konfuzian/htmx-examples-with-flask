from flask import Blueprint, render_template

bp = Blueprint(
    "lazy_loading",
    __name__,
    url_prefix="/lazy_loading",
    template_folder="templates",
)


@bp.route("/")
def index():
    return render_template("lazy_loading/index.html.j2")


@bp.route("/graph")
def graph():
    return render_template("lazy_loading/image.html.j2")
