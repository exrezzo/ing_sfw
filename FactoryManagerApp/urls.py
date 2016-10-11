from django.conf.urls import url

from . import views
# === Configurazione URLS per FactoryManagerApp ===
urlpatterns = [
    # url che porta alla scheda descrittiva del database
    url(r'^schedadescrittiva/', views.schedaDescrittiva , name='test'),
    # url che porta alla scheda descrittiva dei dipendenti
    url(r'^dipendenti/', views.schedaDipendenti , name='dip'),
    # url che porta alla scheda descrittiva degli ambienti
    url(r'^ambienti/', views.schedaAmbienti , name='space'),
    # url che porta alla scheda descrittiva degli strumenti
    url(r'^strumenti/', views.schedaStrumenti , name='tools'),
    # url che permette di scaricare il pdf del report completo
    url(r'^schedapdf/', views.pdf_view , name='schedapdf'),
]