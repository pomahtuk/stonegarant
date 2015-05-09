# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import stonegarant.models.attached_image
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stonegarant', '0002_auto_20150508_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachedimage',
            name='photo',
            field=models.FileField(upload_to=stonegarant.models.attached_image.upload_path_handler, null=True, verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
        ),
        migrations.AlterField(
            model_name='memorial',
            name='admin_thumb',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 9, 19, 40, 5, 853394), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
    ]
