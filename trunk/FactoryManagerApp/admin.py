from django.contrib import admin
from .models import *
from django.forms import ModelForm
from suit.widgets import EnclosedInput


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
    search_fields = ('nome', 'ubicazione', )
#
#
#
class StrumentoAdmin(admin.ModelAdmin):
    filter_horizontal = ('dipendenti', )
    list_display = ('nome', 'marca', 'modello',)
    list_filter = ('marca','nome','dipendenti', 'ambiente')
    fieldsets = [
        ('Strumento',
         {'fields': ['nome', 'modello', 'marca', 'ambiente', 'annoAcquisto', 'tipologia', 'dipendenti']}),
    ]
    ordering = ('tipologia', 'marca', 'modello',)
    search_fields = ('nome', 'marca', 'modello', 'tipologia', )


class MansioneAdmin(admin.ModelAdmin):

    list_display = ('nome',)
    fieldsets = [
        ('Mansione',
         {'fields': ['nome',]}),
    ]
    search_fields = ('nome',)



class DipendenteAdmin(admin.ModelAdmin):
    list_filter = ('codiceFiscale', 'cognome', 'email', 'mansione', )
    list_display = ('nome','cognome','codiceFiscale',)
    fieldsets = [
        ('Dipendenti',
         {'fields': ['nome','cognome','sesso','dataNascita','codiceFiscale','email','telefono','domicilio','mansione',]})
    ]
    ordering = ('mansione',)
    search_fields = ('nome', 'cognome', 'codiceFiscale', 'email', 'domicilio', )
#
# # Register your models here.
#
# admin.site.register(Strumento,StrumentoAdmin)
# admin.site.register(Dipendente, DipendenteAdmin)
# admin.site.register(Mansione)
admin.site.register(Mansione, MansioneAdmin)
admin.site.register(Ambiente, AmbienteAdmin)
admin.site.register(Dipendente, DipendenteAdmin)
admin.site.register(Strumento, StrumentoAdmin)

