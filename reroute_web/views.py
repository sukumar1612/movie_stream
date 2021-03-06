from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

def rerout(request):
    return HttpResponseRedirect(reverse('login_website:user_login'))
# Create your views here.
