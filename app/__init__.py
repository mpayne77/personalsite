from flask import Flask


SECRET_KEY = '12345'

app = Flask(__name__)

app.config.from_object(__name__)
from app import views, models


db = models.mysql_db

