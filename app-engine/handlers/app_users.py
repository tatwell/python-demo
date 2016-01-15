"""
    App Users Handler
"""
#
# Imports
#
import os
from datetime import datetime

from flask import jsonify, render_template, request, flash, redirect, url_for

from handlers import app
from models.app_user import AppUser
from forms.app_user import AppUserConsistencyForm


#
# Action
#
@app.route('/demo/consistency', methods=['GET', 'POST'])
def demonstrate_consistency():
    form = AppUserConsistencyForm(request.form)
    form.ip_address.data = AppUser.get_ip_address_from_os()
    form.blank_slate.data = 'Form loaded at %s' % (datetime.utcnow())

    # Look for existing user record
    user = AppUser.find_by_ip_address_inconsistently()
    if user:
        form.stored_browserprint.data = user.browserprint

    # Process request
    if request.method == 'POST' and form.validate():
        # TODO: Vary method by request.form['consistency']
        if not user:
            user = AppUser.create(request.form.get('browserprint'),
                                  request.form.get('blank_slate'))
            flash('New user saved!', 'local')
            return redirect(url_for('demonstrate_consistency'))
        else:
            user.browserprint = request.form.get('browserprint')
            user.blank_slate = request.form.get('blank_slate')
            user.put()
            flash('user updated.', 'local')
            return redirect(url_for('demonstrate_consistency'))

    form.consistency.data = request.form.get('consistency', 'eventual')
    consistency = dict(form.consistency.choices).get(form.consistency.data)

    return render_template('app_users/consistency.html',
                           form=form,
                           user=user,
                           consistency=consistency)
