from myapp import db
from datetime import datetime

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), index=True)
    body = db.Column(db.String(), index=True)
    url = db.Column(db.String(),nullable=True)
    comments = db.relationship('Comment', backref='com', lazy='dynamic')

    def __repr__(self):
        return self.title


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))

    def __repr__(self):
        return self.text
