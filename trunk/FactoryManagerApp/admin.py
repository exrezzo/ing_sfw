from django.contrib import admin
from .models import *


# #visualizzare gli strumenti
# class StrumentiInLine(admin.TabularInline):
#     model = Strumento
#     extra = 2
#
#
#
#
# class DipendenteAdmin(admin.ModelAdmin):
#     list_display = ('nome', 'cognome', 'idMansione', 'email')
#     #inlines = [DipendenteUtilizzaInLine,DipendenteLavoraInline]
#
#     #Il sistema deve permettere di visualizzare gli ambienti associati ad un dipendente o a nessuno
#
#
#
# #  Visualizzazione ambiente di lavoro in admin

class AmbienteAdmin(admin.ModelAdmin):
    filter_horizontal = ('dipendenti',)
    list_display = ('nome', 'ubicazione')
    fieldsets = [
        ('Ambiente', {'fields': ['nome', 'numeroFinestre', 'numeroPorte', 'numeroPiano', 'ubicazione', 'dipendenti']}),
    ]
        #sono visualizzati gli strumenti presenti in quell'ambiente e i dipendenti associati a tale ambiente

    ordering = ('ubicazione',)
#
#
#
class StrumentoAdmin(admin.ModelAdmin):
    filter_horizontal = ('dipendenti', )
    list_display = ('nome', 'marca', 'modello',)
    fieldsets = [
        ('Strumento',
         {'fields': ['nome', 'modello', 'marca', 'ambiente', 'annoAcquisto', 'tipologia', 'dipendenti']}),
    ]
    ordering = ('tipologia', 'marca', 'modello',)


class MansioneAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    fieldsets = [
        ('Mansione',
         {'fields': ['nome',]}),
    ]


class DipendenteAdmin(admin.ModelAdmin):

    list_display = ('nome','cognome','codiceFiscale',)
    fieldsets = [
        ('Dipendenti',
         {'fields': ['nome','cognome','sesso','dataNascita','codiceFiscale','email','telefono','domicilio','mansione',]})
    ]
    ordering = ('mansione',)
#
# # Register your models here.
#
# admin.site.register(Strumento,StrumentoAdmin)
# admin.site.register(Dipendente, DipendenteAdmin)
# admin.site.register(Mansione)
admin.site.register(Mansione,MansioneAdmin)
admin.site.register(Ambiente, AmbienteAdmin)
admin.site.register(Dipendente, DipendenteAdmin)
admin.site.register(Strumento, StrumentoAdmin)

