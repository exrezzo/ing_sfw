from django.db import models
## creazione modello strumento con id_ambiente come attributo chiave esterna##


class Strumento(models.Model):

        #id_ambiente = models.ForeignKey(Ambiente)
        nome_strumento = models.CharField(max_length=56)
        modello = models.CharField(max_length=56)
        marca = models.CharField(max_length=56)
        anno_acquisto = models.CharField(max_length=56)
        tipologia = models.CharField(max_length=56)

        def __str__(self):
            return self.modello + self.nome_strumento + self.marca



# Aggiungo dizionario per sesso
SESSO = (
    ('M' , 'Maschio'),
    ('F' , 'Femmina'),
)

# Create your models here.

# 'Mansione'
# @param nome: denominazione mansione eseguita dal Dipendente
class Mansione(models.Model):
    nome=models.CharField(max_length=32)

# 'Dipendente'
# definizione attributi generici di dipendente
class Dipendente(models.Model):
    nome = models.CharField(max_length=32)
    cognome = models.CharField(max_length=32)
    sesso = models.CharField(max_length=7, choices=SESSO)
    dataNascita = models.DateField()
    codiceFiscale = models.CharField(max_length=16)
    email = models.CharField(max_length=32)
    telefono = models.CharField(max_length=16)
    domicilio = models.CharField(max_length=32)
    idMansione = models.ForeignKey(Mansione)

# Modello Ambiente di lavoro
class Ambiente(models.Model):
    nomeAmbiente = models.CharField(max_length=56)
    numeroFinestre =  models.PositiveIntegerField(null=True)
    numeroPorte = models.PositiveIntegerField(null=True)
    numeroPiano = models.PositiveIntegerField(null=True)
    ubicazione = models.CharField(max_length=56, null=True)

#   funzione che ritorna il nome dell'ambiente di lavoro
    def __str__(self):
        return  self.nomeAmbiente

# Associa un dipendente ad uno o piu luoghi di lavoro.
class Lavora(models.Model):
    class Meta:
        unique_together = (('id_dipendente', 'id_ambiente'),)
    id_dipendente = models.ForeignKey(Dipendente)
    id_ambiente = models.ForeignKey(Ambiente)
    postazioneFissa = models.BooleanField()

# Esprime l'assengazione degli strumenti ai dipendenti.
class Utilizza(models.Model):
    class Meta:
        unique_together = (('id_dipendente', 'id_strumento'))
    id_dipendente = models.ForeignKey(Dipendente)
    id_strumento = models.ForeignKey(Strumento)
