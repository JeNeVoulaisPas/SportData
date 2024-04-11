from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.oauth2.views import OAuth2LoginView

def login_user(request) :
    if request.method == 'POST' :
            username = request.POST["username"]
            password = request.POST["password"]

            user = authenticate(request, username = username, password = password)
            
            if user != None : 
                login(request, user)
                return redirect("http://127.0.0.1:8000/")
            else :
                messages.info(request, "Incorrect login or password !")

    form = AuthenticationForm()

    return render(request, "login.html", {'form': form})
    

def logout_user(request) :
    logout(request)
    return redirect("http://127.0.0.1:8000/")

def signup_user(request) :
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('login')  # Rediriger vers la page de connexion après l'inscription
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})