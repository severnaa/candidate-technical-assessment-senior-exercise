from datetime import date
from datetime import timedelta

import factory
from factory import Factory
from factory import Faker

from movies.test.factories import MovieFactory
from people.models import Person
from people.models import Role


class PersonFactory(Factory):
    class Meta:
        model = Person

    name = Faker('Jon Snow')
    born_on = date.now() - timedelta(years=30)


class RoleFactory(Factory):
    class Meta:
        model = Role

    movie = factory.SubFactory(MovieFactory)
    person = factory.SubFactory(PersonFactory)
    credit = Faker('Han Solo')
    on_screen = True


class ActorInOneMovieFactory(Factory):
    role = factory.RelatedFactory(
        RoleFactory,
        factory_related_name='person'
    )


class ActorInTwoMovieFactory(Factory):
    role1 = factory.RelatedFactory(
        RoleFactory,
        factory_related_name='person'
    )
    role2 = factory.RelatedFactory(
        RoleFactory,
        factory_related_name='person'
    )
