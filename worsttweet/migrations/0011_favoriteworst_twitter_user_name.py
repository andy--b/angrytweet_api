# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worsttweet', '0010_auto_20151023_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoriteworst',
            name='twitter_user_name',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
