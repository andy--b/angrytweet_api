# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worsttweet', '0008_auto_20151021_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoriteworst',
            name='twitter_screen_name',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
