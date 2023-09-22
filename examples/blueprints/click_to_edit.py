from flask import Blueprint, render_template, request


bp = Blueprint("click_to_edit", __name__, url_prefix="/click_to_edit")

data = [
    {
        "firstName": "Joe",
        "lastName": "Blow",
        "email": "joe@blow.com",
    }
]


@bp.route("/", defaults={"id": 0})
@bp.route("/contact/<int:id>", methods=["GET", "PUT"])
def contact(id):
    if request.method == "PUT":
        data[id] = {k: request.form[k] for k in ("firstName", "lastName", "email")}

    return render_template("click_to_edit/index.html.j2", contact=data[id])


@bp.route("/contact/<int:id>/edit")
def contact_edit(id):
    return render_template("click_to_edit/edit.html.j2", contact=data[id])
