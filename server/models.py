from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Movie(db.Model, SerializerMixin):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    genre = db.Column(db.String)
    year = db.Column(db.Integer)

    def __repr__(self):
        return f'<Movie {self.title}>'
