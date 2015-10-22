# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worsttweet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favoriteworst',
            old_name='twitter_id',
            new_name='tweet_id',
        ),
        migrations.AddField(
            model_name='favoriteworst',
            name='search_term',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='favoriteworst',
            name='tweet_text',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='favoriteworst',
            name='twitter_user',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='favoriteworst',
            name='downvote_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='favoriteworst',
            name='upvote_count',
            field=models.IntegerField(default=1),
        ),
    ]
