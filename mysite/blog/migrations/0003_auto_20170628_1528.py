# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170627_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='self_intro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
    ]
