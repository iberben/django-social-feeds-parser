# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialfeedsparser', '0003_channel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='name',
            field=models.CharField(default=b'', help_text='This will be used as author name for facebook fan pages.', max_length=100, verbose_name="Channel's name", blank=True),
        ),
        migrations.AlterField(
            model_name='channel',
            name='source',
            field=models.CharField(default=(b'twitter', b'Twitter'), max_length=50, verbose_name='Social media', choices=[(b'twitter', b'Twitter'), (b'facebook', b'Facebook'), (b'instagram', b'Instagram')]),
        ),
    ]
