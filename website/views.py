from django.shortcuts import render
from datetime import datetime, timedelta

# Importation des modèles
from .models import up_match

# Importation des fonctions de scraping
from website.scraping.upcoming_matches import get_upcoming_matches
from website.scraping.referee import get_referee
from website.scraping.meteo import get_weather

# Page d'acceuil #
def homePage(request) :

    #get_upcoming_matches("https://www.rugbypass.com/fixtures/")

    #get_referee('https://rugbyreferee.net/category/appointments/') 

    # Récupérer les 4 matchs les plus proches ordonnés par date puis par heure
    upcoming_matches = up_match.objects.all().order_by('date', 'hour')[:4]
    today_date = datetime.now().date()
    tomorrow_date = today_date + timedelta(days=1)

    # Récupérer les compétitions distinctes associées aux matchs et les trier par ordre alphabétique
    # Renvoie un tuple -> {'league': 'nom'} (dictionnaire)
    competitions_sorted = up_match.objects.values('league').distinct().order_by('league')

    # Passer les matchs récupérés au contexte du template
    context = {
        'upcoming_matches': upcoming_matches,
        'num_matches': len(upcoming_matches),  # Nombre de matchs récupérés
        'today_date' : today_date,
        'tomorrow_date' : tomorrow_date,
        'competitions_sorted' : competitions_sorted
    }

    return render(request, "homePage.html", context)


def leagues(request) :

    return render(request, "leagues.html")

def teams(request) :

    return render(request, "teams.html")

def matches(request) :

    return render(request, "matches.html")

def players(request) :

    return render(request, "players.html")
         
def contact(request) :

    return render(request, "contact.html")  

def imgSources(request) :

    return render(request, "imgSources.html")   

def urlSources(request) :

    return render(request, "urlSources.html")   