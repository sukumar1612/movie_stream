from django.shortcuts import render
from login_website.forms import UserForm,UserProfileInfoForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

from first_app.views import display_movie

def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('first_app:display_movie'))

        else:
            return HttpResponseRedirect(reverse('login_website:user_login'))
    else:
        return render(request,'lgin/login.html',{})
    #return render(request,'lgin/login.html',{'hello':'hello'})

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'lgin/register.html',{'registered':registered,'user_form':user_form,'profile_form':profile_form}  )


@login_required(login_url='/login_website/user_login')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_website:user_login'))
#return render(request,'lgin/register.html',{'hello':'hello'})


# Create your views here.
