from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db=SQLAlchemy()

class post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80),nullable=False)
    author = db.Column(db.String(80),nullable=False)
    content = db.Column(db.String(80),nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    def serialize(self):
        return{
            'id':self.id,
            'author':self.author,
            'content':self.content,
            'title':self.title,
            'date_posted':self.date_posted.strftime('%Y-%m-%d %H:%M:%S')
        }