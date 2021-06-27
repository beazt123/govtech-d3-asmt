from .database import db

class URL(db.Model):
    id = db.Column(db.Text, primary_key=True)
    originalUrl = db.Column(db.Text)