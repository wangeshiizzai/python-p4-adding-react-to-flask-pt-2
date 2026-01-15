#!/usr/bin/env python3

from random import choice, randint
from faker import Faker

from app import app
from models import db, Movie

fake = Faker()

GENRES = ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Romance']

def make_movies():
    # Clear existing movies
    Movie.query.delete()

    movies = []
    for _ in range(50):
        movie = Movie(
            title=fake.sentence(nb_words=4).title(),
            genre=choice(GENRES),
            year=randint(1980, 2025)
        )
        movies.append(movie)

    db.session.add_all(movies)
    db.session.commit()
    print("50 movies added to the database!")

if __name__ == '__main__':
    with app.app_context():
        make_movies()
