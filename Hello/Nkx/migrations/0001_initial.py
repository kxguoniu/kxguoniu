# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('status', models.BooleanField()),
                ('email', models.EmailField(max_length=254)),
                ('number', models.BigIntegerField()),
                ('text', models.TextField(null=True)),
                ('data', models.DateField()),
                ('time', models.DateTimeField()),
                ('num', models.DecimalField(max_digits=10, decimal_places=2)),
                ('file', models.FileField(upload_to=b'')),
            ],
        ),
    ]
