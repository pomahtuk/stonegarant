# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stonegarant', '0005_auto_20150505_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='memorial',
            name='photo3',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'uploads/memorials', null=True, verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 3', blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='cvetnik',
            field=models.ForeignKey(default=1, verbose_name=b'\xd0\xa6\xd0\xb2\xd0\xb5\xd1\x82\xd0\xbd\xd0\xb8\xd0\xba', to='stonegarant.Cvetnik'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='notes',
            field=models.TextField(null=True, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xbc\xd0\xb5\xd1\x87\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f', blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.CharField(default=1, unique=True, max_length=150, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='order_pin',
            field=models.CharField(default=1, max_length=150, verbose_name=b'\xd0\x9f\xd0\x98\xd0\x9d-\xd0\xba\xd0\xbe\xd0\xb4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='podstavka',
            field=models.ForeignKey(default=1, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xb4\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb0', to='stonegarant.Podstavka'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='polirovka',
            field=models.ForeignKey(default=1, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xb0', to='stonegarant.Polirovka'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='stella',
            field=models.ForeignKey(default=1, verbose_name=b'\xd0\xa1\xd1\x82\xd1\x8d\xd0\xbb\xd0\xbb\xd0\xb0', to='stonegarant.Stella'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.BigIntegerField(default=0, verbose_name=b'\xd0\x98\xd1\x82\xd0\xbe\xd0\xb3\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x8f \xd1\x86\xd0\xb5\xd0\xbd\xd0\xb0 \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='user_email',
            field=models.CharField(max_length=150, null=True, verbose_name=b'Email', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 6, 21, 3, 16, 190883), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default=b'N', max_length=1, choices=[(b'N', b'\xd0\x9d\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb9'), (b'S', b'\xd0\x9e\xd1\x82\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd'), (b'D', b'\xd0\x94\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xb2\xd0\xbd\xd0\xb5\xd1\x81\xd0\xb5\xd0\xbd\xd1\x8b'), (b'P', b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb8\xd0\xb7\xd0\xb2\xd0\xbe\xd0\xb4\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe'), (b'C', b'\xd0\x97\xd0\xb0\xd0\xb2\xd0\xb5\xd1\x80\xd0\xb5\xd1\x88\xd0\xb5\xd0\xbd'), (b'R', b'\xd0\x94\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd')]),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_comment',
            field=models.TextField(max_length=150, null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb9 \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8f', blank=True),
        ),
    ]
