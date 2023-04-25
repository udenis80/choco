from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserOurRegistration(UserCreationForm):
    email = forms.EmailField(required=True) #обязательное поле, если фолс, то не обязательное
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
