__author__ = 'Liheng'
from google.appengine.ext.webapp import blobstore_handlers
from models import User
from models import Yeller
from google.appengine.api.images import get_serving_url
import webapp2
import json

class Android_FriendPage(blobstore_handlers.BlobstoreUploadHandler):
    def get(self):

        User_name = self.request.params.get("User_name")
        user = User.query(User.fullname == User_name).fetch(1)[0]
        yellers = Yeller.query(Yeller.author == user.email, Yeller.Anonymity == False).fetch(50)
        yellers = sorted(yellers, key=lambda  k: k.date, reverse = True)
        yellers_key_ids = []
        for yeller in yellers:
            yellers_key_ids.append(yeller.key_id)
        dictPassed = {'yellers_key_ids':yellers_key_ids}
        jsonObj = json.dumps(dictPassed, sort_keys=True, indent=4, separators=(',', ': '))
        self.response.write(jsonObj)
app = webapp2.WSGIApplication([
                               ('/android_friendpage', Android_FriendPage),
                               ], debug=True)