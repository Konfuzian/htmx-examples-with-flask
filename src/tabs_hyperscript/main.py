from flask import Blueprint, render_template

bp = Blueprint(
    "tabs_hyperscript",
    __name__,
    url_prefix="/tabs_hyperscript",
    template_folder="templates",
)


@bp.route("/")
def index():
    return render_template("tabs_hyperscript/index.html.j2")


@bp.route("/tab1/")
def tab1():
    return render_template("tabs_hyperscript/tab1.html.j2")


@bp.route("/tab2/")
def tab2():
    return render_template("tabs_hyperscript/tab2.html.j2")


@bp.route("/tab3/")
def tab3():
    return render_template("tabs_hyperscript/tab3.html.j2")
