from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_categories, name='liste_categories'),
    path('quiz/<int:cat_id>/', views.passer_quiz, name='passer_quiz'),
    path('admin/creer/', views.creer_categorie, name='creer_categorie'),
]