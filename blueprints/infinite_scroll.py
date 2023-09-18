import random
import string
import time

from flask import Blueprint, render_template, request


bp = Blueprint("infinite_scroll", __name__, url_prefix="/infinite_scroll")


def generate_contacts(page=1, page_size=20):
    def generate_contact(i):
        def generate_id(n=15):
            return "".join(random.choices(string.ascii_uppercase + string.digits, k=n))

        return {"name": "Agent Smith", "email": f"void{10 + (page - 1) * page_size + i}@null.org", "id": generate_id()}

    return [generate_contact(i) for i in range(page_size)]


@bp.route("/", defaults={"page": 1})
def index(page):
    return render_template("infinite_scroll/index.html.j2", contacts=generate_contacts(page=page), page=page)


@bp.route("/contacts/")
def contacts():
    page = int(request.args.get("page", 1))
    time.sleep(1)
    return render_template("infinite_scroll/partial.html.j2", contacts=generate_contacts(page=page), page=page)
