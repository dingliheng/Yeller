import webapp2
from models import JINJA_ENVIRONMENT

__author__ = 'yusun'

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('htmls/login.html')
        self.response.write(template.render())

