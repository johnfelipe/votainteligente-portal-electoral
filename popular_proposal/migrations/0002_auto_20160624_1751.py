# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-24 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popular_proposal', '0001_squashed_0014_popularproposal_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposaltemporarydata',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='proposaltemporarydata',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
