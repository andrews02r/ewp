# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 00:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0008_auto_20171204_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledprogram',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programs.Program'),
        ),
    ]
