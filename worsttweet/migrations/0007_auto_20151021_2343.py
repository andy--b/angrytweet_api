# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worsttweet', '0006_auto_20151021_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoriteworst',
            name='upvote_count',
            field=models.IntegerField(db_index=True, default=1),
        ),
    ]
