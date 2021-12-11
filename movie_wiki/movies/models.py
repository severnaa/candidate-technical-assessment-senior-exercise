from django.db import models


class Movie(models.Model):
    name = models.Choices()
    released = models.DateField()
