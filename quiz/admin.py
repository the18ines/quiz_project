from django.contrib import admin
from .models import Categorie, Question

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['id', 'libelle', 'createur', 'date_creation']
    list_filter = ['createur']
    search_fields = ['libelle']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_texte', 'get_type', 'categorie', 'points'] 
    list_filter = ['categorie', 'createur']

    def get_texte(self, obj):
        # Accès au champ JSONB depuis l'admin
        return obj.contenu.get('texte', 'N/A')[:60]
    get_texte.short_description = 'Texte de la question'

    def get_type(self, obj):
        return obj.contenu.get('type', 'libre')
    get_type.short_description = 'Type'

# Register your models here.