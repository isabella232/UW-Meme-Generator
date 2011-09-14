#!/usr/bin/env python

# waterlol data models

import logging

from google.appengine.ext import db, webapp
from google.appengine.api import users

class Template(db.Model):
    """Model for storing meem templates"""
    uid = db.StringProperty()
    name = db.StringProperty()
    img = db.BlobProperty(default=None)
    thumb = db.BlobProperty(default=None)
