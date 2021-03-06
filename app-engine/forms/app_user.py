"""
    Summer Forms
"""
import re

from wtforms import Form, validators, StringField, HiddenField, SelectField

NDB_CONSISTENCY_CHOICES = [
    ('eventual', 'Eventual (Default)'),
    ('memcache', 'Memcache-Assisted Pseudo-Strong'),
    ('interstitial', 'Interstitial Pseudo-Strong')
]

class AppUserConsistencyForm(Form):
    ip_address = StringField('IP Address')
    browserprint = HiddenField('Hidden Browserprint')
    blank_slate = StringField('Blank Slate (whatever you want)')
    consistency = SelectField('Consistency Method', choices=NDB_CONSISTENCY_CHOICES)

    # These are no longer displayed. But form still functions so leaving them for now.
    current_browserprint = StringField('Current Browser Fingerprint')
    stored_browserprint = StringField('Stored Browser Fingerprint')
