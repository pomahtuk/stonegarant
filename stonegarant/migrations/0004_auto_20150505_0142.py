# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stonegarant', '0003_auto_20150505_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='cvetnik',
            name='stella',
            field=models.ForeignKey(verbose_name=b'\xd0\x9c\xd0\xb5\xd0\xbc\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbb', to='stonegarant.Stella', null=True),
        ),
        migrations.AddField(
            model_name='podstavka',
            name='stella',
            field=models.ForeignKey(verbose_name=b'\xd0\x9c\xd0\xb5\xd0\xbc\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbb', to='stonegarant.Stella', null=True),
        ),
        migrations.AddField(
            model_name='polirovka',
            name='stella',
            field=models.ForeignKey(verbose_name=b'\xd0\x9c\xd0\xb5\xd0\xbc\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbb', to='stonegarant.Stella', null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 5, 1, 42, 11, 557844), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
    ]
