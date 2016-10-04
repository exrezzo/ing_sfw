from django.db import models

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
