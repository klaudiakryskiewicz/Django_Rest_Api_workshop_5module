from random import sample

import pytz
from faker import Faker

from moviebase.settings import TIME_ZONE
from movielist.models import Movie
from showtimes.models import Cinema, Screening

faker = Faker("pl_PL")
TZ = pytz.timezone(TIME_ZONE)


def random_movies():
    movies = list(Movie.objects.all())
    return sample(movies, 3)


def add_screenings(cinema):
    movies = random_movies()
    for movie in movies:
        Screening.objects.create(cinema=cinema, movie=movie, date=faker.date_time(tzinfo=TZ))


def fake_cinema_data():
    return {
        "name": faker.name(),
        "city": faker.city(),
    }


def create_fake_cinema():
    cinema = Cinema.objects.create(**fake_cinema_data())
    add_screenings(cinema)
