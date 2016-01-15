"""
    App Users Handler
"""
#
# Imports
#
import os
from datetime import datetime

from flask import jsonify, render_template, request, flash, redirect, url_for
from google.appengine.ext import ndb

from handlers import app
from models.app_user import AppUser
from forms.app_user import AppUserConsistencyForm


#
# Action
#
@app.route('/demo/consistency/<consistency>', methods=['GET', 'POST'])
def demonstrate_consistency(consistency):
    # Which type of consistency? eventual (default), memcache, or institial
    consistency = request.form.get('consistency', consistency)

    # Look for existing user record
    if consistency == 'memcache':
        user = AppUser.find_by_ip_address_pseudo_strongly()
    else:
        user = AppUser.find_by_ip_address_eventually()

    # Create form
    form = AppUserConsistencyForm(request.form)
    form.ip_address.data = AppUser.get_ip_address_from_os()
    form.blank_slate.data = 'Form loaded at %s' % (datetime.utcnow())
    form.consistency.data = consistency

    if user:
        form.stored_browserprint.data = user.browserprint

    # Process request
    if request.method == 'POST':
        if not form.validate():
            flash('Unable to validate form.', 'local')
            return redirect(url_for('demonstrate_consistency'))

        if consistency == 'memcache':
            return process_using_memcache(request, user)
        elif consistency == 'interstitial':
            return process_using_interstitial(request, user)
        else:   # eventual
            return process_using_eventual_consistency(request, user)

    return render_template('app_users/consistency.html',
                           form=form,
                           user=user,
                           consistency=dict(form.consistency.choices).get(consistency))

@app.route('/demo/interstitial/<user_safeurl>', methods=['GET'])
def consistency_interstitial(user_safeurl):
    # By redirecting here rather than directly to the form, this gives
    # datastore a chance to update with eventual consistency.
    user = ndb.Key(urlsafe=user_safeurl).get()
    return render_template('app_users/interstitial.html',
                           user=user)

def process_using_eventual_consistency(request, user):
    redirect_url = url_for('demonstrate_consistency', consistency='eventual')

    if not user:
        user = AppUser.create(request.form.get('browserprint'),
                              request.form.get('blank_slate'))
        flash('New user saved!', 'local')
    else:
        user.browserprint = request.form.get('browserprint')
        user.blank_slate = request.form.get('blank_slate')
        user.put()
        flash('User updated.', 'local')

    return redirect(redirect_url)

def process_using_interstitial(request, user):
    if not user:
        user = AppUser.create(request.form.get('browserprint'),
                              request.form.get('blank_slate'))
        flash('New user saved!', 'local')
    else:
        user.browserprint = request.form.get('browserprint')
        user.blank_slate = request.form.get('blank_slate')
        user.put()
        flash('User updated.', 'local')

    redirect_url = url_for('consistency_interstitial', user_safeurl=user.key.urlsafe())
    return redirect(redirect_url)

def process_using_memcache(request, user):
    """Notice create_and_cache method used and cache called for update."""
    redirect_url = url_for('demonstrate_consistency', consistency='memcache')

    if not user:
        user = AppUser.create_and_cache(request.form.get('browserprint'),
                                        request.form.get('blank_slate'))
        flash('New user saved and cached!', 'local')
    else:
        user.browserprint = request.form.get('browserprint')
        user.blank_slate = request.form.get('blank_slate')
        user.cache()
        user.put()
        flash('User updated and cached.', 'local')

    return redirect(redirect_url)
