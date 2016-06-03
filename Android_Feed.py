__author__ = 'Liheng'
from google.appengine.ext.webapp import blobstore_handlers
from models import User
from models import Yeller
from google.appengine.api.images import get_serving_url
import webapp2
import json

class Android_Feed(blobstore_handlers.BlobstoreUploadHandler):
    def get(self):

        User_email = self.request.params.get("User_email")
        getUser = User.query(User.email == User_email).fetch(1)[0]
        friends = getUser.friends
        feed_list = []
        feed_list.append(getUser.email)
        for friend in friends:
            if User.query(User.fullname == friend).fetch(1):
                getfriend = User.query(User.fullname == friend).fetch(1)[0]
                feed_list.append(getfriend.email)
        yellers = Yeller.query(Yeller.to_whom == "public").fetch(50)
        for yeller in yellers[:]:
            if yeller.author not in feed_list:
                yellers.remove(yeller)
        yellers = sorted(yellers, key=lambda  k: k.date, reverse = True)
        yellers_key_ids = []
        for yeller in yellers:
            yellers_key_ids.append(yeller.key_id)
        dictPassed = {'yellers_key_ids':yellers_key_ids,"feed_list":feed_list}

        jsonObj = json.dumps(dictPassed, sort_keys=True, indent=4, separators=(',', ': '))
        self.response.write(jsonObj)
app = webapp2.WSGIApplication([
                               ('/android_feed', Android_Feed),
                               ], debug=True)