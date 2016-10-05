from django.contrib import admin
from .models import *


#visualizzare gli strumenti
class StrumentiInLine(admin.TabularInline):
    model = Strumento
    extra = 2



class DipendenteUtilizzaInLine (admin.TabularInline):
    model = Utilizza
    extra = 3

class DipendenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cognome', 'idMansione', 'email')
    inlines = [DipendenteUtilizzaInLine]

    #Il sistema deve permettere di visualizzare gli ambienti associati ad un dipendente o a nessuno

class DipendenteLavoraInline (admin.TabularInline):
    model = Lavora
    extra = 2

#Visualizzazione ambiente di lavoro in admin
class AmbienteAdmin(admin.ModelAdmin):
    list_display = ('nomeAmbiente', 'ubicazione')
    fieldsets = [
        ('Ambiente',               {'fields': ['nomeAmbiente']}),
    ]
    inlines = [StrumentiInLine,DipendenteLavoraInline]
    ordering = ('ubicazione',)



# Register your models here.

admin.site.register(Strumento)
admin.site.register(Dipendente, DipendenteAdmin)
admin.site.register(Mansione)
admin.site.register(Lavora)
admin.site.register(Utilizza)
admin.site.register(Ambiente,AmbienteAdmin)
