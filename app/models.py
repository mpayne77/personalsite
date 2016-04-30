from app import app
from peewee import *
from playhouse.flask_utils import FlaskDB
import datetime
import re

flask_db = FlaskDB(app, 'mysql://mpayne77:@0.0.0.0:3306/c9')
#mysql_db = MySQLDatabase('c9', user='mpayne77')
mysql_db = flask_db.database

# class BaseModel(flask_db.Model):
#     class Meta:
#         database = mysql_db
        

class Blogpost(flask_db.Model):
    database = mysql_db
    title = CharField()
    slug = CharField(unique=True)
    thumbnail = CharField()
    content = TextField()
    published = BooleanField(index=True)
    timestamp = DateTimeField(default=datetime.datetime.now, index=True)
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = re.sub('[^\w]+', '-', self.title.lower())
        ret = super(Blogpost, self).save(*args, **kwargs)
        return ret
        


    

