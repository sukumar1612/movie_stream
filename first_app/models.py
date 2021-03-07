from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.genre_name

class movies(models.Model):
    movie_name = models.CharField(max_length=100, primary_key=True)
    movie_photo = models.CharField(max_length=300, unique=True)
    movie_video = models.CharField(max_length=300, unique=True)
    movie_photo_actual = models.ImageField(blank=True)
    movie_video_actual = models.FileField(blank=True)
    genre = models.ManyToManyField(Genre)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.movie_name
# Create your models here.
