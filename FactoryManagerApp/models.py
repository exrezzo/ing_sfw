from django.db import models

# Aggiungo dizionario per sesso
SESSO = (
    ('M', 'Maschio'),
    ('F', 'Femmina'),
)


# Create your models here.

# 'Mansione'
# @param nome: denominazione mansione eseguita dal Dipendente
class Mansione(models.Model):
    class Meta:
        verbose_name = 'Mansione'
        verbose_name_plural = 'Mansioni' \
                              ''

    nome = models.CharField(max_length=32)

    def __str__(self):
        return self.nome

# 'Dipendente'
# definizione attributi generici di dipendente
class Dipendente(models.Model):
    class Meta:
        verbose_name = 'Dipendente'
        verbose_name_plural = 'Dipendenti'

    nome = models.CharField(max_length=32)
    cognome = models.CharField(max_length=32)
    sesso = models.CharField(max_length=7, choices=SESSO)
    dataNascita = models.DateField()
    codiceFiscale = models.CharField(max_length=16)
    email = models.CharField(max_length=32)
    telefono = models.CharField(max_length=16)
    domicilio = models.CharField(max_length=32)
    mansione = models.ForeignKey(Mansione)

    def __str__(self):
        return self.nome

# Modello Ambiente di lavoro
class Ambiente(models.Model):
    class Meta:
        verbose_name = 'Ambiente'
        verbose_name_plural = 'Ambienti'

    nome = models.CharField(max_length=56)
    numeroFinestre = models.PositiveIntegerField(null=True)
    numeroPorte = models.PositiveIntegerField(null=True)
    numeroPiano = models.PositiveIntegerField(null=True)
    ubicazione = models.CharField(max_length=56)
    dipendenti = models.ManyToManyField(Dipendente)

    #   funzione che ritorna il nome dell'ambiente di lavoro
    def __str__(self):
        return self.nome


# creazione modello strumento con id_ambiente come attributo chiave esterna##
class Strumento(models.Model):
    class Meta:
        verbose_name = 'Strumento'
        verbose_name_plural = 'Strumenti'

    ambiente = models.ForeignKey(Ambiente, null=True, blank=True)
    nome = models.CharField(max_length=56)
    modello = models.CharField(max_length=56)
    marca = models.CharField(max_length=56)
    annoAcquisto = models.CharField(max_length=56, null=True, blank=True)
    tipologia = models.CharField(max_length=56)
    dipendenti = models.ManyToManyField ('Dipendente')

    def __str__(self):
        return self.nome+ ' ' + self.modello + ' ' + self.tipologia







# Associa un dipendente ad uno o piu luoghi di lavoro.
# class Lavora(models.Model):
#     class Meta:
#         unique_together = (('id_dipendente', 'id_ambiente'),)
#         verbose_name = 'Lavora'
#         verbose_name_plural = 'Lavorano'
#
#     id_dipendente = models.ForeignKey(Dipendente)
#     id_ambiente = models.ForeignKey(Ambiente)
#     postazioneFissa = models.BooleanField()
#
#     def __str__(self):
#         return self.id_ambiente.nomeAmbiente


# # Esprime l'assengazione degli strumenti ai dipendenti.
# class Utilizza(models.Model):
#     class Meta:
#         unique_together = (('id_dipendente', 'id_strumento'))
#         verbose_name = 'Utilizza'
#         verbose_name_plural = 'Utilizzano'
#
#     id_dipendente = models.ForeignKey(Dipendente)
#     id_strumento = models.ForeignKey(Strumento)
#
#     def __str__(self):
#         return self.id_dipendente.nome
