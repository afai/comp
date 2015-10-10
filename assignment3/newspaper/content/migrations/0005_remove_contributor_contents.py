# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20151004_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contributor',
            name='contents',
        ),
    ]
