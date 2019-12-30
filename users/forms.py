from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CreateUser(forms.Form):
    username = forms.CharField(label='Username',max_length=16)
    email = forms.EmailField(label='Email')
    password_1 = forms.CharField(label='Password',max_length=16,widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password',max_length=16, widget=forms.PasswordInput)
    name = forms.CharField(label='Name',max_length=16)
    last_name = forms.CharField(label='Last Name', max_length=16)
    information = forms.CharField(label='Description',required=False)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password',max_length=16,widget=forms.PasswordInput)
