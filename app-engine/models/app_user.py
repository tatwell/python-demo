"""
    AppUser Model

    User model. Calling this AppUser to avoid any confusion or conflict with the Google
    App Engine User class.
"""
import os

from google.appengine.ext import ndb
from google.appengine.api import memcache


class AppUser(ndb.Model):
    #
    # Fields
    #
    ip_address      = ndb.StringProperty(required=True)     # Also key.id()
    browserprint    = ndb.StringProperty(required=False)
    blank_slate     = ndb.StringProperty(required=False)

    # Timestamps
    created_at      = ndb.DateTimeProperty(auto_now_add=True)
    updated_at      = ndb.DateTimeProperty(auto_now=True)

    #
    # Virtual Fields
    #
    @property
    def key_id(self):
        return self.key.id()

    #
    # Class Methods
    #
    @staticmethod
    def find_by_ip_address_consistently():
        ip_address = AppUser.get_ip_address_from_os()
        return AppUser.get_by_id(ip_address)

    @staticmethod
    def find_by_ip_address_eventually():
        ip_address = AppUser.get_ip_address_from_os()
        return AppUser.query(AppUser.ip_address == ip_address).get()

    @staticmethod
    def find_by_ip_address_pseudo_strongly():
        ip_address = AppUser.get_ip_address_from_os()
        app_user = memcache.get(ip_address)

        if not app_user:
            app_user = AppUser.find_by_ip_address_eventually()

        return app_user

    @staticmethod
    def create(browserprint=None, blank_slate=None):
        ip_address = AppUser.get_ip_address_from_os()
        app_user = AppUser(id=ip_address,
                           ip_address=ip_address,
                           browserprint=browserprint,
                           blank_slate=blank_slate)
        app_user.put()
        return app_user

    @staticmethod
    def create_and_cache(browserprint=None, blank_slate=None):
        # Create datastore record
        app_user = AppUser.create(ip_address,
                                  browserprint,
                                  blank_slate)

        app_user.cache()
        return app_user

    @staticmethod
    def get_ip_address_from_os():
        return os.environ.get('REMOTE_ADDR', 'unknown')

    #
    # Instance Methods
    #
    def cache(self):
        # Add or overwrite existing cache record.
        memcache.set(self.ip_address, self)
