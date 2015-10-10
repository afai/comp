# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20151004_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
