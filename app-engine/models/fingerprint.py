"""
    Fingerprint Model

    Really just a test model. Can be used with browser fingerprint lib.
"""
from google.appengine.ext import ndb
from google.appengine.api import memcache
from google.appengine.api import users
from datetime import date, timedelta


DNA_BASES = ['A', 'C', 'T', 'G']


class Fingerprint(ndb.Model):
    # Fields
    browser         = ndb.StringProperty(required=True)
    dna_sequence    = ndb.StringProperty(required=False)

    # Timestamps
    created_at      = ndb.DateTimeProperty(auto_now_add=True)
    updated_at      = ndb.DateTimeProperty(auto_now=True)
