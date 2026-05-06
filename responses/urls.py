from django.urls import path
from . import views

urlpatterns = [
    path('soumettre/<int:cat_id>/', views.soumettre_reponses, name='soumettre'),
    path('resultats/<int:cat_id>/', views.resultats, name='resultats'),
]