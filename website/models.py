from django.db import models

class up_match(models.Model):
    # Choix possibles pour le statut du match.
    # Chaque choix est une paire (valeur_en_base_de_données, étiquette_affichée).
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),      
        ('In progress', 'In progress'),  
        ('Finished', 'Finished'),   
        ('Cancelled', 'Cancelled'),   
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    team_home = models.CharField(max_length=100, null=True, blank=True)
    team_away = models.CharField(max_length=100, null=True, blank=True)
    score = models.CharField(max_length=20, null=True, blank=True)
    referee = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    hour = models.TimeField(null=True, blank=True)
    stade_name = models.CharField(max_length=100, null=True, blank=True)
    league = models.CharField(max_length=100, null=True, blank=True)
    phase = models.CharField(max_length=100, null=True, blank=True)