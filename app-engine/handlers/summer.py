"""
    summer.py
    Summer Handler
"""
#
# Imports
#
from handlers import app
from flask import jsonify, render_template, request

from forms.summer import SummerForm
from services.summer import diophantine_subset_sum, SummerRuntimeError


#
# Action
#
@app.route('/summer', methods = ['GET', 'POST'])
def index():
    subset = None
    error = None

    form = SummerForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
            subset = diophantine_subset_sum(form.numbers.data, form.target.data)
            subset = [format(v, ',d') for v in sorted(subset)]
        except SummerRuntimeError, e:
            error = e

    return render_template('summer/index.html', form=form, subset=subset, error=error)

#
# Error Handlers
#
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
