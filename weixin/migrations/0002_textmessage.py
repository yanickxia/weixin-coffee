# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weixin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextMessage',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('to_user_name', models.CharField(max_length=100)),
                ('from_user_name', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField()),
                ('msg_type', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=50)),
                ('msg_id', models.CharField(max_length=20)),
            ],
        ),
    ]
