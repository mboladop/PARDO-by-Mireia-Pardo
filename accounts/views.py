from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserLoginForm, UserRegistrationForm


# Create your views here.

def get_index(request):
    return render(request, "base.html")

def login(request):
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            u = login_form.cleaned_data['username']
            p = login_form.cleaned_data['password']
            user = authenticate(username=u, password=p)
    
            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                login_form.add_error(None, "Tu nombre de usuario (email) y/o contraseña no son correctos :(")
    else:
        login_form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': login_form})
    
def register(request):
    if request.method=="POST":
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            
            u = registration_form.cleaned_data['username']
            p = registration_form.cleaned_data['password1']
            user = authenticate(username=u, password=p)
            
            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                registration_form.add_error(None, "Login bloqueado, porfavor intentalo más tarde, lo sentimos :(")
    else:
        registration_form = UserRegistrationForm()
    
    
    return render(request, 'accounts/register.html', {'form': registration_form}),
    
def logout(request):
    auth.logout(request)
    return redirect('/')
    
def profile(request):
    return render(request, 'accounts/profile.html')