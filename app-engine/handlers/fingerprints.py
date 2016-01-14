"""
    summer.py
    Summer Handler
"""
#
# Imports
#
from handlers import app
from flask import jsonify, render_template, request, flash

from forms.fingerprint import InconsistentFingerprintForm


#
# Action
#
@app.route('/fingerprints/consistency', methods=['GET', 'POST'])
def fingerprint_consistency():
    form = InconsistentFingerprintForm(request.form)
    print request.form

    if request.method == 'POST':
        flash('submitted', 'info')
        if form.validate():
            pass

    return render_template('fingerprints/consistency.html',
                           form=form)

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
