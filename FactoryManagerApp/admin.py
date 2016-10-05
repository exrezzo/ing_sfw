from django.contrib import admin
from .models import *


#visualizzare gli strumenti
class StrumentiInLine(admin.TabularInline):
    model = Strumento
    extra = 5

class AmbienteAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Ambiente',               {'fields': ['nomeAmbiente']}),
    ]
    inlines = [StrumentiInLine]




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
admin.site.register(Ambiente,AmbienteAdmin)
