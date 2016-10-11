import StringIO

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from xhtml2pdf import pisa

from .models import Strumento
from .models import Ambiente
from .models import Dipendente
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


def html_view(request, as_pdf=False):
    # Get varaibles to populate the template
    payload = {'dipendenti': Dipendente.objects.all(),
               'strumenti': Strumento.objects.all(),
               'ambienti': Ambiente.objects.all(), }
    if as_pdf:
        return payload
    return render_to_response('topdf.html', payload, RequestContext(request))


def pdf_view(request):
    payload = html_view(request, as_pdf=True)
    file_data = render_to_string('topdf.html', payload, RequestContext(request))
    myfile = StringIO.StringIO()
    pisa.CreatePDF(file_data, myfile)
    myfile.seek(0)
    response = HttpResponse(myfile, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=report.pdf'
    return response
