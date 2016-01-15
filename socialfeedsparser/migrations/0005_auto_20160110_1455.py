# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialfeedsparser', '0004_auto_20151007_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='query_type',
            field=models.CharField(default=b'feed', help_text='Note: search is not applicable for Facebook.', max_length=10, verbose_name='Search for:', choices=[(b'feed', 'feed'), (b'search', 'search')]),
        ),
        migrations.AlterField(
            model_name='channel',
            name='source',
            field=models.CharField(default=(b'twitter', b'Twitter'), max_length=50, verbose_name='Social media', choices=[(b'twitter', b'Twitter')]),
        ),
    ]
