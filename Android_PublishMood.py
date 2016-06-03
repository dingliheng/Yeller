__author__ = 'Liheng'
from google.appengine.ext.webapp import blobstore_handlers
from models import User
from google.appengine.api import users
from models import Yeller
import webapp2
from google.appengine.ext import ndb

def user_key(user_id):
    """Constructs a Datastore key for a Guestbook entity.
    We use guestbook_name as the key.
    """
    return ndb.Key('User', user_id)

class Android_PublishMood(blobstore_handlers.BlobstoreUploadHandler):
    def get(self):

        User_email = self.request.params.get("User_email")
        to_whom = self.request.params.get("to:")
        content = self.request.params.get("content")
        is_Anonynmous = self.request.params.get("is_Anonynmous")
        latitude = self.request.params.get("latitude")
        longitude = self.request.params.get("longitude")
        current_user = User.query(User.email == User_email).fetch(1)[0]
        newyeller = Yeller(author = User_email)
        if is_Anonynmous == "true":
            newyeller.Anonymity = True
        else:
            newyeller.Anonymity = False
        newyeller.to_whom = to_whom
        newyeller.text = content
        newyeller.latitude = float(latitude)
        newyeller.longitude = float(longitude)

        yeller_key = newyeller.put()
        newyeller.key_id = str(newyeller.key.id())
        newyeller.put()
        current_user.yellers_owned.append(yeller_key)

        current_user.put()

app = webapp2.WSGIApplication([
                               ('/android_publishmood', Android_PublishMood),
                               ], debug=True)