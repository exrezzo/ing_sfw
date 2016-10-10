from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import *
from django.template import Context, loader

# === Viste per FactoryManagerApp ===

# Vista del report relativo alla descrizione generale dell'azienda, ovvero tutti i dipendenti, strumenti ed ambienti.
def schedaDescrittiva(request):
    # Context e' un dizionario Python le cui chiavi possono essere accedute nel template vista.html
    context = Context({
        'dipendenti': Dipendente.objects.all(),
        'strumenti': Strumento.objects.all(),
        'ambienti': Ambiente.objects.all(),
    })

    template = loader.get_template('vista.html')
    return HttpResponse(template.render(context))

# Vista del report relativo alla descrizione dei dipendenti.
def schedaDipendenti(request):
    # Context e' un dizionario Python le cui chiavi possono essere accedute nel template dipendenti.html
    context = Context({
        'dipendenti': Dipendente.objects.all(),

    })

    template = loader.get_template('dipendenti.html')
    return HttpResponse(template.render(context))


# Vista del report relativo alla descrizione degli ambienti.
def schedaAmbienti(request):
    # Context e' un dizionario Python le cui chiavi possono essere accedute nel template ambienti.html
    context = Context({
        'ambienti': Ambiente.objects.all(),

    })

    template = loader.get_template('ambiente.html')
    return HttpResponse(template.render(context))

# Vista del report relativo alla descrizione degli strumenti.
def schedaStrumenti(request):
    # Context e' un dizionario Python le cui chiavi possono essere accedute nel template strumenti.html
    context = Context({
        'strumenti': Strumento.objects.all(),
        'dipendenti': Dipendente.objects.all(),

    })

    template = loader.get_template('strumenti.html')
    return HttpResponse(template.render(context))
def documentazione (request):
    template = loader.get_template("/docs/models.html")
