from flask import Blueprint, render_template


bp = Blueprint("file_upload", __name__, url_prefix="/file_upload")


@bp.route("/")
def index():
    return render_template("file_upload/index.html.j2")


@bp.route("/upload", methods=("POST",))
def upload_hyperscript():
    # upload logic would go here, see e.g. https://flask.palletsprojects.com/en/2.3.x/patterns/fileuploads/

    return ("", 204)  # return empty response so htmx does not overwrite the progress bar value
