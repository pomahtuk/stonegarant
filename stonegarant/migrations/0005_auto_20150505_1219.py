# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stonegarant', '0004_auto_20150505_0142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cvetnik',
            name='memorial',
        ),
        migrations.RemoveField(
            model_name='podstavka',
            name='memorial',
        ),
        migrations.RemoveField(
            model_name='polirovka',
            name='memorial',
        ),
        migrations.AlterField(
            model_name='cvetnik',
            name='stella',
            field=models.ForeignKey(verbose_name=b'\xd0\xa1\xd1\x82\xd1\x8d\xd0\xbb\xd0\xbb\xd0\xb0', to='stonegarant.Stella', null=True),
        ),
        migrations.AlterField(
            model_name='memorial',
            name='granit',
            field=models.ForeignKey(verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xb3\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x82\xd0\xb0', blank=True, to='stonegarant.Granit', null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 5, 12, 19, 0, 721704), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='podstavka',
            name='stella',
            field=models.ForeignKey(verbose_name=b'\xd0\xa1\xd1\x82\xd1\x8d\xd0\xbb\xd0\xbb\xd0\xb0', to='stonegarant.Stella', null=True),
        ),
        migrations.AlterField(
            model_name='polirovka',
            name='stella',
            field=models.ForeignKey(verbose_name=b'\xd0\xa1\xd1\x82\xd1\x8d\xd0\xbb\xd0\xbb\xd0\xb0', blank=True, to='stonegarant.Stella', null=True),
        ),
    ]
