# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialfeedsparser', '0006_auto_20160110_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='avatar',
            field=models.ImageField(upload_to=b'socialfeedsparser/avatars', null=True, verbose_name='Avatar', blank=True),
        ),
    ]
