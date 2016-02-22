__author__ = 'SWEN356 Team 4'

from flask import Flask

app = Flask(__name__)
app.secret_key = '\xa5\x8f\x19\xbb`$\xacw\x91\xe1\xd2\x896R\xf9\x14\x01\xe1\xd5U\xcc\xa9\x13'

from app import views
