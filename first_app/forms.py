from django import forms
from first_app.models import movies

class movie_form(forms.ModelForm):
    class Meta:
        model=movies
        fields=['movie_name','movie_photo_actual','movie_video_actual']
