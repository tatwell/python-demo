#
# Imports
#
from os.path import dirname, join

from flask import Flask, render_template, jsonify


#
# Constants
#
APP_PATH = dirname(__file__)
TEMPLATE_PATH = join(APP_PATH, 'templates')


#
# Flask App
#
app = Flask(__name__, template_folder=TEMPLATE_PATH)


#
# Endpoints
#
@app.route('/', methods=['GET'])
def main_index():
    """Home page."""
    return render_template('index.html')

# Arrow API
# Mainly to test fix for this issue:
#
@app.route('/arrow/version', methods=['GET'])
def arrow_version():
    import arrow
    import dateutil

    return jsonify({
        'arrow': arrow.VERSION,
        'dateutil': dateutil.__version__
    })


#
# Exception Handlers
#
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return render_template('500.html', error=e), 500
