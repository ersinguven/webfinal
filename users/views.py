from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from .models import CustomUser
from .forms import CreateUser, LoginForm
from django import forms

def create_user(request):

    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password_1 = form.cleaned_data['password_1']
            password_2 = form.cleaned_data['password_2']
            if password_1 and password_2 and password_1 != password_2:
                raise forms.ValidationError("Passwords don't match")
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            information = form.cleaned_data['information']
            new_user = CustomUser(email=email,
                       username=username,
                       password=password_1,
                       name=name,
                       last_name=last_name,
                       info=information)
            new_user.save()
            return HttpResponseRedirect('/users/login')
    else:
            form = CreateUser()
    return render(request, 'createUser.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                valid = CustomUser.objects.filter(email=email)
            except:
                raise forms.ValidationError("Incorrect Email or Password")
            valid_password = valid.password
            if password == valid_password:
                return HttpResponseRedirect('/')

        else:
            form = LoginForm()

        return render(request,'login.html',{'form':form})

