from django.db import models
from accounts.models import Personne
from quiz.models import Question, Categorie
class Reponse(models.Model):
    """ Stocke les réponses en JSONB pour comparaison flexible """
    # Champs SQL classiques
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(Personne, on_delete=models.CASCADE)
    date_reponse = models.DateTimeField(auto_now_add=True)
    point_obtenu = models.IntegerField(default=0)
    est_correct = models.BooleanField(default=False)
    # Champs JSONB — cœur NoSQL
    reponse_donnee = models.JSONField()      # JSONB ★
    reponse_correcte = models.JSONField()    # JSONB ★
    # Exemple reponse_donnee : {'valeur': 'Type hybride'}
    # Exemple reponse_correcte: {'valeur': 'Type hybride'}

    class Meta:
        db_table = 'reponse'
        unique_together = [('question', 'utilisateur')]

class ScoreCategorie(models.Model):
    """ Résumé du score par catégorie — SQL classique """
    utilisateur = models.ForeignKey(Personne, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=0)
    date_passage = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'score_categorie'
