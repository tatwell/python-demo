#
# Imports
#
from os.path import dirname, join

from flask import Flask, render_template


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
