from flask import Blueprint, render_template, request

bp = Blueprint("bulk_update", __name__, url_prefix="/bulk_update",
    template_folder="templates",)

data = [
    {
        "name": "Joe Smith",
        "email": "joe@smith.org",
        "status": "Active",
    },
    {
        "name": "Angie MacDowell",
        "email": "angie@macdowell.org",
        "status": "Active",
    },
    {
        "name": "Fuqua Tarkenton",
        "email": "fuqua@tarkenton.org",
        "status": "Active",
    },
    {
        "name": "Kim Yee",
        "email": "kim@yee.org",
        "status": "Inactive",
    },
]


@bp.route("/")
def index():
    return render_template("bulk_update/index.html.j2", contacts=data)


@bp.route("/activate", methods=("PUT",))
def activate():
    for id in request.form.getlist("ids", type=int):
        data[id]["status"] = "Active"

    return render_template("bulk_update/index.html.j2", contacts=data)


@bp.route("/deactivate", methods=("PUT",))
def deactivate():
    for id in request.form.getlist("ids", type=int):
        data[id]["status"] = "Inactive"

    return render_template("bulk_update/index.html.j2", contacts=data)
