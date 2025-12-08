from django import forms
from .models import Moviesed

class MoviesedForm(forms.ModelForm):
    class Meta:
        model = Moviesed
        fields = "__all__"
