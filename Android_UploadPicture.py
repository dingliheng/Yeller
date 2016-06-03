__author__ = 'Liheng'

import webapp2
import datetime
from models import User
from models import Yeller
from models import Picture
from google.appengine.ext.webapp import blobstore_handlers


class Android_UploadPicture(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        User_email = self.request.params.get('User_email')
        current_user = User.query(User.email == User_email).fetch(1)[0]
        activity = self.request.params.get('activity')
        upload = self.get_uploads()[0]
        if activity == 'FeedPad':
            content = self.request.params.get('content')
            latitude = self.request.params.get("latitude")
            longitude = self.request.params.get("longitude")

            newyeller = Yeller(author=User_email)
            newyeller.text = content
            newyeller.latitude = float(latitude)
            newyeller.longitude = float(longitude)
            newyeller.to_whom='public'
            newyeller.Anonymity = False
            newyeller.pictures.append(Picture(blob_key=upload.key()))
            yeller_key = newyeller.put()
            newyeller.key_id = str(newyeller.key.id())
            newyeller.put()
            current_user.yellers_owned.append(yeller_key)
        else:
            current_user.head_portrait=upload.key()

        current_user.put()

app = webapp2.WSGIApplication([
    ('/android_UploadPicture', Android_UploadPicture),
], debug=True)
