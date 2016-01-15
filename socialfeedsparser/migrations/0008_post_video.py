# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialfeedsparser', '0007_post_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.URLField(max_length=255, null=True, verbose_name='Video', blank=True),
        ),
    ]
