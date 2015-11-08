__author__ = 'Liheng'
from google.appengine.ext.webapp import blobstore_handlers
from models import User
import webapp2

class Android_Register(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):

        newUser_id = self.request.params.get("user_id")
        newUser_email = self.request.params.get("email")
        newUser = User(identity = newUser_id,email = newUser_email)
        upload = self.get_uploads()[0]
        newUser.head_portrait = upload.key()
        newUser.album = []
        newUser.friends = []
        newUser.yellers_collect = []
        newUser.yellers_comment = []
        newUser.yellers_owned = []

        newUser.put()

app = webapp2.WSGIApplication([
                               ('/android_register', Android_Register),
                               ], debug=True)
