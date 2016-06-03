__author__ = 'Liheng'
import webapp2
from google.appengine.ext import blobstore
import json


class GetUploadUrl(webapp2.RequestHandler):
    def get(self):
        upload_url = blobstore.create_upload_url("/android_UploadPicture")
        # upload_url = str(upload_url)
        dictPassed = {'upload_url': upload_url}
        jsonObj = json.dumps(dictPassed, sort_keys=True, indent=4, separators=(',', ': '))
        self.response.write(jsonObj)


app = webapp2.WSGIApplication([
('/android_getUploadUrl', GetUploadUrl),
], debug=True)
