from pyexpat import model
from django.db import models

# Create your models here.

class Artiste(models, model):
    first_name = models.CharField()
    last_name = models.CharField()
    age = models.IntegerField()

class Song(models, model):
    title = models.CharField()
    date_released = models.IntegerField()
    likes = models.CharField()
    artiste_id = models.IntegerField()

class Lyrics(models, model):
    content = models.CharField()
    song_id = models.IntegerField()