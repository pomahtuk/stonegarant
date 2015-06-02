# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stonegarant', '0003_auto_20150509_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cvetnik',
            field=models.ForeignKey(verbose_name=b'\xd0\xa6\xd0\xb2\xd0\xb5\xd1\x82\xd0\xbd\xd0\xb8\xd0\xba', blank=True, to='stonegarant.Cvetnik', null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='podstavka',
            field=models.ForeignKey(verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xb4\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb0', blank=True, to='stonegarant.Podstavka', null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='polirovka',
            field=models.ForeignKey(verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xb0', blank=True, to='stonegarant.Polirovka', null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 2, 15, 11, 3, 455801), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default=b'D', max_length=1, choices=[(b'D', b'\xd0\xa7\xd0\xb5\xd1\x80\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xb8\xd0\xba'), (b'N', b'\xd0\x9d\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb9'), (b'S', b'\xd0\x9e\xd1\x82\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd'), (b'D', b'\xd0\x94\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xb2\xd0\xbd\xd0\xb5\xd1\x81\xd0\xb5\xd0\xbd\xd1\x8b'), (b'P', b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb8\xd0\xb7\xd0\xb2\xd0\xbe\xd0\xb4\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe'), (b'C', b'\xd0\x97\xd0\xb0\xd0\xb2\xd0\xb5\xd1\x80\xd0\xb5\xd1\x88\xd0\xb5\xd0\xbd'), (b'R', b'\xd0\x94\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd')]),
        ),
        migrations.AlterField(
            model_name='polirovka',
            name='added_value',
            field=models.BigIntegerField(default=0, null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb4\xd0\xb1\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb0 \xd0\xba \xd1\x86\xd0\xb5\xd0\xbd\xd0\xb5 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xbb\xd0\xb5\xd0\xba\xd1\x82\xd0\xb0 (%)', blank=True),
        ),
    ]
