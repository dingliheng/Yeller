__author__ = 'Liheng'
from google.appengine.ext.webapp import blobstore_handlers
from models import User
import webapp2
import json

class Android_Follow(blobstore_handlers.BlobstoreUploadHandler):
    def get(self):

        user_email = User_email = self.request.params.get("User_email")
        friend_name = self.request.params.get("friendname")
        getUser = User.query(User.email == User_email).fetch(1)[0]
        if friend_name in getUser.friends:
            pass
        else:
            getUser.friends.append(friend_name)
        getUser.put()

app = webapp2.WSGIApplication([
                               ('/android_follow', Android_Follow),
                               ], debug=True)