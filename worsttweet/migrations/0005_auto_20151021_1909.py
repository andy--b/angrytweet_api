# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worsttweet', '0004_remove_favoriteworst_downvote_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoriteworst',
            name='upvote_count',
            field=models.IntegerField(default=1, db_index=True),
        ),
    ]
