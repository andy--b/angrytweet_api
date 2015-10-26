# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worsttweet', '0009_favoriteworst_twitter_screen_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoriteworst',
            name='user_followers_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='favoriteworst',
            name='user_profile_pic_url',
            field=models.CharField(default='', max_length=100),
        ),
    ]
