import click
from flask import Flask, render_template
from jinja2 import StrictUndefined

from examples.blueprints import click_to_load, dialogs_browser, value_select, click_to_edit, dialogs_custom, \
    preserving_file_inputs, bulk_update, confirm, sortable, infinite_scroll, dialogs_uikit, edit_row, tabs_hyperscript, \
    progress_bar, updating_other_content, lazy_loading, file_upload, animations, active_search, dialogs_bootstrap, \
    delete_row, inline_validation, tabs_hateoas, keyboard_shortcuts

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined

app.register_blueprint(click_to_edit.bp)
app.register_blueprint(bulk_update.bp)
app.register_blueprint(click_to_load.bp)
app.register_blueprint(delete_row.bp)
app.register_blueprint(edit_row.bp)
app.register_blueprint(lazy_loading.bp)
app.register_blueprint(inline_validation.bp)
app.register_blueprint(infinite_scroll.bp)
app.register_blueprint(active_search.bp)
app.register_blueprint(progress_bar.bp)
app.register_blueprint(value_select.bp)
app.register_blueprint(animations.bp)
app.register_blueprint(file_upload.bp)
app.register_blueprint(preserving_file_inputs.bp)
app.register_blueprint(dialogs_browser.bp)
app.register_blueprint(dialogs_uikit.bp)
app.register_blueprint(dialogs_bootstrap.bp)
app.register_blueprint(dialogs_custom.bp)
app.register_blueprint(tabs_hateoas.bp)
app.register_blueprint(tabs_hyperscript.bp)
app.register_blueprint(keyboard_shortcuts.bp)
app.register_blueprint(sortable.bp)
app.register_blueprint(updating_other_content.bp)
app.register_blueprint(confirm.bp)


@app.route('/')
def index():
    return render_template('index.html.j2')


@click.command()
@click.option(
    "--debug",
    is_flag=True,
    default=False,
    help="enable auto reload and debugging"
)
def main(debug: bool):
    app.run(debug=debug)


if __name__ == '__main__':
    main()
