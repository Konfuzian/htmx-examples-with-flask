from flask import Blueprint, render_template, request

bp = Blueprint("edit_row", __name__, url_prefix="/edit_row",
    template_folder="templates",)

data = [
    {
        "id": 0,
        "name": "Joe Smith",
        "email": "joe@smith.org",
    },
    {
        "id": 1,
        "name": "Angie MacDowell",
        "email": "angie@macdowell.org",
    },
    {
        "id": 2,
        "name": "Fuqua Tarkenton",
        "email": "fuqua@tarkenton.org",
    },
    {
        "id": 3,
        "name": "Kim Yee",
        "email": "kim@yee.org",
    },
]


@bp.route("/")
def index():
    return render_template("edit_row/index.html.j2", contacts=data)


@bp.route("/contact/<int:id>", methods=["GET", "PUT"])
def contact(id):
    if request.method == "PUT":
        print(request.form)
        data[id] = {
            "id": id,
            "name": request.form["name"],
            "email": request.form["email"],
        }

    return render_template("edit_row/partial.html.j2", contact=data[id])


@bp.route("/contact/<int:id>/edit")
def contact_edit(id):
    print("blubb")
    return render_template("edit_row/edit.html.j2", contact=data[id])
