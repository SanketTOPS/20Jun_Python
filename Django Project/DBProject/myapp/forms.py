from django import forms
from .models import *

class studForm(forms.ModelForm):
    class Meta:
        model=studinfo
        fields='__all__'
        #fields=['name','email','dob','mobile','address']

class updateForm(forms.ModelForm):
    class Meta:
        model=studinfo
        fields=['name','email','dob','mobile']