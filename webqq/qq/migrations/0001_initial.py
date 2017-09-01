# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QQGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u7fa4\u540d')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='\u6210\u5458')),
            ],
            options={
                'verbose_name': '\u7fa4\u7ec4',
                'verbose_name_plural': '\u7fa4\u7ec4',
            },
        ),
    ]
