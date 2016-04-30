from app import app
from peewee import *
import datetime

mysql_db = MySQLDatabase('c9', user='mpayne77')


class BaseModel(Model):
    class Meta:
        database = mysql_db
        

class Blogpost(BaseModel):
    title = CharField()
    slug = CharField(unique=True)
    thumbnail = CharField()
    content = TextField()
    published = BooleanField(index=True)
    timestamp = DateTimeField(default=datetime.datetime.now, index=True)
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = re.sub('[^\w]+', '-', self.title.lower())
        ret = super(Entry, self).save(*args, **kwargs)
        return ret
        


    

