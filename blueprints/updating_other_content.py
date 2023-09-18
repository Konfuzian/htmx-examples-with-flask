from flask import Blueprint, make_response, render_template, request


bp = Blueprint("updating_other_content", __name__, url_prefix="/updating_other_content")

data = [
    {
        "name": "Joe Smith",
        "email": "joe@smith.org",
    },
    {
        "name": "Angie MacDowell",
        "email": "angie@macdowell.org",
    },
]


@bp.route("/")
def index():
    return render_template("updating_other_content/index.html.j2", contacts=data)


@bp.route("/contacts1", methods=("POST",))
def contacts1():
    data.append(
        {
            "name": request.form["name"],
            "email": request.form["email"],
        }
    )
    return render_template("updating_other_content/partial_1.html.j2", contacts=data)


@bp.route("/contacts2", methods=("POST",))
def contacts2():
    contact = {
        "name": request.form["name"],
        "email": request.form["email"],
    }
    data.append(contact)
    return render_template("updating_other_content/partial_2.html.j2", contact=contact)


@bp.route("/contacts3", methods=("POST",))
def contacts3():
    data.append(
        {
            "name": request.form["name"],
            "email": request.form["email"],
        }
    )
    res = make_response("", 204)
    res.headers["HX-Trigger"] = "newContact"
    return res


@bp.route("/contacts3/table")
def contacts3_table():
    return render_template("updating_other_content/partial_table.html.j2", contacts=data)


@bp.route("/contacts4", methods=("POST",))
def contacts4():
    data.append(
        {
            "name": request.form["name"],
            "email": request.form["email"],
        }
    )
    return render_template("updating_other_content/partial_4.html.j2")


@bp.route("/contacts4/table")
def contacts4_table():
    return render_template("updating_other_content/partial_table.html.j2", contacts=data)
