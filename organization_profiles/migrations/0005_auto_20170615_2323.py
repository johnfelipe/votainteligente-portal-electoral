# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-15 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization_profiles', '0004_create_extra_pages_for_all'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationtemplate',
            name='secondary_color',
            field=models.CharField(default='#2DDC22', max_length=8, verbose_name='Color secundario'),
        ),
    ]
