import webapp2
from models import JINJA_ENVIRONMENT

class AndroidUploadHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('htmls/login.html')
        self.response.write(template.render())
