from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from quiz.models import Categorie, Question
from .models import Reponse, ScoreCategorie
from accounts.models import Profil

@login_required
def soumettre_reponses(request, cat_id):
    if request.method != 'POST':
        return redirect('liste_categories')

    cat = get_object_or_404(Categorie, pk=cat_id)
    questions = cat.questions.all()
    score = 0
    total = questions.count()

    for question in questions:
        # Récupérer la réponse de l'utilisateur depuis le formulaire
        valeur_user = request.POST.get(f'q_{question.id}', '')

        # Extraire la bonne réponse depuis le champ JSONB 'contenu'
        bonne_reponse = question.contenu.get('reponse_correcte', '')

        # Comparaison (insensible à la casse)
        est_correct = (valeur_user.strip().lower() ==
                       str(bonne_reponse).strip().lower())
        pts = question.points if est_correct else 0
        score += pts

        # Sauvegarder la réponse en JSONB
        Reponse.objects.update_or_create(
            question=question,
            utilisateur=request.user,
            defaults={
                'reponse_donnee': {'valeur': valeur_user},    # JSONB ★
                'reponse_correcte': {'valeur': bonne_reponse}, # JSONB ★
                'est_correct': est_correct,
                'point_obtenu': pts,
            }
        )

    # Sauvegarder le score de cette catégorie
    ScoreCategorie.objects.update_or_create(
        utilisateur=request.user, categorie=cat,
        defaults={'score': score, 'total_questions': total}
    )

    # Mettre à jour le score total du profil
    profil, _ = Profil.objects.get_or_create(personne=request.user)
    total_score = ScoreCategorie.objects.filter(
        utilisateur=request.user).aggregate(Sum('score'))['score__sum'] or 0
    profil.score_total = total_score
    profil.save()

    return redirect('resultats', cat_id=cat_id)

@login_required
def resultats(request, cat_id):
    cat = get_object_or_404(Categorie, pk=cat_id)
    reponses = Reponse.objects.filter(
        utilisateur=request.user,
        question__categorie=cat
    ).select_related('question')
    score_cat = ScoreCategorie.objects.filter(
        utilisateur=request.user, categorie=cat).first()
    from django.db.models import Sum
    score_max = cat.questions.aggregate(Sum('points'))['points__sum'] or 0

    return render(request, 'responses/resultats.html', {
        'categorie': cat,
        'reponses':  reponses,
        'score':     score_cat,
        'score_max': score_max,   # ← ex: 25 si tu as 5 questions à 5pts
    })
