# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_contributor_asdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contributor',
            name='asdf',
        ),
        migrations.AddField(
            model_name='contributor',
            name='contents',
            field=models.ManyToManyField(related_name='contributor', to='content.Content'),
        ),
    ]
