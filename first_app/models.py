from django.db import models
from django.contrib.auth.models import User

class movies(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=100, unique=True)
    movie_photo = models.CharField(max_length=300, unique=True)
    movie_video = models.CharField(max_length=300, unique=True)
    movie_photo_actual = models.ImageField(blank=True)
    movie_video_actual = models.FileField(blank=True)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.movie_name
# Create your models here.
