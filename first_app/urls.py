from django.conf.urls import url
from django.urls import path,re_path
from first_app import views


app_name = 'first_app'

urlpatterns=[
    path('',views.display_movie,name='display_movie'),
    path('search_movies/',views.search_movies,name='search_movies'),
    path('display_user_details/',views.display_user_details,name='display_user_details'),
    re_path(r'^watch_movie/*',views.watch_movie,name='watch_movie'),
]
