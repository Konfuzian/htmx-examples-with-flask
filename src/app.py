import click
from flask import Flask, render_template
from jinja2 import StrictUndefined

from src.examples.active_search.main import bp as active_search
# from examples.animations import animations
# from examples.bulk_update import bulk_update
# from examples.click_to_edit import click_to_edit
# from examples.click_to_load import click_to_load
# from examples.confirm import confirm
# from examples.delete_row import delete_row
# from examples.dialogs_bootstrap import dialogs_bootstrap
# from examples.dialogs_browser import dialogs_browser
# from examples.dialogs_custom import dialogs_custom
# from examples.dialogs_uikit import dialogs_uikit
# from examples.edit_row import edit_row
# from examples.file_upload import file_upload
# from examples.infinite_scroll import infinite_scroll
# from examples.inline_validation import inline_validation
# from examples.keyboard_shortcuts import keyboard_shortcuts
# from examples.lazy_loading import lazy_loading
# from examples.preserving_file_inputs import preserving_file_inputs
# from examples.progress_bar import progress_bar
# from examples.sortable import sortable
# from examples.tabs_hateoas import tabs_hateoas
# from examples.tabs_hyperscript import tabs_hyperscript
# from examples.updating_other_content import updating_other_content
# from examples.value_select import value_select


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
# app.register_blueprint(click_to_edit.bp)
# app.register_blueprint(bulk_update.bp)
# app.register_blueprint(click_to_load.bp)
# app.register_blueprint(delete_row.bp)
# app.register_blueprint(edit_row.bp)
# app.register_blueprint(lazy_loading.bp)
# app.register_blueprint(inline_validation.bp)
# app.register_blueprint(infinite_scroll.bp)
app.register_blueprint(active_search)
# app.register_blueprint(progress_bar.bp)
# app.register_blueprint(value_select.bp)
# app.register_blueprint(animations.bp)
# app.register_blueprint(file_upload.bp)
# app.register_blueprint(preserving_file_inputs.bp)
# app.register_blueprint(dialogs_browser.bp)
# app.register_blueprint(dialogs_uikit.bp)
# app.register_blueprint(dialogs_bootstrap.bp)
# app.register_blueprint(dialogs_custom.bp)
# app.register_blueprint(tabs_hateoas.bp)
# app.register_blueprint(tabs_hyperscript.bp)
# app.register_blueprint(keyboard_shortcuts.bp)
# app.register_blueprint(sortable.bp)
# app.register_blueprint(updating_other_content.bp)
# app.register_blueprint(confirm.bp)


@app.route("/")
def index():
    return render_template("index.html.j2")


@click.command()
@click.option("--debug", is_flag=True, default=False, help="enable auto reload and debugging")
def main(debug: bool):
    app.run(debug=debug)


if __name__ == "__main__":
    main()
