# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worsttweet', '0003_auto_20151021_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favoriteworst',
            name='downvote_count',
        ),
    ]
