# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stonegarant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memorial',
            name='discount',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\xa1\xd0\xbe \xd1\x81\xd0\xba\xd0\xb8\xd0\xb4\xd0\xba\xd0\xbe\xd0\xb9'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 1, 12, 15, 44, 817710), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
    ]
