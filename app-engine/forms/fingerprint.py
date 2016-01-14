"""
    Summer Forms
"""
import re

from wtforms import Form, validators, StringField, SelectField


class InconsistentFingerprintForm(Form):
    browser = StringField('Browser Fingerprint')
    comment = StringField('Comment')
    consistency = SelectField('Type', choices=[('eventual consistency', 'default'),
                                               ('memcache consistency', 'memcache'),
                                               ('interstital', 'interstital')])


