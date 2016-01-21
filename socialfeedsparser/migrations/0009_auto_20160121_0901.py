# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialfeedsparser', '0008_post_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='language',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='Language', choices=[(b'nl', 'Dutch'), (b'fr', 'French'), (b'en', 'English')]),
        ),
        migrations.AddField(
            model_name='post',
            name='repost',
            field=models.BooleanField(default=False, verbose_name='Is repost'),
        ),
    ]
