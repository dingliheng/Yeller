__author__ = 'Liheng'
from google.appengine.ext.webapp import blobstore_handlers
from models import User
from models import Yeller
from models import Comment
from google.appengine.api.images import get_serving_url
import webapp2
import json

class Android_FindYeller(blobstore_handlers.BlobstoreUploadHandler):
    def get(self):
        yeller_id = str(self.request.params.get('yeller_id'))
        yeller = Yeller.query(Yeller.key_id==yeller_id).fetch(1)[0]
        author = yeller.author
        date = str(yeller.date)[:-10]
        content = yeller.text
        picture_urls = []
        for picture in yeller.pictures:
            picture_urls.append(get_serving_url(picture.blob_key, size=None, crop=False))
        user = User.query(User.email==author).fetch(1)[0]
        if yeller.Anonymity == True:
            anonymity = "true"
            fullname = "Anonymous"
        else:
            anonymity = "false"
            fullname = user.fullname
        if user.head_portrait != None:
            portrait_url = get_serving_url(user.head_portrait, size=None, crop=False)
        else:
            portrait_url = None
        dictPassed = {'fullname':fullname,"portrait_url":portrait_url,"date":date
                      ,"content":content,"picture_urls":picture_urls,"anonymity":anonymity}
        jsonObj = json.dumps(dictPassed,sort_keys=True,indent=4, separators=(',', ': '))
        self.response.write(jsonObj)

app = webapp2.WSGIApplication([
                               ('/android_findyeller', Android_FindYeller),
                               ], debug=True)