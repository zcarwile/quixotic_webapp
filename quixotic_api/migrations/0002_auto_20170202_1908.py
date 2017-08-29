# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 19:08
from __future__ import unicode_literals

from django.db import migrations, models

def populate_user(apps, schema_editor):
    User = apps.get_model("quixotic_api", "User")
    u = User(name="zcarwile")
    u.save()

class Migration(migrations.Migration):

    dependencies = [
        ('quixotic_api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_user),
    ]
