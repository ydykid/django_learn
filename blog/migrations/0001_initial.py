# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=256)),
                ('content', models.TextField(verbose_name='content')),
                ('pub_date', models.DateTimeField(verbose_name='publish-time', auto_now_add=True)),
                ('update_date', models.DateTimeField(verbose_name='update-time', null=True, auto_now=True)),
            ],
        ),
    ]
