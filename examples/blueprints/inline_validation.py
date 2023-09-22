from flask import Blueprint, render_template, request


bp = Blueprint("inline_validation", __name__, url_prefix="/inline_validation")


def validate_email(email):
    return email == "test@test.com"


@bp.route("/")
@bp.route("/contact", methods=("POST",))
def contact():
    return render_template("inline_validation/index.html.j2")


@bp.route("/contact/email", methods=("POST",))
def contact_edit():
    email = request.form["email"]
    if not validate_email(email):
        return render_template("inline_validation/partial_error.html.j2", email=email)

    return render_template("inline_validation/partial_valid.html.j2", email=email)
