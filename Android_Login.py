__author__ = 'Liheng'
import webapp2
from models import User
import json

class Android_Login(webapp2.RequestHandler):
    def get(self):
        user_email = self.request.params.get("email")
        dictPassed = {}
        if User.query(User.email == user_email):
            dictPassed = {"newUser":0}
        else:
            dictPassed = {"newUser":1}
        jsonObj = json.dumps(dictPassed,sort_keys=True,indent=4, separators=(',', ': '))
        self.response.write(jsonObj)

app = webapp2.WSGIApplication([
                               ('/android_login', Android_Login),
                               ], debug=True)