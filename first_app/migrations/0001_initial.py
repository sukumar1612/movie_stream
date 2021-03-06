# Generated by Django 3.1.7 on 2021-03-02 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('movie_name', models.CharField(max_length=30, unique=True)),
                ('movie_photo', models.CharField(max_length=300, unique=True)),
                ('movie_video', models.CharField(max_length=300, unique=True)),
            ],
        ),
    ]