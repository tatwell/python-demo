#
# Imports
#
from os.path import dirname, join
import arrow
import dateutil

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
# https://github.com/crsmithdev/arrow/issues/240
@app.route('/arrow/version')
def arrow_version():
    return jsonify({
        'arrow': arrow.VERSION,
        'dateutil': dateutil.__version__
    })

@app.route('/arrow/now')
@app.route('/arrow/now/<timezone>')
def arrow_now(timezone=None):
    now = arrow.utcnow()
    json_data = {
        'now': str(now),
        'timezone': 'UTC'
    }

    if timezone:
        timezone = timezone.replace('-', '/')
        json_data['timezone'] = timezone
        try:
            json_data['now'] = str(now.to(timezone))
        except arrow.parser.ParserError, e:
            json_data['now'] = None
            json_data['error'] = str(e)

    return jsonify(json_data)

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
