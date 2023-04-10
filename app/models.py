from . import db
from flask import Flask, request

app = Flask(__name__)

class Movie(db.Model):

    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    description = db.Column(db.Text)
    poster_url = db.Column(db.String(255)) #Just in case the path is EXTRA long
    created_at = db.Column(db.DateTime)
