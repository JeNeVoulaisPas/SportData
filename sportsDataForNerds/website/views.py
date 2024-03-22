from django.shortcuts import render

# Create your views here.

# Page d'acceuil #
def acceuil(request) :
    return render(request, "acceuil.html")