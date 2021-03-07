# Generated by Django 3.1.7 on 2021-03-07 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20210307_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='movie_photo_actual',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='movies',
            name='movie_video_actual',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='movies',
            name='movie_photo',
            field=models.CharField(max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='movie_video',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]
