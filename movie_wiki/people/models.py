from django.db import models


class Person(models.Model):
    name = models.CharField()
    born_on = models.DateField()
    died_on = models.DateField(null=True)
    movies = models.ManyToManyField('movies.Movie', through='Role')

    def __str__(self):
        return self.name


class Role(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE)
    credit = models.CharField(max_length=200)
    on_screen = models.BooleanField()
