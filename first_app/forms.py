from django import forms
from first_app.models import movies,Genre

class movie_form(forms.ModelForm):
    class Meta:
        model=movies
        fields=['movie_name','genre','movie_photo_actual','movie_video_actual']

class gnre(forms.ModelForm):
    class Meta:
        model=movies
        fields=['genre',]
