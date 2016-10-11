from django.contrib import admin
from .models import Mansione
from .models import Ambiente
from .models import Dipendente
from .models import Strumento

# === Configurazione classi per la personalizzazione interfacce admin per FactoryManagerApp ===

# Classe AmbienteAdmin per l'amministrazione degli ambienti relativi all'azienda.
class AmbienteAdmin(admin.ModelAdmin):
    # Fornisce un'interfaccia utile alla ricerca delle relative chiavi esterne.
    filter_horizontal = ('dipendenti',)
    list_display = ('nome', 'ubicazione',)
    #Fornisce un'interfaccia per filtrare i dati.
    list_filter = ('ubicazione','numeroPiano','dipendenti',)

    # Visualizza gli strumenti presenti in quell'ambiente e i dipendenti associati a tale ambiente.
    fieldsets = [
        ('Ambiente', {'fields': ['nome', 'numeroFinestre', 'numeroPorte', 'numeroPiano', 'ubicazione', 'dipendenti']}),
    ]

    # Ordina e raggruppa i dati in base all'ubicazione.
    ordering = ('ubicazione',)
    search_fields = ('nome', 'ubicazione', )

#
#
# Classe StrumentoAdmin per l'amministrazione degli strumenti relativi all'azienda.
class StrumentoAdmin(admin.ModelAdmin):
    # Fornisce un'interfaccia utile alla ricerca delle relative chiavi esterne.
    filter_horizontal = ('dipendenti', )
    list_display = ('nome', 'marca', 'modello',)
    list_filter = ('marca','nome','dipendenti', 'ambiente')
    # Visualizza gli strumenti e i dipendenti ad essi associati
    fieldsets = [
        ('Strumento',
         {'fields': ['nome', 'modello', 'marca', 'ambiente', 'annoAcquisto', 'tipologia', 'dipendenti']}),
    ]
    # Ordina e raggruppa i dati in base a tipologia, marca e modello.
    ordering = ('tipologia', 'marca', 'modello',)
    search_fields = ('nome', 'marca', 'modello', 'tipologia', )

# Classe MansioneAdmin per l'amministrazione delle mansioni relative all'azienda.
class MansioneAdmin(admin.ModelAdmin):

    list_display = ('nome',)
    # Visualizza le mansioni
    fieldsets = [
        ('Mansione',
         {'fields': ['nome',]}),
    ]
    search_fields = ('nome',)

# Classe DipendenteAdmin per l'amministrazione dei dipendenti dell'azienda.
class DipendenteAdmin(admin.ModelAdmin):
    # Fornisce un'interfaccia utile alla ricerca delle relative chiavi esterne.
    list_filter = ('codiceFiscale', 'cognome', 'email', 'mansione', )
    list_display = ('nome','cognome','codiceFiscale',)
    fieldsets = [
        ('Dipendenti',
         {'fields': ['nome','cognome','sesso','dataNascita','codiceFiscale','email','telefono','domicilio','mansione',]})
    ]
    # Ordina e raggruppa i dati in base alla mansione svolta dal dipendente.
    ordering = ('mansione',)
    search_fields = ('nome', 'cognome', 'codiceFiscale', 'email', 'domicilio', )

# Registrazione dei modelli creati
admin.site.register(Mansione, MansioneAdmin)
admin.site.register(Ambiente, AmbienteAdmin)
admin.site.register(Dipendente, DipendenteAdmin)
admin.site.register(Strumento, StrumentoAdmin)

