# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialfeedsparser', '0005_auto_20160110_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='source',
            field=models.CharField(default=(b'twitter', b'Twitter'), max_length=50, verbose_name='Social media', choices=[(b'twitter', b'Twitter'), (b'instagram', b'Instagram')]),
        ),
    ]
