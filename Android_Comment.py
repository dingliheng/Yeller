__author__ = 'Liheng'
from google.appengine.ext.webapp import blobstore_handlers
from models import Yeller
from models import User
from models import Comment
from google.appengine.api.images import get_serving_url
import webapp2
import json


class Android_Comment(blobstore_handlers.BlobstoreUploadHandler):

    def get(self):
        yeller_id = str(self.request.params.get('yeller_id'))
        yeller = Yeller.query(Yeller.key_id==yeller_id).fetch(1)[0]
        authors = []
        comments_content = []
        for comment in yeller.comment:
            getuser = User.query(User.email == comment.author).fetch(1)[0]
            authors.append(getuser.fullname)
            comments_content.append(comment.content)
        dictPassed = {'authors':authors,'comments':comments_content}
        jsonObj = json.dumps(dictPassed,sort_keys=True,indent=4, separators=(',', ': '))
        self.response.write(jsonObj)

    def post(self):
        yeller_id = str(self.request.params.get('yeller_id'))
        User_email = self.request.params.get("User_email")
        comment = self.request.params.get("comment")
        yeller = Yeller.query(Yeller.key_id==yeller_id).fetch(1)[0]
        new_comment = Comment(author = User_email)
        new_comment.content = comment
        new_comment_key = new_comment.put()
        yeller.comment.append(new_comment)
        yeller.put()

app = webapp2.WSGIApplication([
                               ('/android_comment', Android_Comment),
                               ], debug=True)