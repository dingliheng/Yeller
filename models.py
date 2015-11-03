import os
import jinja2
from google.appengine.api import images
__author__ = 'yusun'

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
JINJA_ENVIRONMENT.filters['get_serving_url'] = images.get_serving_url

