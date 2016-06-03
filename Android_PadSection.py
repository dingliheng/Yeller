__author__ = 'Liheng'
from google.appengine.ext.webapp import blobstore_handlers
from models import User
import webapp2
import json

class Android_Register(blobstore_handlers.BlobstoreUploadHandler):
    def get(self):

        User_email = self.request.params.get("newUser_email")
        newUser_fullname = self.request.params.get("newUser_id")
        newUser_password = self.request.params.get("newUser_password")
        getUser = User.query(User.email == User_email)
        if getUser.fetch(1):
            dictPassed = {"newUser":"0"}
        else:
            dictPassed = {"newUser":"1"}
            newUser = User(identity=newUser_fullname, email=User_email, password=newUser_password)
            newUser.put()

        jsonObj = json.dumps(dictPassed, sort_keys=True, indent=4, separators=(',', ': '))
        self.response.write(jsonObj)
app = webapp2.WSGIApplication([
                               ('/android_register', Android_Register),
                               ], debug=True)