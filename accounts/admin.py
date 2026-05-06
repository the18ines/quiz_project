from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Personne, Profil

class ProfilInline(admin.StackedInline):
    model = Profil
    can_delete = False
@admin.register(Personne)
class PersonneAdmin(UserAdmin):
    inlines = [ProfilInline]
    list_display = ['username', 'email', 'is_superuser', 'est_actif']


