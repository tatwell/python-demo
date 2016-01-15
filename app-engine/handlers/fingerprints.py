"""
    summer.py
    Summer Handler
"""
#
# Imports
#
import os
from datetime import datetime

from flask import jsonify, render_template, request, flash, redirect, url_for

from handlers import app
from models.fingerprint import Fingerprint
from forms.fingerprint import ConsistentFingerprintForm


#
# Action
#
@app.route('/fingerprints/consistency', methods=['GET', 'POST'])
def fingerprint_consistency():
    ip_address = os.environ.get('REMOTE_ADDR', 'unknown')
    form = ConsistentFingerprintForm(request.form)
    form.ip_address.data = ip_address
    form.comment.data = 'Form loaded at %s' % (datetime.utcnow())

    # Look for existing fingerprint record
    fingerprint = Fingerprint.find_by_ip_address_inconsistently(ip_address)
    if fingerprint:
        form.stored_browser.data = fingerprint.browser

    # Process request
    if request.method == 'POST' and form.validate():
        # TODO: Vary method by request.form['consistency']
        if not fingerprint:
            fingerprint = Fingerprint.create(ip_address,
                                             request.form.get('browserprint'),
                                             request.form.get('comment'))
            flash('New fingerprint saved!', 'local')
            return redirect(url_for('fingerprint_consistency'))
        else:
            fingerprint.browser = request.form.get('browserprint')
            fingerprint.comment = request.form.get('comment')
            fingerprint.put()
            flash('Fingerprint updated.', 'local')
            return redirect(url_for('fingerprint_consistency'))

    form.consistency.data = request.form.get('consistency', 'eventual')
    consistency = dict(form.consistency.choices).get(form.consistency.data)

    return render_template('fingerprints/consistency.html',
                           form=form,
                           fingerprint=fingerprint,
                           consistency=consistency)
