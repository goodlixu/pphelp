# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-30 00:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggestion', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='group_info',
            name='subject',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='group_info',
            name='groups_info',
        ),
        migrations.AddField(
            model_name='group_info',
            name='groups_info',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
