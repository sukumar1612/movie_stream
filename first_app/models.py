from django.db import models


class movies(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=100, unique=True)
    movie_photo = models.CharField(max_length=300, unique=True)
    movie_video = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.movie_name
# Create your models here.
