import click
from flask import Flask, render_template
from jinja2 import StrictUndefined

from src.examples.active_search.main import bp as active_search
from src.examples.animations.main import bp as animations
from src.examples.bulk_update.main import bp as bulk_update
from src.examples.click_to_edit.main import bp as click_to_edit
from src.examples.click_to_load.main import bp as click_to_load
from src.examples.confirm.main import bp as confirm
from src.examples.delete_row.main import bp as delete_row
from src.examples.dialogs_bootstrap.main import bp as dialogs_bootstrap
from src.examples.dialogs_browser.main import bp as dialogs_browser
from src.examples.dialogs_custom.main import bp as dialogs_custom
from src.examples.dialogs_uikit.main import bp as dialogs_uikit
from src.examples.edit_row.main import bp as edit_row
from src.examples.file_upload.main import bp as file_upload
from src.examples.infinite_scroll.main import bp as infinite_scroll
from src.examples.inline_validation.main import bp as inline_validation
from src.examples.keyboard_shortcuts.main import bp as keyboard_shortcuts
from src.examples.lazy_loading.main import bp as lazy_loading
from src.examples.preserving_file_inputs.main import bp as preserving_file_inputs
from src.examples.progress_bar.main import bp as progress_bar
from src.examples.sortable.main import bp as sortable
from src.examples.tabs_hateoas.main import bp as tabs_hateoas
from src.examples.tabs_hyperscript.main import bp as tabs_hyperscript
from src.examples.updating_other_content.main import bp as updating_other_content
from src.examples.value_select.main import bp as value_select


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.register_blueprint(click_to_edit)
app.register_blueprint(bulk_update)
app.register_blueprint(click_to_load)
app.register_blueprint(delete_row)
app.register_blueprint(edit_row)
app.register_blueprint(lazy_loading)
app.register_blueprint(inline_validation)
app.register_blueprint(infinite_scroll)
app.register_blueprint(active_search)
app.register_blueprint(progress_bar)
app.register_blueprint(value_select)
app.register_blueprint(animations)
app.register_blueprint(file_upload)
app.register_blueprint(preserving_file_inputs)
app.register_blueprint(dialogs_browser)
app.register_blueprint(dialogs_uikit)
app.register_blueprint(dialogs_bootstrap)
app.register_blueprint(dialogs_custom)
app.register_blueprint(tabs_hateoas)
app.register_blueprint(tabs_hyperscript)
app.register_blueprint(keyboard_shortcuts)
app.register_blueprint(sortable)
app.register_blueprint(updating_other_content)
app.register_blueprint(confirm)


@app.route("/")
def index():
    return render_template("index.html.j2")


@click.command()
@click.option("--debug", is_flag=True, default=False, help="enable auto reload and debugging")
def main(debug: bool):
    app.run(debug=debug)


if __name__ == "__main__":
    main()
