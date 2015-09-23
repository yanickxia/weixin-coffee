# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weixin', '0002_textmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadMedia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('type', models.CharField(max_length=10)),
                ('media_id', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
