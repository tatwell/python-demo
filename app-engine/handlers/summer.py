"""
    summer.py
    Summer Handler
"""
#
# Imports
#
from handlers import app
from flask import jsonify, render_template, request

from services.summer import diophantine_subset_sum, SummerTimeoutError


#
# Action
#
@app.route('/summer', methods = ['GET'])
def index():
    number_set = request.args.get('set', '')
    target = request.args.get('sum')

    numbers = [int(n) for n in number_set.split(' ')]
    target = int(target)

    subset = diophantine_subset_sum(numbers, target)

    # Render view
    return jsonify({
        'numbers': numbers,
        'sum': target,
        'subset': subset
    })

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
