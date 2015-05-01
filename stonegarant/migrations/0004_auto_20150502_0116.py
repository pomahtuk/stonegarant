# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stonegarant', '0003_auto_20150501_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memorial',
            name='stella_variants',
        ),
        migrations.RemoveField(
            model_name='stella',
            name='size',
        ),
        migrations.AddField(
            model_name='stella',
            name='height',
            field=models.BigIntegerField(default=0, verbose_name=b'\xd0\x92\xd1\x8b\xd1\x81\xd0\xbe\xd1\x82\xd0\xb0'),
        ),
        migrations.AddField(
            model_name='stella',
            name='length',
            field=models.BigIntegerField(default=0, verbose_name=b'\xd0\x94\xd0\xbb\xd0\xb8\xd0\xbd\xd0\xb0'),
        ),
        migrations.AddField(
            model_name='stella',
            name='memorial',
            field=models.ForeignKey(related_name='stella_variants', verbose_name=b'\xd0\x9c\xd0\xb5\xd0\xbc\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbb', blank=True, to='stonegarant.Memorial', null=True),
        ),
        migrations.AddField(
            model_name='stella',
            name='width',
            field=models.BigIntegerField(default=0, verbose_name=b'\xd0\xa8\xd0\xb8\xd1\x80\xd0\xb8\xd0\xbd\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 2, 1, 16, 40, 768706), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
    ]
