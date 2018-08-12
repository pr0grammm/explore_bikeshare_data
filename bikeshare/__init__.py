#import constructor
from flask import Flask

#create Flask instance
app = Flask(__name__)
app.secret_key = 'topsecret'
from bikeshare import views
