# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stonegarant', '0007_auto_20150503_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='memorial',
            name='admin_thumb',
            field=easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to=b'uploads/memorials', blank=True),
        ),
        migrations.AlterField(
            model_name='memorial',
            name='photo1',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'uploads/memorials', null=True, verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 1', blank=True),
        ),
        migrations.AlterField(
            model_name='memorial',
            name='photo2',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'uploads/memorials', null=True, verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 2', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 3, 14, 31, 36, 409017), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
    ]
