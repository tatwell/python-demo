"""
    Fingerprint Model

    Really just a test model. Can be used with browser fingerprint lib.
"""
from google.appengine.ext import ndb
from google.appengine.api import memcache
from google.appengine.api import users
from datetime import date, timedelta


class Fingerprint(ndb.Model):
    # Fields
    ip_address      = ndb.StringProperty(required=True)     # Also key.id()
    browser         = ndb.StringProperty(required=False)
    comment         = ndb.StringProperty(required=False)

    # Timestamps
    created_at      = ndb.DateTimeProperty(auto_now_add=True)
    updated_at      = ndb.DateTimeProperty(auto_now=True)

    # Virtual Fields
    @property
    def key_id(self):
        return self.key.id()

    # Class Methods
    @staticmethod
    def find_by_ip_address_inconsistently(ip_address):
        return Fingerprint.query(Fingerprint.ip_address == ip_address).get()

    @staticmethod
    def find_by_ip_address_consistently(ip_address):
        return Fingerprint.get_by_id(ip_address)

    @staticmethod
    def find_by_ip_address_pseudo_consistently(ip_address):
        fingerprint = memcache.get(ip_address)

        if not fingerprint:
            fingerprint = Fingerprint.find_by_ip_address_inconsistently(ip_address)

        return fingerprint


    @staticmethod
    def create(ip_address, browser_print=None, comment=None):
        new_fingerprint = Fingerprint(id=ip_address,
                                      ip_address=ip_address,
                                      browser=browser_print,
                                      comment=comment)
        new_fingerprint.put()
        return new_fingerprint

    @staticmethod
    def create_with_consistency(ip_address, browser_print=None, comment=None):
        # Create datastore record
        new_fingerprint = Fingerprint.create_with_consistency(ip_address,
                                                              browser_print,
                                                              comment)

        # Create memcache record
        memcache.add(new_fingerprint.ip_address, new_fingerprint)

        return new_fingerprint
