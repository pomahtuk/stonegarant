# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stonegarant', '0008_auto_20150503_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='readywork',
            name='admin_thumb',
            field=easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to=b'uploads/ready', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 3, 16, 9, 2, 289035), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='readywork',
            name='photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'uploads/ready', null=True, verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
        ),
    ]
