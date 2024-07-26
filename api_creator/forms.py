from django import forms
from .models import API

class APICreationForm(forms.ModelForm):
    class Meta:
        model = API
        fields = ['name', 'key']
