# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pages',
            name='id',
        ),
        migrations.AlterField(
            model_name='pages',
            name='name',
            field=models.CharField(max_length=32, serialize=False, primary_key=True),
        ),
    ]
