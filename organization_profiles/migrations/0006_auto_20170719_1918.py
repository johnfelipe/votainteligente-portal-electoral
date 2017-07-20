# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-19 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization_profiles', '0005_auto_20170615_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationtemplate',
            name='logo_small',
            field=models.ImageField(blank=True, null=True, upload_to='organizations/profiles_small/'),
        ),
        migrations.AlterField(
            model_name='organizationtemplate',
            name='logo',
            field=models.ImageField(blank=True, help_text='perrito', null=True, upload_to='organizations/profiles/', verbose_name='El logo de tu organizaci\xf3n'),
        ),
    ]