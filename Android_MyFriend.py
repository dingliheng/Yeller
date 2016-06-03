__author__ = 'Liheng'
from google.appengine.ext.webapp import blobstore_handlers
from models import User
from models import Yeller
from google.appengine.api.images import get_serving_url
import webapp2
import json

class Android_MyFriend(blobstore_handlers.BlobstoreUploadHandler):
    def get(self):

        User_email = self.request.params.get("User_email")
        user = User.query(User.email == User_email).fetch(1)[0]
        friendlist = user.friends
        dictPassed = {'friendlist':friendlist}
        jsonObj = json.dumps(dictPassed, sort_keys=True, indent=4, separators=(',', ': '))
        self.response.write(jsonObj)

app = webapp2.WSGIApplication([
                               ('/android_myfriend', Android_MyFriend),
                               ], debug=True)