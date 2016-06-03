__author__ = 'Liheng'
from google.appengine.ext.webapp import blobstore_handlers
from models import User
from models import Yeller
from google.appengine.api.images import get_serving_url
import webapp2
import json

class Android_Nearby(blobstore_handlers.BlobstoreUploadHandler):
    def get(self):

        latitude = float(self.request.params.get("latitude"))
        longitude = float(self.request.params.get("longitude"))
        yellers = Yeller.query(Yeller.to_whom == "public", Yeller.Anonymity == True ).fetch(50)
        yellers = sorted(yellers, key=lambda  k: ((k.latitude-latitude)**2+(k.longitude-longitude)**2), reverse = False)
        yellers_key_ids = []
        for yeller in yellers:
            yellers_key_ids.append(yeller.key_id)
        dictPassed = {'yellers_key_ids':yellers_key_ids}
        jsonObj = json.dumps(dictPassed, sort_keys=True, indent=4, separators=(',', ': '))
        self.response.write(jsonObj)
app = webapp2.WSGIApplication([
                               ('/android_nearby', Android_Nearby),
                               ], debug=True)