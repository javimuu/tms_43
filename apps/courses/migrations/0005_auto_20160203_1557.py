# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20160121_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[(b'open', b'Opening'), (b'close', b'Closed')], default=b'open', max_length=10),
        ),
    ]
