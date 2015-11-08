__author__ = 'yusun'
import os
import jinja2
from google.appengine.api import images
from collections import deque
from google.appengine.ext import ndb

count_queue = deque()

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
JINJA_ENVIRONMENT.filters['get_serving_url'] = images.get_serving_url

class Picture(ndb.Model):
    blob_key = ndb.BlobKeyProperty()

class Comment(ndb.Model):
    author = ndb.StringProperty()
    content = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

class Yeller(ndb.Model):
    title = ndb.StringProperty(indexed=True)
    author = ndb.StringProperty()
    text = ndb.TextProperty()
    pictures = ndb.StructuredProperty(Picture, repeated=True)
    date = ndb.DateTimeProperty(auto_now_add=True)
    longitude = ndb.FloatProperty()
    latitude = ndb.FloatProperty()
    comment = ndb.StructuredProperty(Comment, repeated=True)

class User(ndb.Model):
    email = ndb.StringProperty(indexed=True)
    identity = ndb.StringProperty(indexed=True)
    head_portrait = ndb.BlobKeyProperty(repeated=False)
    yellers_owned = ndb.StructuredProperty(Yeller, repeated=True)
    yellers_collect = ndb.StructuredProperty(Yeller, repeated=True)
    yellers_comment = ndb.StructuredProperty(Yeller, repeated=True)
    friends = ndb.KeyProperty(repeated = True)
    album = ndb.StructuredProperty(Picture, repeated=True)

