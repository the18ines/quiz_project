from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .models import Categorie, Question

def is_admin(user):
    return user.is_staff or user.is_superuser

@login_required
def liste_categories(request):
    categories = Categorie.objects.all().order_by('-date_creation')
    return render(request, 'quiz/categories.html',
                  {'categories': categories})

@login_required
def passer_quiz(request, cat_id):
    cat = get_object_or_404(Categorie, pk=cat_id)
    questions = cat.questions.all()
    return render(request, 'quiz/quiz.html',
                  {'categorie': cat, 'questions': questions})

@user_passes_test(is_admin)
def creer_categorie(request):
    if request.method == 'POST':
        libelle = request.POST.get('libelle')
        description = request.POST.get('description', '')
        diff = request.POST.get('difficulte', 'moyen')
        # Structure JSONB de la catégorie
        structure = {
            'description': description,
            'difficulte': diff,
            'points_par_question': 1,
        }
        Categorie.objects.create(
            libelle=libelle,
            createur=request.user,
            structure_questions=structure   # → stocké en JSONB
        )
        return redirect('liste_categories')
    return render(request, 'quiz/creer_categorie.html')

