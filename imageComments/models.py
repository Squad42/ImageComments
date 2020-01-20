from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class ImageComments(db.Model):
    __tablename__ = "imagecomments"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    text = db.Column(db.String(200))
    img_uri = db.Column(db.String(100))
    created_datetime = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, username, text, img_uri, created_datetime):
        self.username = username
        self.text = text
        self.img_uri = img_uri
        self.created_datetime = datetime.datetime.strptime(created_datetime, "%Y-%m-%dT%H:%M:%SZ")
