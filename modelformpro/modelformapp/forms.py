from django import forms
from .models import modelform

class Studentmodel(forms.ModelForm):
    class Meta:
        model = modelform
        fields = '__all__'
