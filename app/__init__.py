from flask import Flask

'''
SECRET_KEY = '12345'
UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
'''

app = Flask(__name__)
app.config.from_object('config')

from app import views



