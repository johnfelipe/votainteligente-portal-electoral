# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-05 23:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0029_candidate_has_won'),
        ('popular_proposal', '0018_popularproposal_join_advocacy_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='popularproposal',
            name='generated_at',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proposals_generated_here', to='elections.Area'),
        ),
    ]