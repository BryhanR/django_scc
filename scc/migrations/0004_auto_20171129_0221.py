# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 02:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scc', '0003_auto_20171129_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]