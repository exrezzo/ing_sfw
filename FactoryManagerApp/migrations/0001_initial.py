# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=56)),
                ('numeroFinestre', models.PositiveIntegerField(null=True)),
                ('numeroPorte', models.PositiveIntegerField(null=True)),
                ('numeroPiano', models.PositiveIntegerField(null=True)),
                ('ubicazione', models.CharField(max_length=56)),
            ],
            options={
                'verbose_name': 'Ambiente',
                'verbose_name_plural': 'Ambienti',
            },
        ),
        migrations.CreateModel(
            name='Dipendente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=32)),
                ('cognome', models.CharField(max_length=32)),
                ('sesso', models.CharField(max_length=7, choices=[(b'M', b'Maschio'), (b'F', b'Femmina')])),
                ('dataNascita', models.DateField()),
                ('codiceFiscale', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=32)),
                ('telefono', models.CharField(max_length=16)),
                ('domicilio', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'Dipendente',
                'verbose_name_plural': 'Dipendenti',
            },
        ),
        migrations.CreateModel(
            name='Mansione',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'Mansione',
                'verbose_name_plural': 'Mansioni',
            },
        ),
        migrations.CreateModel(
            name='Strumento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=56)),
                ('modello', models.CharField(max_length=56)),
                ('marca', models.CharField(max_length=56)),
                ('annoAcquisto', models.CharField(max_length=56, null=True, blank=True)),
                ('tipologia', models.CharField(max_length=56)),
                ('ambiente', models.ForeignKey(blank=True, to='FactoryManagerApp.Ambiente', null=True)),
                ('dipendenti', models.ManyToManyField(to='FactoryManagerApp.Dipendente')),
            ],
            options={
                'verbose_name': 'Strumento',
                'verbose_name_plural': 'Strumenti',
            },
        ),
        migrations.AddField(
            model_name='dipendente',
            name='mansione',
            field=models.ForeignKey(to='FactoryManagerApp.Mansione'),
        ),
        migrations.AddField(
            model_name='ambiente',
            name='dipendenti',
            field=models.ManyToManyField(to='FactoryManagerApp.Dipendente'),
        ),
    ]
