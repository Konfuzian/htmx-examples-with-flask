from flask import Blueprint, render_template


bp = Blueprint("delete_row", __name__, url_prefix="/delete_row")

data = {
    0: {
        "name": "Joe Smith",
        "email": "joe@smith.org",
        "status": "Active",
    },
    1: {
        "name": "Angie MacDowell",
        "email": "angie@macdowell.org",
        "status": "Active",
    },
    2: {
        "name": "Fuqua Tarkenton",
        "email": "fuqua@tarkenton.org",
        "status": "Active",
    },
    3: {
        "name": "Kim Yee",
        "email": "kim@yee.org",
        "status": "Inactive",
    },
}


@bp.route("/")
def index():
    return render_template("delete_row/index.html.j2", contacts=data)


@bp.route("/contact/<int:id>", methods=["DELETE"])
def contact(id):
    del data[id]
    return render_template("delete_row/index.html.j2", contacts=data)
