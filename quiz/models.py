from django.db import models
from django.contrib.postgres.fields import ArrayField
from accounts.models import Personne

class Categorie(models.Model):
    """ SQL + JSONB : libelle en SQL, config en JSONB """
    libelle = models.CharField(max_length=200)   # SQL
    date_creation = models.DateTimeField(auto_now_add=True)  # SQL
    createur = models.ForeignKey(Personne,       # SQL (FK)
        on_delete=models.CASCADE,
        related_name='categories_creees')
    # ↓ JSONB : configuration flexible de la catégorie
    structure_questions = models.JSONField(default=dict)
    # Exemple de valeur JSONB :
    # {'description': 'Quiz Python', 'difficulte': 'facile',
    #  'duree_minutes': 30, 'points_par_question': 1}

    class Meta:
        db_table = 'categorie'

    def __str__(self):
        return self.libelle

class Question(models.Model):
    """ SQL pour les métadonnées, JSONB pour le contenu flexible """
    categorie = models.ForeignKey(Categorie,     # SQL (FK)
        on_delete=models.CASCADE,
        related_name='questions')
    createur = models.ForeignKey(Personne,       # SQL (FK)
        on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)  # SQL
    points = models.IntegerField(default=1)      # SQL
    # ↓ JSONB : contenu flexible de la question
    contenu = models.JSONField()                  # JSONB ★
    # Exemple de valeur JSONB pour QCM :
    # {'texte': 'Qu est-ce que JSONB?',
    #  'type': 'qcm',
    #  'options': ['Type SQL','Type NoSQL','Type hybride','Aucun'],
    #  'reponse_correcte': 'Type hybride'}
    # Exemple pour vrai/faux :
    # {'texte': 'JSONB supporte les tableaux?', 'type': 'vrai_faux'}

    class Meta:
        db_table = 'question'

    def get_texte(self):
        return self.contenu.get('texte', 'Sans titre')

    def get_type(self):
        return self.contenu.get('type', 'libre')
