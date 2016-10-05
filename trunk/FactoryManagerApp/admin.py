from django.contrib import admin
from .models import *

class DipendenteUtilizzaInLine (admin.TabularInline):
    model = Utilizza
    extra = 3

class DipendenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cognome', 'idMansione', 'email')
    inlines = [DipendenteUtilizzaInLine]




# Register your models here.

admin.site.register(Strumento)
admin.site.register(Dipendente, DipendenteAdmin)
admin.site.register(Mansione)
admin.site.register(Lavora)
admin.site.register(Utilizza)
admin.site.register(Ambiente)
