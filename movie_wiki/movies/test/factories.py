from datetime import date
from datetime import timedelta

from factory import Factory
from factory import Faker

from movies.models import Movie


class MovieFactory(Factory):
    class Meta:
        model = Movie

    name = Faker('Inception')
    released = date.now() - timedelta(years=2)