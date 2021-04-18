import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from level1.settings import STATIC_DIR
from django.http import StreamingHttpResponse
import os
import socket
from first_app.models import movies
from urllib.parse import urlparse

from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from login_website.models import UserProfileInfo
from first_app.forms import movie_form, gnre
from first_app.models import Genre, movies

from login_website import models
from django.db.models.signals import post_save
x = []


def ack(sender, **kwargs):
    if kwargs['created']:
        x.append(str(kwargs['instance']))


post_save.connect(ack, sender=models.User)


@login_required(login_url='/login_website/user_login')
def watch_movie(request):
    user_details = request.user
    mvs = movies.objects.all()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.4.4", 80))
    local_ip = s.getsockname()[0]
    s.close()
    print("http://"+local_ip+":8000")
    p = urlparse(request.path_info)
    print(p.path)
    print(''.join((p.path).split('/first_app/watch_movie/')))
    dict = {"insert_ip_addr": str("http://"+local_ip+":8000"+"/"+"".join(
        (p.path).split('/first_app/watch_movie/'))), "movies": mvs, 'user': user_details}
    return render(request, 'first_app/index1.html', dict)


@login_required(login_url='/login_website/user_login')
def display_movie(request):
    user_details = request.user
    mvs = movies.objects.all()
    dct = {'movies': mvs, 'user': user_details}

    if str(dct['user'].username) in x:
        x.remove(str(dct['user'].username))
        dct['user'].username = "welcome new user !!"

    return render(request, 'first_app/index.html', dct)


@login_required(login_url='/login_website/user_login')
def display_user_details(request):
    user_details = UserProfileInfo.objects.get(user=request.user)
    print(user_details.profile_pic.url)
    return render(request, 'first_app/user_detail.html', {'user': request.user, 'pic': user_details.profile_pic.url})


def remove_html(x):
    x = str(x)
    x = x.split("</option>")
    x = ''.join(x)
    x = x.split("<option value=")
    x = ''.join(x)
    x = x.split("\n\n")
    x1 = []
    for i in x:
        if("selected" in i):
            x1.append(i.split("selected>")[0])
    print(x1)
    x1 = ''.join(x1)
    x1 = x1.split(' ')
    x1 = ''.join(x1)
    x1 = x1.split('"')
    print(x1)
    x2 = []
    num = [str(i) for i in range(0, 100)]
    for i in x1:
        if(i in num):
            x2.append(int(i))
    print(x2)
    return x2


@login_required(login_url='/login_website/user_login')
def search_movies(request):
    user_details = request.user
    genre_mov = gnre()

    if request.method == "POST":
        search_value = request.POST.get('search')
        genre_mov = gnre(request.POST)

        x1 = remove_html(genre_mov['genre'])
        mvs = movies.objects.filter(
            movie_name__contains=search_value, genre__in=x1)
        dct = {'genre': genre_mov, 'movies': mvs, 'user': user_details}
        return render(request, 'first_app/search_stuff.html', dct)
    else:
        dct = {'genre': genre_mov, 'user': user_details}
        return render(request, 'first_app/search_stuff.html', dct)


@login_required(login_url='/login_website/user_login')
def fav(request):
    user_details = request.user
    if request.method == "POST":
        mvname = request.POST.get('mvname')
        mvs = movies.objects.get(movie_name=mvname)
        mvs.user.add(user_details)
        mvs.save()
    mvs = movies.objects.filter(user=user_details)
    dct = {'movies': mvs, 'user': user_details}
    return render(request, 'first_app/favourite.html', dct)


@login_required(login_url='/login_website/user_login')
def unfav(request):
    user_details = request.user
    if request.method == "POST":
        mvname = request.POST.get('mvname')
        mvs = movies.objects.get(movie_name=mvname)
        mvs.user.remove(user_details)
        mvs.save()
    mvs = movies.objects.filter(user=user_details)
    dct = {'movies': mvs, 'user': user_details}
    return render(request, 'first_app/favourite.html', dct)


@login_required(login_url='/login_website/user_login')
def upload_movie(request):
    registered = False
    user_details = request.user
    if request.method == "POST":
        mv = movie_form(request.POST, request.FILES)

        if mv.is_valid():
            movie = mv.save(commit=False)
            movie.movie_photo_actual = request.FILES['movie_photo_actual']
            movie.movie_video_actual = request.FILES['movie_video_actual']
            print(movie.movie_video_actual.url.split('/media/')[1])
            movie.movie_photo = movie.movie_photo_actual.url.split(
                '/media/')[1]
            movie.movie_video = movie.movie_video_actual.url.split(
                '/media/')[1]
            movie.save()
            x1 = remove_html(mv['genre'])
            for i in x1:
                movie.genre.add(Genre.objects.get(genre_id=i))

            registered = True

        else:
            print(mv.errors)
    else:
        mv = movie_form()

    dct = {'registered': registered, 'movies': mv, 'user': user_details}
    return render(request, 'first_app/upload_movie.html', dct)


# Create your views here.
