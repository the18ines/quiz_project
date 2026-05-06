from django.db import models
from django.contrib.auth.models import AbstractUser

class Personne(AbstractUser):
    """ Table SQL classique — données stables """
    date_inscription = models.DateTimeField(auto_now_add=True)
    est_actif = models.BooleanField(default=True)

    class Meta:
        db_table = 'personne'

class Profil(models.Model):
    """ Profil utilisateur — SQL classique """
    personne = models.OneToOneField(Personne,
        on_delete=models.CASCADE,
        primary_key=True)
    pseudo = models.CharField(max_length=100, blank=True)
    score_total = models.IntegerField(default=0)
    nombre_questions_repondues = models.IntegerField(default=0)
    est_admin = models.BooleanField(default=False)

    class Meta:
        db_table = 'profil'
    def __str__(self):
        return f'{self.personne.username} ({self.pseudo})'
