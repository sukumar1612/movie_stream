from django.conf.urls import url
from django.urls import path,re_path
from login_website import views

app_name = 'login_website'

urlpatterns=[
    path('user_login/',views.user_login,name='user_login'),
    path('register/',views.register,name='register'),
    path('user_logout/',views.user_logout,name='user_logout')
]
