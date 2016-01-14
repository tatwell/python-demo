"""
    App Handler Module

    Flask app is loaded here in order to avoid repetition. Other handler should
    import this module.

    Other handler modules must have unique function names for their endpoints
    (e.g. journals_index rather than just index). If not, Flask will raise the
    following error:

    AssertionError: View function mapping is overwriting an existing endpoint function
"""
from datetime import date, datetime
from os.path import dirname, join

from flask import Flask, request, render_template
from flask.json import JSONEncoder

from config import secrets


#
# Constants
#
APP_PATH = dirname(dirname(__file__))
TEMPLATE_PATH = join(APP_PATH, 'templates')


#
# Flask App
#
app = Flask(__name__, template_folder=TEMPLATE_PATH)
app.secret_key = secrets.FLASK_SECRET_KEY


#
# Custom JSON Encode for date objects
# See https://github.com/jeffknupp/sandman/issues/22#issuecomment-35677606
#
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, date):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)
app.json_encoder = CustomJSONEncoder


#
# Template Globals
# http://stackoverflow.com/a/29978965/1093087
#
@app.context_processor
def common_variables():
    return dict(
        current_year = date.today().year,
    )

@app.context_processor
def template_helpers():
    def date_now(format="%Y-%m-%d %H:%M:%S"):
        """ returns the formated datetime """
        return datetime.now().strftime(format)

    def navbar_class(tab):
        # Use request.path. request.url_rule.rule does not exist for errorhandler.
        route = request.path
        if tab in route:
            return 'active'
        else:
            return 'inactive'

    def format_amount(value, default=None):
        if not value:
            return default
        else:
            return '%.2f' % (value)

    return dict(
        date_now=date_now,
        navbar_class=navbar_class,
        format_amount=format_amount
    )

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
