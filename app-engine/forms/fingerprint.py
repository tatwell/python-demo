"""
    Summer Forms
"""
import re

from wtforms import Form, validators, StringField, HiddenField, SelectField

NDB_CONSISTENCY_CHOICES = [
    ('eventual', 'Eventual (Default)'),
    ('memcache', 'Memcache-Assisted Pseudo-Strong'),
    ('interstital', 'Interstital Pseudo-Strong')
]

class ConsistentFingerprintForm(Form):
    ip_address = StringField('IP Address')
    browser = StringField('Current Browser Fingerprint')
    browserprint = HiddenField('Hidden Browser')
    stored_browser = StringField('Stored Browser Fingerprint')
    comment = StringField('Comment')
    consistency = SelectField('Consistency Method', choices=NDB_CONSISTENCY_CHOICES)


