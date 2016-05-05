from app import db


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    subtitle = db.Column(db.String(200))
    slug = db.Column(db.String(200))
    thumbnail = db.Column(db.Text)
    content = db.Column(db.Text)
    author = db.Column(db.String(100))
    timestamp = db.column(db.DateTime)
    
    def __str__(self):
        return self.title
    