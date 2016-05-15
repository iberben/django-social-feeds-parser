# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialfeedsparser', '0010_auto_20160121_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='language',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='Language', choices=[(b'nl', 'Dutch'), (b'en', 'English'), (b'fr', 'French'), (b'de', 'German'), (b'it', 'Italian'), (b'es', 'Spanish')]),
        ),
    ]
