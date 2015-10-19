# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteWorst',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('twitter_id', models.CharField(blank=True, max_length=50)),
                ('upvote_count', models.IntegerField()),
                ('downvote_count', models.IntegerField()),
            ],
        ),
    ]
