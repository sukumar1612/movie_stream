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

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from login_website.models import UserProfileInfo

@login_required(login_url='/login_website/user_login')
def watch_movie(request):
    user_details=request.user
    mvs=movies.objects.all()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.4.4", 80))
    local_ip = s.getsockname()[0]
    s.close()
    print("http://"+local_ip+":8000")
    p=urlparse(request.path_info)
    print(p.path)
    print(''.join((p.path).split('/first_app/watch_movie/')))
    dict={"insert_ip_addr":str("http://"+local_ip+":8000"+"/"+"".join((p.path).split('/first_app/watch_movie/'))),"movies":mvs,'user':user_details}
    return render(request,'first_app/index1.html',dict)

@login_required(login_url='/login_website/user_login')
def display_movie(request):
    user_details=request.user
    mvs=movies.objects.all()
    dct={'movies':mvs,'user':user_details}
    return render(request,'first_app/index.html',dct)

@login_required(login_url='/login_website/user_login')
def display_user_details(request):
    user_details = UserProfileInfo.objects.get(user=request.user)
    print(user_details.profile_pic.url)
    return render(request,'first_app/user_detail.html',{'user':request.user,'pic':user_details.profile_pic.url})

@login_required(login_url='/login_website/user_login')
def search_movies(request):
    user_details=request.user
    if request.method == "POST":
        search_value = request.POST.get('search')
        print(search_value)
        mvs=movies.objects.filter(movie_name__contains=search_value)
        dct={'movies':mvs,'user':user_details}
        return render(request,'first_app/search_stuff.html',dct)
    else:
        dct={'user':user_details}
        return render(request,'first_app/search_stuff.html',dct)
# Create your views here.
