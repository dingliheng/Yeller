__author__ = 'Liheng'
from google.appengine.ext.webapp import blobstore_handlers
from models import User
from models import Yeller
from google.appengine.api.images import get_serving_url
import webapp2
import json

class Android_SearchFriend(blobstore_handlers.BlobstoreUploadHandler):
    def get(self):

        if self.request.params.get("friend_name") != None:
            friendname = self.request.params.get("friend_name")
        else:
            friendname = self.request.params.get("search_name")

        users = User.query().fetch(50)
        for user in users:
            user_name = user.fullname
            lower_username = user_name.lower()
            friendname = friendname.lower()
            if lower_username == friendname:
                user_email = user.email
                if user.head_portrait != None:
                    portrait_url = get_serving_url(user.head_portrait, size=None, crop=False)
                else:
                    portrait_url = None
                yellers = Yeller.query(Yeller.author == user_email, Yeller.Anonymity == False).fetch(50)
                yellers = sorted(yellers, key=lambda k: k.date, reverse=True)
                content = yellers[0].text
                date = str(yellers[0].date)[:-10]
                dictPassed = {'isVaild': True, 'fullname': friendname, "portrait_url": portrait_url, "timestamp": date
                , "status": content}
                break
            else:
                dictPassed = {'isVaild':False}

        # if User.query(User.fullname == friendname).fetch(1):
        #     user = User.query(User.fullname == friendname).fetch(1)[0]
        #     username = user.fullname
        #     user_name = username.upper()
        #     user_email = user.email
        #     if user.head_portrait != None:
        #         portrait_url = get_serving_url(user.head_portrait, size=None, crop=False)
        #     else:
        #         portrait_url = None
        #     yellers = Yeller.query(Yeller.author == user_email, Yeller.Anonymity == False).fetch(50)
        #     yellers = sorted(yellers, key=lambda  k: k.date, reverse = True)
        #     content = yellers[0].text
        #     date = str(yellers[0].date)[:-10]
        #     dictPassed = {'isVaild':True,'fullname':friendname,"portrait_url":portrait_url,"timestamp":date
        #               ,"status":content,"up":user_name}
        # else:
        #     dictPassed = {'isVaild':False}

        jsonObj = json.dumps(dictPassed, sort_keys=True, indent=4, separators=(',', ': '))
        self.response.write(jsonObj)

app = webapp2.WSGIApplication([
                               ('/android_searchfriend', Android_SearchFriend),
                               ], debug=True)