# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FactoryManagerApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strumento',
            name='dipendenti',
            field=models.ManyToManyField(to='FactoryManagerApp.Dipendente', null=True, blank=True),
        ),
    ]
