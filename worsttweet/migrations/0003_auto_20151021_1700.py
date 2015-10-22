# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worsttweet', '0002_auto_20151021_1516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favoriteworst',
            old_name='twitter_user',
            new_name='twitter_user_id',
        ),
    ]
