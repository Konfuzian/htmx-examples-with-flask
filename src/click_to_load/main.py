import random
import string

from flask import Blueprint, render_template, request

bp = Blueprint(
    "click_to_load",
    __name__,
    url_prefix="/click_to_load",
    template_folder="templates",
)


def generate_contacts(page=1, page_size=10):
    def generate_contact(i):
        def generate_id(n=10):
            return "".join(random.choices(string.ascii_uppercase + string.digits, k=n))

        return {
            "name": "Agent Smith",
            "email": f"void{page * page_size + i}@null.org",
            "id": generate_id(),
        }

    return [generate_contact(i) for i in range(page_size)]


@bp.route("/", defaults={"page": 1})
def index(page):
    return render_template(
        "click_to_load/index.html.j2", contacts=generate_contacts(page=page), page=page
    )


@bp.route("/contacts/")
def contacts():
    page = int(request.args.get("page", 1))
    return render_template(
        "click_to_load/partial.html.j2", contacts=generate_contacts(page=page), page=page
    )
