from django.db import models
from phonenumber_field.modelfields import *

# === Modelli per FactoryManagerApp ===

# Dizionario per il sesso, ovvero per limitare le scelte possibili per il campo 'sesso' relativo ai dipendenti.
SESSO = (
    ('M', 'Maschio'),
    ('F', 'Femmina'),
)

class Mansione(models.Model):
    """
    La classe Mansione identifica le possibili mansioni ricopribili in una azienda.
    """
    class Meta:
        verbose_name = 'Mansione'
        verbose_name_plural = 'Mansioni' \
                              ''

    nome = models.CharField(max_length=32)

    #return: il nome della mansione
    def __str__(self):
        return self.nome



class Dipendente(models.Model):
    """
    La classe Dipendente identifica un dipendente all'interno di un'azienda.
    Gli attributi di classe specificano le caratteristiche possedute da un dipendente.
    """
    class Meta:
        verbose_name = 'Dipendente'
        verbose_name_plural = 'Dipendenti'

    nome = models.CharField(max_length=32)
    cognome = models.CharField(max_length=32)
    sesso = models.CharField(max_length=7, choices=SESSO)
    dataNascita = models.DateField()
    codiceFiscale = models.CharField(max_length=16)
    email = models.CharField(max_length=32)
    telefono = PhoneNumberField()
    domicilio = models.CharField(max_length=32)
    mansione = models.ForeignKey(Mansione)


    #return: codice fiscale, nome e cognome:
    #tali parametri identificano unicamente il soggetto nel database.
    def __str__(self):
     return  self.codiceFiscale + ' - ' + self.nome+' '+ self.cognome



class Ambiente(models.Model):
    """
    La classe Ambiente identifica un ambiente di lavoro, con le proprie caratteristiche interne ed il posizionamento
    all'interno dell'edificio aziendale, insieme ai dipendenti che vi lavorano all'interno di ognuno.
    """
    class Meta:
        verbose_name = 'Ambiente'
        verbose_name_plural = 'Ambienti'

    nome = models.CharField(max_length=56)
    numeroFinestre = models.PositiveIntegerField(null=True)
    numeroPorte = models.PositiveIntegerField(null=True)
    numeroPiano = models.PositiveIntegerField(null=True)
    ubicazione = models.CharField(max_length=56)
    dipendenti = models.ManyToManyField(Dipendente)

    #return: il nome dell'ambiente di lavoro
    def __str__(self):
        return self.nome + ' ' + str(self.ubicazione)


class Strumento(models.Model):
    """
    La classe Strumento identifica tutta la strumentazione presente all'interno di un'azienda, locazione, anagrafica
    dello strumento e a quali dipendenti e' stato assegnato.
    """

    class Meta:
        verbose_name = 'Strumento'
        verbose_name_plural = 'Strumenti'

    ambiente = models.ForeignKey(Ambiente, null=True, blank=True)
    nome = models.CharField(max_length=56)
    modello = models.CharField(max_length=56)
    marca = models.CharField(max_length=56)
    annoAcquisto = models.CharField(max_length=56, null=True, blank=True)
    tipologia = models.CharField(max_length=56)
    dipendenti = models.ManyToManyField ('Dipendente', blank=True)
    # return: il nome dello strumento, marca e modello
    def __str__(self):
        return self.nome + ' ' + str(self.marca)+ ' ' + str(self.modello)