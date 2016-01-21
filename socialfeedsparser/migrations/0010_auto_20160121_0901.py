# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def _fill_in_repost(apps, schema_editor):
    model_Post = apps.get_model('socialfeedsparser', 'Post')

    for model in model_Post.objects.all():
        if model.content.startswith('RT'):
            model.repost = True
            model.save()


class Migration(migrations.Migration):

    dependencies = [
        ('socialfeedsparser', '0009_auto_20160121_0901'),
    ]

    operations = [
        migrations.RunPython(_fill_in_repost)
    ]
