from time import sleep

from flask import Blueprint, render_template


bp = Blueprint("animations", __name__, url_prefix="/animations")


@bp.route("/")
def index():
    return render_template("animations/index.html.j2", color="red")


color_options = ["red", "blue", "green", "orange"]
color_index = 0


@bp.route("/colors/")
def colors():
    global color_index
    color_index = (color_index + 1) % len(color_options)
    return render_template("animations/color_swap.html.j2", color=color_options[color_index])


@bp.route("/fade_out_demo", methods=("DELETE",))
def fade_out():
    return ""


@bp.route("/fade_in_demo", methods=("POST",))
def fade_in():
    return render_template("animations/fade_in_on_addition.html.j2")


@bp.route("/name", methods=("POST",))
def name():
    sleep(0.5)
    return "Submitted!"


@bp.route("/initial-content")
def initial_content():
    return render_template("animations/view_transition_initial.html.j2")


@bp.route("/new-content")
def new_content():
    return render_template("animations/view_transition_new.html.j2")
