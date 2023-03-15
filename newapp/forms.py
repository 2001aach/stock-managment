from django import forms
from django.contrib.auth.forms import UserCreationForm

from newapp.models import Login, stock


class loginform(UserCreationForm):
    class Meta:
        model=Login
        fields=('username','password1','password2','name','phonenumber','address')

class stockform(forms.ModelForm):
    class Meta:
        model=stock
        fields=('__all__')


